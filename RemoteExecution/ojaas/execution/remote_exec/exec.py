## Simple script which hits the rest endpoint
## gets the json object
##  - Connects to a server.
##   - Writes to a file.
##  -
##
#from ast import literal_eval
#import urllib
import json
from subprocess import CalledProcessError, check_output
import urllib2

url = "http://localhost:8080/myapp/smproxy"


def embedded_python_script(dict):
    py_src = dict["script"]
    vars = dict["data-bag"]

    with open('/tmp/script.py', 'w+') as f:
        f.write("\n__data_bag = {")
        f.write(("\n\t").join(["\"" + key + "\":" + vars.get(key) + "," for key in vars]))
        f.write("\n\n".join(["}", py_src]))
    try:
        ans = check_output(['python', '/tmp/script.py'])
    except CalledProcessError, e:
        print ("python script errored with...", e, e.returncode)
    finally:
        f.close()
    return ans


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
