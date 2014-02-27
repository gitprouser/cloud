import os
import socket
import traceback
import paramiko
import sys
#import RemoteExecution.ojaas.logger.pythonUtils.commonLogging as logger


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
    # Take a new Logging as a prefix.. Getting out to std if possible
    def __init__(self, time_stamp):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_log_channel(logger.getLogger())        # setting the logger to ojass logging
        self.ssh.load_system_host_keys()                    #
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    """ Helper function to initiate an ssh connection to a host. """
    def ssh_connect(self, host, username, private_key, port=22):
        raise RuntimeError("not implemented")


    def execute_cmd_using_sudo(self, sudo_user, cmd):
        raise RuntimeError("not implemented")


    """ Enables remote connection using ssh """
    def execute_cmd_remote(self, remote_ip, command, pkey, port=22):
        transport = self.get_transport(remote_ip, port)
        channel = transport.open_session()
        channel.exec_command(command)
        output = channel.makefile('rb', -1).readlines()
        self.close(transport)
        return output


    def execute_cmd_remote_with_sudo(self, remote_ip, remote_sudo_user, remote_cmd, args, stdin):
        raise RuntimeError("not implemented")


    """ Helper function to create an SFTP connection from an SSH
        connection. Once a connection is established, a user can use
        conn.get(remotepath) or conn.put(localpath, remotepath) to
        transfer files. """
    def put_file(self, local_fie, remote_ip, remote_file_loc, port=22):
        transport = self.get_transport(remote_ip, port)
        conn = transport.open_sftp_client()
        conn.put(local_fie, remote_file_loc, success_msg = lambda x: "successful work")
        self.close(transport)


    def get_file(self, remote_ip, local_file, remote_file_loc):
        transport = self.get_transport(remote_ip, port)
        conn = transport.open_sftp_client()
        conn.get(remote_file_loc, local_file, success_msg = lambda x: "successful work")
        self.close(transport)


    def execute_cmd(self, cmd, args, stdin):
        raise RuntimeError("not ipmlemented")

    def close(self, transport):
        transport.close()

    def get_transport(self, username, pkey, remote_ip, port=22):
        transport = paramiko.Transport((remote_ip.encode('utf-8'), port))
        if not os.path.exists(pkey):
            raise IOError('The private key file not found')
        rsa_key = paramiko.RSAKey.from_private_key_file(private_key)
        transport.connect(username=username, pkey=rsa_key)
        return transport


    def connect_vm(self, hostname, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.connect((hostname, port))
        except Exception, e:
            logger = self.logger(" --- Connection failed: " + str(e) + traceback.print_exc())


    def __verify_username(self, username):
        if len(username) > 1:
            return username


    # Port error verification.
    def __verify_hostname(self, hostname):
        if hostname.find(':') >= 0:
            hostname, portstr = hostname.split(':')
            port = int(portstr)
            return hostname, port
        m = [x for x in hostname.split(".") if (int(x) > 0 and int(x) <= 255)]
        if len(m) != 4:
            raise Exception("Hostname is not correct")


    class Transport:
        def __init__(self, sock):
            try:
                t = paramiko.Transport(sock)
                try:
                    t.start_client()
                except paramiko.SSHException:
                    Log('*** SSH negotiation failed.')
                    sys.exit(1)

                try:
                    keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
                except IOError:
                    try:
                        keys = paramiko.util.load_host_keys(os.path.expanduser('~/ssh/known_hosts'))
                    except IOError:
                        Log('*** Unable to open host keys file')
                        keys = {}

                # check server's host key -- this is important.
                key = t.get_remote_server_key()
                if not keys.has_key(hostname):
                    Log('*** WARNING: Unknown host key!')
                elif not keys[hostname].has_key(key.get_name()):
                    Log('*** WARNING: Unknown host key!')
                elif keys[hostname][key.get_name()] != key:
                    Log('*** WARNING: Host key has changed!!!')
                    sys.exit(1)
                else:
                    Log('*** Host key OK.')

                agent_auth(t, username)
                if not t.is_authenticated():
                    manual_auth(username, hostname)
                if not t.is_authenticated():
                    Log('*** Authentication failed. :(')
                    t.close()
                    sys.exit(1)

                chan = t.open_session()
                chan.get_pty()
                chan.invoke_shell()
                Log('*** Here we go!')
                print interactive.interactive_shell(chan)
                chan.close()
                t.close()

            except Exception, e:
                print '*** Caught exception: ' + str(e.__class__) + ': ' + str(e)
                traceback.print_exc()
                try:
                    t.close()
                except:
                    pass
                    sys.exit(1)


    """ Connects to a IP when username and password has been provided
            If connection failed throws a System Exit. """
    def connect(self, ip, username, password):
        try:
            ip_number = ip.encode('utf-8')
            self.ssh.connect(ip_number, username=username, password=password)
        except Exception as e:
            sys.exit(-1)

    def ssh_connect_without_pty(self, command):
        """ Execute without user passwd returns the stdin, stdout and stderr back to the caller """
        stdin, stdout, stderr = self.ssh.exec_command(command, get_pty=False)
        return stdin, stdout, stderr

