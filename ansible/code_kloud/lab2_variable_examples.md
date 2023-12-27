# Lab 2 Variable Examples

    This is a good examples of how to use variables.
    Note: user_details is nested and pp_install.yaml has nested items
    
## file structure

    ansible.cfg
    inventory
    playbook.yaml
    app_install.yaml
    user_setup.yaml
    
    
## commands

    ansible-playbook playbook.yaml
    ansible-playbook -i inventory playbook.yaml
    ansible-playbook -i inventory user_setup.yaml
    
## inventory contents

    localhost ansible_connection=local nameserver_ip=8.8.8.8 snmp_port=160-161
    node01 ansible_host=node01 ansible_ssh_pass=caleston123
    node02 ansible_host=node02 ansible_ssh_pass=caleston123
    [web_nodes]
    node01
    node02

    [all:vars]
    app_list=['vim', 'sqlite', 'jq']
    user_details={'username': 'admin', 'password': 'secret_pass', 'email': 'admin@example.com'}
    
## playbook.yaml contents

    ---
    - hosts: localhost
      vars:
        car_model: 'BMW M3'
        country_name: USA
        title: 'Systems Engineer'
      tasks:
        - command: 'echo "My car is {{ car_model }}"'
        - command: 'echo "I live in the {{ country_name }}"'
        - command: 'echo "I work as a {{ title }}"'
        
## app_install.yaml contents

    ---
    - hosts: all
      become: yes
      tasks:
        - name: Install applications
          yum:
            name: "{{ item }}"
            state: present
          with_items:
            '{{ app_list }}'
            
## user_setup.yaml contents

    ---
    - hosts: all
      become: yes
      tasks:
        - name: Set up user
          user:
            name: "{{ user_details.username }}"
            password: "{{ user_details.password }}"
            comment: "{{ user_details.email }}"
            state: present