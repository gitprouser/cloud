import ojaas.sm_connect.ssh_util as ssh
from datetime import datetime as d
import re


timestamp = re.sub(r"[^0-9]","_","_".join([str(d.now().date()), str(d.now().time())]))
print (str(timestamp).strip())
client = ssh.SSHUtils(timestamp)
client.connect('10.249.128.91','dhgajend','Muruga549.')
print client.ssh_connect_with_pty("ls -al")
client.close()
