import time

def execute(inp_data):
    type_vers = inp_data['ServiceTypeCompVersions']
    for ver in type_vers:
        svc_ver = ver['ServiceTypeCompVersion']
        time.sleep(7)
        print "name = " + str(svc_ver['name'])
        print "component = " + str(svc_ver['component'])
        print "cloud-key = " + str(svc_ver['cloudKey'])

