import socket
import pdb
from subprocess import Popen, PIPE
from thread import *


HOST = ''       # running on All available interfaces
PORT = 9000     # VM Agent will listen on this port

# AF_INET       (this is IPv4 IP)
# SOCK_STREAM   (is a connection oriented TCP protocol)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created"


def exec_command(script):
    p = Popen(script, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print "executing = '", (script), "'"
    print out.rstrip(), err.rstrip()


def client_thread(conn):
    #pdb.set_trace()
    conn.settimeout(0.001)
    try:
        while True:
            script = conn.recv(1024)
            exec_command(script)
            print script
    except socket.timeout:
        conn.sendall("Done...")
        conn.close()


#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print "binding socket to port " + str(PORT) + "failed with Error Code :" + str(msg[0]) + \
          " Message : " + msg[1]

print "socket bind complete"
s.listen(1)
print "socket new listening"


while 1:
    conn, addr = s.accept()
    print "connection established with SM at" + addr[0]
    start_new_thread(client_thread, (conn,))
s.close()
