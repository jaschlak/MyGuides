# Jinja utilization in ansible

    Tese are examples of how jinja can be used to modify a variable after recalled.
    Lookup more info at the official jinja2 docs: 
    https://jinja.palletsprojects.com/en/3.1.x/
    
    Lookup ansible extensions to jinja at:
    https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html#formatting-data-yaml-and-json
    
## filter examples: https://jinja.palletsprojects.com/en/3.1.x/templates/#filters

    {{ <var> }}                                                             # calls variable (no filters)
    {{ <var> | upper }}                                                     # upper case the variable
    {{ <var> | lower }}                                                     # lower case the variable
    {{ <var> | title }}                                                     # title style the variable
    {{ <var> | replace ("<old_str>","<new_str>") }}                         # replace string in variable
    {{ <var> | default("<lookup_str>","<inplace_str>") }}                   # if lookup fails for string, replace string with default value
    {{ [<array>] | min }}                                                   # gives minimum value of array
    {{ [<array>] | max }}                                                   # gives maximum value of array
    {{ [<array>] | unique }}                                                # gives unique values of array
    {{ [<array>] | union([<array2>]) }}                                     # joins arrays
    {{ [<array>] | intersect([<array2>]) }}                                 # returns intersecting values in 2 arrays
    {{ <int> | random }}                                                    # returns random number between 1 and int
    {{ [<str_array>] | join("<str or str_array>") }}                        # join string arrays
    
## loop/statements: https://jinja.palletsprojects.com/en/3.1.x/extensions/#loop-controls

    # for loop
    {% for item in <array> %}
        {{ item }}
    {% endfor %}
    
    # if statement
    {% if <number> == <value> %}
        {{ <number> }}
    {% endif %}