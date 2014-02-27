import os
import paramiko
import sys


"""
########################
### Establish an SSH
########################
Usage of this module:

Step 1: ssh = new SSHUtils()
Step 2: ssh.connect(IP, username, password)
Step 3: ssh.ssh_connect_sudo("linux command")
Step 4: ssh.ssh_connect("Linux command")
"""
class SSHUtils:
    def __init__(self, time_stamp):
        self.ssh = paramiko.SSHClient()
        paramiko.util.log_to_file('/tmp/ssh.log_%s' % (time_stamp) )
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    def connect(self, ip, username, password):
        """ Connects to a IP when username and password has been provided
            If connection failed throws a System Exit. """
        try:
            ip_number = ip.encode('utf-8')
            self.ssh.connect(ip_number, username=username, password=password)
        except Exception as e:
            sys.exit(-1)


    def ssh_connect_without_pty(self, command):
        """ Execute without user passwd returns the stdin, stdout and stderr back to the caller """
        stdin, stdout, stderr = self.ssh.exec_command(command, get_pty=False)
        return stdin, stdout, stderr
        # for line in stdout.readlines():
        #     print line
        # if not stderr:
        #     print "Error with command:" + command
        #     print "Std error" + stderr
        #     return False
        # else:
        #     print stdout.read()
        #     return True


    def ssh_connect(self, host, username, private_key, port=22):
        """Helper function to initiate an ssh connection to a host."""
        transport = paramiko.Transport((host, port))
        if os.path.exists(private_key):
            rsa_key = paramiko.RSAKey.from_private_key_file(private_key)
            transport.connect(username=username, pkey=rsa_key)
        else:
            raise TypeError("Incorrect private key path")
        return transport


    def sftp_connect(self, transport):
        """Helper function to create an SFTP connection from an SSH
        connection. Once a connection is established, a user can use
        conn.get(remotepath) or conn.put(localpath, remotepath) to
        transfer files. """
        return transport.open_sftp()

    def exec_cmd(self, transport, command):
        """Executes a command on the same server as the provided transport"""
        channel = transport.open_session()
        channel.exec_command(command)
        output = channel.makefile('rb', -1).readlines()
        return output


    def ssh_connect_with_pty(self, command):
        """Returns the logged output of the sudo command. """
        channel = self.ssh.get_transport().open_session()
        channel.get_pty()
        channel.exec_command(command)
        try:
            while(True):
                log = channel.recv(65536)
                if (not log):
                    break
                else:
                    print log
                return log
        except Exception as e:
            raise Exception("The command '%s' execution failed" % (command) + e)
        finally:
            channel.close()


    def close(self):
        self.ssh.close()