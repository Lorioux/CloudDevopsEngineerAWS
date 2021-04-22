from re import template
import boto3
import os, pathlib2, json, sys, getopt

def help():
    print(
        "Usage: manage-stack.py <-c --create [| -u --update]> <stack-name> \n\n",
        "-c, --create     create a new stack with given name\n",
        "-u, --update     update an existing stack with given name\n",
        "stack-name       stack name\n",
        end="\n"
    )
    sys.exit(2)

def read_template_and_parameters(template_file, param_file):
    template = parameters = ""
    with open(template_file, mode='r') as file:
        for line in file.readlines():
            template += line #input("--template-body> ")

    with open(param_file, mode='r') as file:
        for line in file.readlines():
            parameters += line
    return (template, parameters)

def handle_servers(request, operation, capabilities):
    name = "servers-stack"
    template, parameters = read_template_and_parameters("servers.yml", "serversparams.json")
    response = None
    if operation == "create" :
        try:
            response = create_stack(request, name, template,parameters, capabilities)
            print (response)
        except:
            print (response)
            raise
    elif operation == 'update': 
        try: 
            response = update_stack(request, name, template,parameters, capabilities)
            print (response)
        except:
            print (response)
            sys.exit(1)
    else:
        raise IOError ("Give the intended operation to continue")

def handle_network(request, operation, capabilities):
    template, parameters = read_template_and_parameters("network.yml", "networkparams.json")
    name = "network-stack"
    if operation == "create":
        response = create_stack(request, name, template,parameters, capabilities)
        print (response)
    elif operation == 'update':
        response = update_stack(request, name, template,parameters, capabilities)
        print (response)
    else:
        raise IOError ("Give the intended operation to continue")

def update_stack(request, name, template, parameters, capabilities):
    try:
        return request.update_stack(
                    StackName=name,
                    TemplateBody=template,
                    Parameters=json.loads(parameters),
                    Capabilities=capabilities
                )
    except:
        raise

def create_stack(request, name, template, parameters, capabilities):
    try:
        return request.create_stack(
                    StackName=name,
                    TemplateBody=template,
                    Parameters=json.loads(parameters),
                    Capabilities=capabilities
                )
    except:
        raise

def handle_elbs(request, operation, capabilities):

    template, parameters = read_template_and_parameters("loadbalancers.yml", "elbsparams.json")

    name = "loadbalancers-stack"

    if operation == "create":

        response = create_stack(request, name, template,parameters, capabilities)

        print (response)

    elif operation == 'update':

        response = update_stack(request, name, template,parameters, capabilities)

        print (response)

    else:

        raise IOError ("Give the intended operation to continue")

def main(args):
    BASE_DIR = pathlib2.Path(os.path.dirname(__file__))
    os.chdir(BASE_DIR)
    #print(os.listdir())
    request = boto3.client('cloudformation')
    capabilities = ['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']
    operation = ""

    try:
        opts, miscargs = getopt.getopt(args,"hc:u:",["help","create","update"])
        if len(opts) == 0:
            raise help()
    except getopt.GetoptError:
        help()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            raise help()
        elif opt is None:
            raise help()
        
        if opt in ("-c", "--create"):
            operation = "create"
        elif opt in ("-u", "--update"):
            operation = "update"
        
        if arg == "servers-stack":
            handle_servers(request, operation, capabilities)
        elif arg == "network-stack":
            handle_network(request, operation, capabilities)
        elif arg == "loadbalancers-stack":
            handle_elbs(request, operation, capabilities)
        else:
            response = request.list_stacks(
                StackStatusFilter= ['CREATE_COMPLETE']
            )
            print("\nStackName Not Recognized. Try one  of the following names: ")
            for stack in response['StackSummaries'][0:]:
                print(stack['StackName'], end="\n")

            raise help()
            
if __name__ == '__main__':
    main(sys.argv[1:])