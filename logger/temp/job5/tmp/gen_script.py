import sys

sys.path.append('/Users/dhgajend/my_home/workspace/cloud/logger/temp/ojaas/cloud-master/RemoteExecution')

## GENERATED SCRIPT

import inp_script

__data_bag = {"ServiceTypeCompVersions": [{"ServiceTypeCompVersion": {"releaseDate": "2/21/2014", "isRetired": "false", "name": "JaaS VM Scripts 14.1", "component": "VM_SCRIPTS", "cloudKey": "JaaS/14.0-140221/JaaSVMtoolsScripts.zip", "version": "14.1"}}, {"ServiceTypeCompVersion": {"releaseDate": "12/1/2011", "isRetired": "false", "name": "jdk 1.7.0_45", "component": "JDK", "cloudKey": "JDK/jdk7_u45.zip", "version": "1.7.0_45"}}, {"ServiceTypeCompVersion": {"releaseDate": "12/1/2011", "isRetired": "false", "name": "WLS 10.3.6.0.0", "component": "WLS", "cloudKey": "WLS/11g/fmiddleware.zip", "version": "10.3.6.0.0", "supportedServiceTypeCompVersions": [{"version": "1.7.0_45", "component": "JDK"}]}}, {"ServiceTypeCompVersion": {"releaseDate": "12/1/2011", "isRetired": "false", "name": "WLS 10.3.6.0.6", "component": "WLS", "cloudKey": "WLS/11g/fmiddleware.zip", "version": "10.3.6.0.6", "supportedServiceTypeCompVersions": [{"version": "1.7.0_45", "component": "JDK"}]}}, {"ServiceTypeCompVersion": {"releaseDate": "12/1/2011", "isRetired": "false", "name": "WLS 12.1.0.0.0", "component": "WLS", "cloudKey": "WLS/12c/fmiddleware.zip", "version": "12.1.1.0.0", "type": "JaaS", "supportedServiceTypeCompVersions": [{"version": "1.7.0_45", "component": "JDK"}]}}], "ServiceTypeVersions": [{"ServiceTypeVersion": {"ServiceTypeCompVersions": [{"version": "14.1", "component": "VM_SCRIPTS"}, {"version": "1.7.0_45", "component": "JDK"}, {"version": "10.3.6.0.6", "component": "WLS"}], "version": "11g", "type": "JaaS"}}, {"ServiceTypeVersion": {"ServiceTypeCompVersions": [{"version": "14.1", "component": "VM_SCRIPTS"}, {"version": "1.7.0_45", "component": "JDK"}, {"version": "12.1.1.0.0", "component": "WLS"}], "version": "12c", "type": "JaaS"}}]}

import ojaas.logger.pythonUtils.commonLogging as commonLogging
## LOGGER MODULE ARGS passed in as cpsLogger
commonLogging.setFileName("/Users/dhgajend/my_home/workspace/cloud/logger/temp/job5/logger.log")
commonLogging.setLogFileSeverity(commonLogging.DEBUG)
commonLogging.setFileCount(10)
commonLogging.setFileMinSize(1000)
commonLogging.setConsoleSeverity(commonLogging.INFO)
cpsLogger = commonLogging.getLogger('job5')

inp_script.execute(__data_bag, cpsLogger)