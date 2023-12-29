# Ansible Loops

    Hopefully these are decent examples of implementing loops in Ansible
    
## files

    ansible.cfg  fruits.yml  inventory  packages.yml
    
## commands



## inventory

    node01 ansible_host=node01 ansible_ssh_pass=caleston123
    node02 ansible_host=node02 ansible_ssh_pass=caleston123
    
## fruits.yml

    ---
    -  name: 'Print list of fruits'
       hosts: localhost
       vars:
         fruits:
           - Apple
           - Banana
           - Grapes
           - Orange
       tasks:
         - command: 'echo "{{ item }}"'
           with_items: '{{ fruits }}'

## packaages.yml

    ---
    -  name: 'Print list of fruits'
       hosts: localhost
       vars:
         fruits:
           - Apple
           - Banana
           - Grapes
           - Orange
       tasks:
         - command: 'echo "{{ item }}"'
           with_items: '{{ fruits }}'