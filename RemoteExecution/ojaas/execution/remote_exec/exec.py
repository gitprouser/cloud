## Simple script which hits the rest endpoint
## gets the json object
##  - Connects to a server.
##   - Writes to a file.
##  -
##
from ast import literal_eval
from subprocess import CalledProcessError, check_output
#import urllib
#import json

import urllib2
import sys

url = "http://localhost:8080/myapp/smproxy"


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
def embedded_python_script(dict):
    py_src = dict["script"]

    with open('/tmp/script.py', 'w+') as f:
        f.write("\ndict = {")
        for vals in dict["data-bag"]:
                f.write("\n\t\"" + vals + "\":" + str(dict["data-bag"].get(vals)) + ",")
        f.write("\n}")
        for x in xrange(2):
            f.write("\n")
        f.write("\n" + py_src)
    try:
        ans = check_output(['python', '/tmp/script.py'])
    except CalledProcessError, e:
        print ("python script errored with...", e, e.returncode)
    finally:
        f.close()
    return ans


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
    dict = loadjson(data)
    result = embedded_python_script(dict)
    print post(result)
except urllib2.HTTPError, e:
    print "HTTP error: %s" % e
except urllib2.URLError, e:
    print "Network error: %s" % e.reason.args[1]
