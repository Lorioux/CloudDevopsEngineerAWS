## What is Needed In This Job?

    1. An image that gets us ready to run Ansible.
    2. A filter to only run this job on master branch.
    3. Our ssh keys/key pair for our EC2 instance.
    4. Install the Ansible CLI in the job.
    5. An inventory file with the hostname or IP address of our EC2 instance in it.
    6. An Ansible playbook that configures the instance and copies files.
    7. A step that executes Ansible.
    8. A dependency in our workflow to make sure the infrastructure creation job finishes before this job runs.

<div style="padding: 16px; margin: 24px;background-color: white;">
    <img src="./roles/files/cicid-wfw.png" />
    <br><br>
    <h2>Deployment Going Smoothly!</h2>
</div>


In case you haven't added your SSH keys to Circle CI yet, check out [these instructions](https://circleci.com/docs/2.0/add-ssh-key) in the doc to do that now.


## Exercise: Configuration and Deployment

Write a job that uses Ansible to configure an EC2 instance and copy production files.
Instructions:

1.    If you don't have a key pair created already in your AWS Console, you should do that now. Folllow [these instructions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair) to create the key pair and save a copy to your computer in a file named `udacity.pem`. We suggest using "udacity" as the key pair name so that it's easier to follow future instructions.
2.    Add the contents of your PEM file to the SSH keys in your Circle CI account so that Ansible will have the creds it needs to access the EC2 instance. You can follow [these instructions](https://circleci.com/docs/2.0/add-ssh-key/) for help doing this. Since you already have SSH keys from your EC2 instance, you can skip step 1.
3.    Manually create an EC2 instance and note it's public IP address for later. Micro/free tier is fine. We suggest ubuntu for better compatibility with the exercise. Be sure to use your "udacity" key pair.
4.    You created the Ansible Playbook to configure infrastructure and copy production files. If it's not already present in your repo, bring in that Playbook now.
5.    Create a job to execute your Playbook.
    
* It should use a docker image that has the necessary settings and dependencies to install Ansible. The docker image `python:3.7-alpine3.11` seems to work well.

* You need to give your job access to your SSH keys saved in your Circle CI account. To do this, follow [these instructions](https://circleci.com/docs/2.0/add-ssh-key/#adding-ssh-keys-to-a-job) to add a section to `add_ssh_keys` to your job.
* Manually add the public IP address of your EC2 instance to the inventory file underneath `[all]`(not automating this since we're not automating the creation of the EC2 instance in this exercise).

6. Define a workflow that uses the job.
7. After your pipeline executes successfully in Circle CI, verify the instance was properly configured.
8. Clean up your EC2 instance by terminating it.


