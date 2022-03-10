
# Copy Tricks

    Sometimes you want to do unique things that involve copying folder structures and files. This is meant to be a drop of tricks found
    
## Copy folder structure up to particular file types

    # move to the folder you want to copy from (you likely don't want filepath from root)
    cd <parent file path>
    sudo find . -name '*.<target filetype>' -exec cp --parents \{\} <destination parent directory> \;
    
    #example
    sudo mkdir ~/testhome
    cd /var/project/myproject
    sudo find . -name '*.json' -exec cp --parents \{\} ~/testhome \;
    
    #check example worked
    ls ~/testhome
    find ~/testhome -name '*.json'