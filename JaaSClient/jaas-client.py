import sys
import urllib2
from subprocess import Popen, PIPE, check_output, CalledProcessError
from ast import literal_eval


sm_service = 'http://localhost:8080/myapp/myresource'
#cmd = urllib2.urlopen(sm_service).read()

#req = urllib2.Request(sm_service)
#content = urllib2.urlopen(req).read()
#print content


def loadjson(json_str):
    json_dict = None
    try:
        json_dict = literal_eval(str(json_str))
    except Exception, e:
        print('error parsing json', e)
        print sys.exc_traceback.tb_lineno
    return json_dict


# For now writing to a file.
# this will be streamed for future usage
def embedded_python_script(py_src):
    with open('/tmp/script.py', 'w+') as f:
        f.write(py_src)
    try:
        ans = check_output(['python', '/tmp/script.py'])
    except CalledProcessError, e:
        print ("python script errored with...", e, e.returncode)
    finally:
        f.close()
    return ans


def execute_python_script():
    script_url = sm_service + "/script"
    cmd = urllib2.urlopen(script_url).read()
    print embedded_python_script(cmd)


while True:
    execute_python_script()
    cmd = urllib2.urlopen(sm_service).read()
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    #print "executing = '", (cmd), "'"
    #print out.rstrip(), err.rstrip()

    #req = urllib2.Request(sm_service + "/script", urllib.urlencode(out.rstrip()))
    #response = urllib2.urlopen(req)
    #print response.read()

#print JOBID out.rstrip(), err.rstrip()
#print out.rstrip(), err.rstrip()

#list = []
#for args in cmd:
#    call([args])
