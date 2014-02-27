import sys
import os
import json

#logger = logging.getLogger('LOG')
#logger.setLevel(logging.DEBUG)
#log_file = logging.FileHandler('runner.log')
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logger.addHandler(log_file)


workspace = '/Users/dhgajend/my_home/workspace/cloud/logger/temp'
ojaas_lib_dir = workspace + os.sep + 'ojaas/cloud-master/RemoteExecution'
if os.path.exists(ojaas_lib_dir):
    sys.path.append(ojaas_lib_dir)
    import ojaas.execution.remote_exec.simple_exec as simple_exec
    import ojaas.logger.pythonUtils.commonLogging as commonLogging
    #Set configuration value
    commonLogging.setFileName('test.log')
    commonLogging.setLogFileSeverity(commonLogging.DEBUG)
    commonLogging.setFileCount(10)
    commonLogging.setFileMinSize(1000)
    commonLogging.setConsoleSeverity(commonLogging.INFO)
    commonLogging.displayConfigStatus()
    logger = commonLogging.getLogger('CPSLogger')


def read_file(file):
    with open(file, 'r') as f:
        return "".join(f.readlines())


def write_file(file, msg):
    with open(file, 'w+') as f:
        f.write(msg)


def build_job_dict(dir):
    scriptlet = read_file(dir + os.sep + 'script.py')
    #print scriptlet
    dict = {'data-bag': json.load(open(dir + os.sep + 'data.json')), 'script': scriptlet}
    #print pprint.pprint(dict)
    return dict



jobs = ['job1', 'job2', 'job3', 'job4', 'job5']
children = []
logger.debug('Executing jobs under the jobs directory')
for job in jobs:
    job_dir = workspace + os.sep + job
    dict = build_job_dict(job_dir)
    logger.debug('Executing job ' + job)
    pid = os.fork()
    if pid:
        write_file(job_dir + os.sep + 'pid', str(pid))
        children.append(pid)
    else:
        errcode, out, err = simple_exec.embedded_python_script(dict, job_dir, ojaas_lib_dir)
        write_file(job_dir + os.sep + 'errcode', str(errcode))
        write_file(job_dir + os.sep + 'out', out)
        write_file(job_dir + os.sep + 'err', err)
        os._exit(0)

#logger.debug("waiting for all jobs to complete")
#for i, child in enumerate(children):
#    os.waitpid(child, 0)
logger.debug("Completed...")
