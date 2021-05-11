# Project 03

## Configure and Execute C/CD Pipelines With  CircleCI and Ansible 



### Continous Deployment Configuration W/ Ansible

Our objective will be to print the contents of an environment variable to the console using an Ansible Playbook via a role.

#### Steps
Here we assume, we already have installed Ansible in our workstation.

    1). Create a new Ansible Playbook file named main.yml (starting out, it's just a blank text file).
    2). Create a new directory named roles.
    3). In the roles directory, create a new folder called print.
    4). Inside print, create a new folder called tasks.
    5). Your folder structure should look like this:
    `
    /main.yml
    /roles
    /roles/print
    /roles/print/tasks
    `

    6). Create a task to be executed by the role. Name it `/roles/print/tasks/main.yml` and add the following content:
    `
    ---
        - name: Print env variable
        shell: echo $PATH
        register: print_result

        - name: print message
        debug:
            msg: "{{ print_result.stdout_lines }}"
    `

    7). Navigate back to the folder that contains your Playbook (in case you navigated away).

    8). Add the following code to your Playbook file:
    `
    ---
        - name: Exercise #1
        hosts: localhost

        roles:
        - print
    `
    Notice that we reference a role named print. We didn't mention a path to the task file. That's because Ansible knows where to look as long as we follow the folder structure convention!

    9). Run your playbook using the command `ansible-playbook main.yml`.

10). You should see some results like the following:
`
TASK [print : print message]     ************************************************************************
ok: [localhost] => {
    "msg": [
        "/home/user/.local/bin:/home/user/bin:/usr/local/sbin:/usr/local/bin:/usr/    sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"
    ]
}
`