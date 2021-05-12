## Exercise: Remote Control Using Ansible

Build a playbook that automates configuration of an EC2 instance by adapting manual instructions to Ansible Playbook tasks.

### Instructions:

1. If you don't have a key pair already created in your AWS Console, you should do that now! Follow these instructions to create the key pair and save a copy to your computer in a file named udacity.pem. We suggest using "udacity" as the key pair name so that it's easier to follow future instructions.

2. Create a new EC2 instance with a tag like "udacity". As you are creating the instance, be sure to assign the "udacity" key pair. Also, be sure to open up port 3000 for incoming traffic since that's what our web server will use.
    
3. Generate an inventory file using the method you learned from the previous exercise. The public IP of our test EC2 instance should be in the file under the line [all].

4. Create a new Playbook file named main-remote.yml with the following contents:
```yml
---
- name: Exercise for setting up a web server in an EC2
  hosts: all
  user: ubuntu
  roles:
  - setup
```

Notice the reference to ``all`` here. That refers to the ``[all]`` we added to the top of the inventory file in the previous exercise.

5. Create a role for ``setup``. Remember how to do that? Your folder structure should be named after the role and should contain a ``tasks`` folder and a ``files`` folder. Just in case you need a reminder, your folder structure should look like this:

```yml
    /main-remote.yml
    /roles
    /roles/setup
    /roles/setup/tasks
    /roles/setup/files
```

6. Create a simple web server in NodeJS named `index.js`. Add it to the `files` folder so that we can copy it later. That file should have the following code:


```nodejs
var http = require("http");
var server = http.createServer(function (req, res) {
res.writeHead(200);
res.end("Hello world!");
});
server.listen(3000);
```

7. Add a new task file to your `setup` role called `main.yml`. Can you guess where to put that?

8. This task file should contain instructions to handle each one of the manual steps from the [manual instructions](https://www.howtoforge.com/tutorial/nodejs-ubuntu-getting-started/) we provided     (Hello World on NodeJS). As a hint, the file should start by updating and upgrading the packages in the Ubuntu server like this:


```yml
---
- name: "update apt packages."
  become: yes
  apt:
    update_cache: yes

- name: "upgrade packages"
  become: tyes
  apt:
    upgrade: yes
```

    You'll need several other tasks to fully configure the instance. Some will need `become: yes` and others will not depending on if you need privilege escalation.

9. Now let's run the Playbook using your inventory file and `udacity.pem` file:

```shell
ansible-playbook main-remote.yml -i inventory --private-key udacity.pem
```

10. After running all the plays, Ansible should give you a successful message.
11. You should be able to navigate to the hostname:port (e.g. `3000`) of the instance and view your Hello World message.
12. Terminate any test EC2 instances you created for this exercise to clean up.