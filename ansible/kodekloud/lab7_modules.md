# Ansible Modules

    Ansible modules Examples
    
## files

    ansible.cfg  
    inventory  
    playbook.yaml
    /tmp/install_script.sh

## commands



## inventory

    node01 ansible_host=node01 ansible_ssh_pass=caleston123
    node02 ansible_host=node02 ansible_ssh_pass=caleston123
    [web_nodes]
    node01
    node02
    
## playbook.yaml

    ---
    - name: 'hosts'
      hosts: all
      become: yes
      tasks:
        - name: 'Execute a script'
          script: '/tmp/install_script.sh'
        - name: 'Start httpd service'
          service:
            name: 'httpd'
            state: 'started'
        - name: "Update /var/www/html/index.html"
          lineinfile:
            path: /var/www/html/index.html
            line: "Welcome to ansible-beginning course"
            create: true
        - name: Create User
          user:
            name: web_user
            uid: 1040
            group: developers