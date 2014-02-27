import time

def execute(inp_data, cpsLogger):
    type_vers = inp_data['ServiceTypeCompVersions']
    cpsLogger.debug('logger') 
    for ver in type_vers:
        svc_ver = ver['ServiceTypeCompVersion']
        time.sleep(5)
        print "name = " + str(svc_ver['name'])
        print "component = " + str(svc_ver['component'])
        print "cloud-key = " + str(svc_ver['cloudKey'])

