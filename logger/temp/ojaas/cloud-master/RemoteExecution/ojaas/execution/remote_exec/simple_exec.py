#from ast import literal_eval
import json
import os
from subprocess import Popen, PIPE
import urllib2
import sys

url = "http://localhost:8080/myapp/smproxy"
py_path = sys.executable


def embedded_python_script(dict, job_dir, ojaas_lib_dir):
    py_src = dict["script"]
    work_dir = job_dir + os.sep + 'tmp'
    if(not os.path.exists(work_dir)):
        os.mkdir(work_dir)
    usr_script = work_dir + os.sep + "inp_script.py"
    gen_script = work_dir + os.sep + "gen_script.py"

    logger = '\n'.join(['import ojaas.logger.pythonUtils.commonLogging as commonLogging',
                        '## LOGGER MODULE ARGS passed in as cpsLogger',
                        'commonLogging.setFileName("%s.log")' % (job_dir + os.sep + 'logger'),
                        'commonLogging.setLogFileSeverity(commonLogging.DEBUG)',
                        'commonLogging.setFileCount(10)', 'commonLogging.setFileMinSize(1000)',
                        'commonLogging.setConsoleSeverity(commonLogging.INFO)',
                        'cpsLogger = commonLogging.getLogger(\'%s\')' %(job_dir.split('/')[-1])])

    with open(usr_script, 'w+') as f:
        f.write(py_src)
    with open(gen_script, 'w+') as f:
        f.write("\n\n".join(["import sys","sys.path.append(\'%s\')" % (ojaas_lib_dir),
                             "## GENERATED SCRIPT",  "import %s" % (usr_script[-13:-3].replace(os.sep,'.')),
                             "__data_bag = " + json.dumps(dict["data-bag"]),
                             logger, "%s.execute(__data_bag, cpsLogger)" % (usr_script[-13:-3]).replace(os.sep,'.')]))

    # ans = check_output("[python gen_script]", subprocess.stderr=STDOUT)
    process = Popen("%s %s" % (py_path, gen_script), shell=True, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    errcode = process.returncode

    f.close()
    return errcode, out, err


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


def infinite_sm_proxy():
    while(True):
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
