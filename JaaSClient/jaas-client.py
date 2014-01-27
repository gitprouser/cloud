import urllib2
from subprocess import Popen, PIPE

sm_service = 'http://localhost:8080/myapp/myresource'
#cmd = urllib2.urlopen(sm_service).read()

#req = urllib2.Request(sm_service)
#content = urllib2.urlopen(req).read()
#print content



while True:
    cmd = urllib2.urlopen(sm_service).read()
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print "executing = '", (cmd), "'"
    print out.rstrip(), err.rstrip()

#print JOBID out.rstrip(), err.rstrip()
#print out.rstrip(), err.rstrip()

#list = []
#for args in cmd:
#    call([args])
