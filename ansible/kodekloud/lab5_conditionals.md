# Ansible Condition Statements (When)

    Hopefully this will provide some decent examples of how to use condition statements in Ansible
    
## files

    inventory  
    ansible.cfg  
    nginx.yaml
    age.yaml  
    nameserver.yaml  
    
    
## commands

    ansible-playbook -i inventory age.yaml --check
    ansible-playbook -i inventory age.yaml
    
## ansible.cfg

    [defaults]
    host_key_checking = False
    
## inventory

    node01 ansible_host=node01 ansible_ssh_pass=caleston123
    node02 ansible_host=node02 ansible_ssh_pass=caleston123
    [web_nodes]
    node01
    node02

## nginx.yaml

    -  name: 'Execute a script on all web server nodes'
       hosts: all
       become: yes
       tasks:
         -  name: Install Nginx
            yum:
              name: nginx
              state: present
            when: 'ansible_host=="node02"'
         -  name: Check nginx is running
            service: 'name=nginx state=started'
            when: 'ansible_host=="node02"'
            
## age.yaml

    ---
    - name: 'Am I an Adult or a Child?'
      hosts: localhost
      vars:
        age: 25
      tasks:
        - name: I am a Child
          command: 'echo "I am a Child"'
          when: '{{ age }} < 18'
          
        - name: I am an Adult
          command: 'echo "I am an Adult"'
          when: '{{ age }} >= 18'
          
## nameserver.yaml (note: lineinfile would be cleaner implementation than this conditional)

    ---
    - name: 'Add name server entry if not already entered'
      hosts: localhost
      become: yes
      tasks:
        - shell: 'cat /etc/resolv.conf'
          register: command_output
        
        - shell: 'echo "nameserver 10.0.250.10" >> /etc/resolv.conf'
          when: 'command_output.stdout.find("10.0.250.10") == -1'