#from ast import literal_eval
import json
from subprocess import Popen, PIPE
import urllib2
import sys

url = "http://localhost:8080/myapp/smproxy"
usr_script = "/tmp/inp_script.py"
gen_script = "/tmp/gen_script.py"
py_path = sys.executable


def embedded_python_script(dict):
    py_src = dict["script"]
    with open(usr_script, 'w+') as f:
        f.write(py_src)
    with open(gen_script, 'w+') as f:
        f.write("\n\n".join(["## GENERATED SCRIPT",  "import %s" % (usr_script[5:-3]),
                             "__data_bag = " + json.dumps(dict["data-bag"]),
                             "## Logger", "%s.execute(__data_bag)" % (usr_script[5:-3])]))

    # ans = check_output("[python gen_script]", subprocess.stderr=STDOUT)
    process = Popen("%s %s" % (py_path, gen_script), shell=True, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    errcode = process.returncode

    f.close()
    if err:
        return "errocode=" + str(errcode) + "\nerr=" + err
    return "errocode = " + str(errcode) + "\nstdout = " + out


# Posting to rest end /receive-task-status
def post(result):
    #params = urllib.urlencode({
    #    'output': result
    #})
    data = urllib2.Request(url + "/receive-task-status", result)
    data.add_header("Content-Type", "application/json")
    data.add_header("Accept", "application/json")
    #print type(data), data.data
    response = urllib2.urlopen(data).read()
    return response


try:
    data = urllib2.urlopen(url + "/get-Task-Details").read()
    result = embedded_python_script(json.loads(data))
    print post(result)
except urllib2.HTTPError, e:
    print "HTTP error: %s" % e
except urllib2.URLError, e:
    print "Network error: %s" % e.reason.args[1]


#def loadjson(json_str):
#    json_dict = None
#    try:
#        json_dict = literal_eval(str(json_str))
#    except Exception, e:
#        print('error parsing json', e)
#        print sys.exc_traceback.tb_lineno
#    return json_dict
