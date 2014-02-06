import paramiko
import sys


########################
### Establish an SSH
########################
ssh = paramiko.SSHClient()
paramiko.util.log_to_file('ssh.log')
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connect(ip, username, password):
    try:
        ip_number = ip.encode('utf-8')
        ssh.connect(ip_number, username=username, password=password)
    except Exception as e:
        sys.exit(-1)


def ssh_connect_without_pty(command, client=ssh):
    stdin, stdout, stderr = client.exec_command(command, get_pty=True)
    for line in stdout.readlines():
        print line
    if not stderr:
        print "Error with command:" + command
        print "Std error" + stderr
        return False
    else:
        print stdout.read()
        return True


def ssh_connect_with_pty(command, client=ssh):
    channel = client.get_transport().open_session()
    channel.get_pty()
    channel.exec_command(command, )
    try:
        while(True):
            log = channel.recv(65536)
            if (not log):
                break
            else:
                print "log: " + log
    except Exception as e:
        print e.message
    finally:
        channel.close()



def main():
    raise Exception(NotImplemented)

if __name__ == '__main__':
    main()
