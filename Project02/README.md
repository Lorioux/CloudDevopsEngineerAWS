Please, find the related folder "Project02" in this repository. There are three Cloudformation Templates, namely:
1) network.yml
2) servers.yml
3) loadbalancers.yml 

And three parameters files, respectively:
a) networkparams.json
b) serversparams.json
c) elbsparams.json

NOTE: Ignore the other files, such as manage-stack.py and .gitignore.

There have been deployed two publicly accessible app servers in the public subnet and  other two (2) private app servers in the private subnet, accessible throw loadbalancer. 

Here is the loadbalancer dns name: http://loadb-webap-1kacqg0pvsrj2-755061240.us-east-1.elb.amazonaws.com/