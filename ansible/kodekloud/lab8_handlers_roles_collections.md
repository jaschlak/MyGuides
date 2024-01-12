# Ansible Handlers, Roles, and Collections

    Examples
    
## files

    .
    |---ansible_lab
    |   |
    |   |-files
    |   | |-file1.conf
    |   | |-file2.conf
    |   |
    |   |-handler_test.yml
    |   
    |-playbooks
      |
      |-requirements.yml
      |-playbook.yml (installed)
        
## commands

    ansible-galaxy collection install -r requirements.yml
    ansible-playbook handler_test.yml
    
## ./playbooks/requirements.yml

    ---
    collections:
      - name: community.general
        version: '1.0.0'
      - name: amazon.aws
        version: '1.2.1'
        
## ./playbooks/playbook.yml

    # note: this is installing a custom library from namespace "company_xyz", collection "networking_tools", module "configure_vlan"
    
    ---
    - hosts: localhost
      tasks:
        - name: Install the networking_tools collection
          ansible.builtin.ansible_galaxy_collection:
            name: company_xyz.networking_tools
            source: https://galaxy.ansible.com

    - hosts: switches
      collections:
        - company_xyz.networking_tools
      tasks:
        - name: Configure VLAN 10
          configure_vlan:
            vlan_id: 10
            vlan_name: Admin_VLAN
            
## ./ansible_lab/handler_test.yml

    ---
    - name: Test Handler Execution
      hosts: localhost
      tasks:
        - name: Copy file1.conf
          copy:
            src: files/file1.conf
            dest: /tmp/file1.conf
          notify: Sample Handler

        - name: Copy file2.conf
          copy:
            src: files/file2.conf
            dest: /tmp/file2.conf
          notify: Sample Handler

      handlers:
        - name: Sample Handler
          debug:
            msg: "Handler has been triggered!"