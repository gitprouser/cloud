Remote Execution Support
===========================
Remote Execution support on any cloud platform. Any cloud enabled 
enterprise deployment blocks ports for any outside communication

This is a prototype framework which schedules and executes jobs on VMs
using the concept of VMAgents. 

Essential Architecture
Job server (1) <---> VMAgent (N) many 

The Job server: Has REST end points and is connected to the outside 
world. Tasks can be given to the VMAgent via Server using the REST end
points provided by the server.


A Service Manager will schedule jobs which need to be run on the client
 
A piece of code in Ruby, Python, Java and Shell should be executed from 
the remote client on the VM. The remote execution script would be 
executed at boot time and would exist over the duration of the VM. 
There are two pieces to the this job. The server side and the client 
side.

