What is Needed in This Job?

1. AWS credentials saved in your project environment variables so they are available to the AWS CLI ([Instructions](https://circleci.com/docs/2.0/env-vars/#setting-an-environment-variable-in-a-project)).
2. An image that has AWS CLI pre-installed.
3. A filter to only run this job on the `master` branch.
4. To check out the code.
5. A step that executes CloudFormation with our template.

<div style="background-color: white; padding: 32px;">

<img src="https://video.udacity-data.com/topher/2020/June/5ef0ccd1_005-d/005-d.png" />

## The "Deploy" Stage Kicks off the Continuous Deployment Portion of CI/CD

</div>


Exercise: Infrastructure Creation

Write a job that creates your infrastructure.
## Instructions:

1.    If you don't have a key pair created already in your AWS Console, you should do that now. Folllow these [instructions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair) to create the key pair and save a copy to your computer in a file named udacity.pem. We suggest using "udacity" as the key pair name so that it's easier to follow future instructions.

2.    To use the AWS CLI in your jobs you'll need to add some environment variables to the Project Settings in Circle CI. You should already have an IAM account with programmatic access from previous exercises. Let's add those credentials as environment variables with these name:

    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_DEFAULT_REGION (ex: us-west-1)

3.    Create a simple CloudFormation template named template.yml that will create some infrastructure. This should be checked into your git repo. You can use your own from previous lessons or you can try this example:

    
```yml
Resources:
    Ec2Instance:
     Type: 'AWS::EC2::Instance'
     Properties:
       SecurityGroups:
         - !Ref InstanceSecurityGroup
       KeyName: udacity
       ImageId: 'ami-068663a3c619dd892' # you may need to find out what instance types are available in your region - use https://cloud-images.ubuntu.com/locator/ec2/
    InstanceSecurityGroup:
     Type: 'AWS::EC2::SecurityGroup'
     Properties:
       GroupDescription: Enable SSH access via port 22
       SecurityGroupIngress:
         - IpProtocol: tcp
           FromPort: '22'
           ToPort: '22'
           CidrIp: 0.0.0.0/0
```

    Notice we are using the `udacity` as the `KeyName`. That refers to the key pair we created before.

    4.    Create a job in your Circle CI config file named create_infrastructure. It should use a docker image that has AWS CLI installed already. This one is perfect: amazon/aws-cli. The job should execute your CloudFormation template to create the infrastructure.
    5.    Define a workflow that uses the job.
    6.    Run the job in Circle CI by committing your changes.
    7.    Once the job has run successfully, check for your new stack in CloudFormation in the AWS Console to see if it was created.
    8.    Remove the stack manually from Cloudformation in the AWS Console to clean up.

