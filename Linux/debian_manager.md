Debian Manager

    Some usefull APT (Advanced Packaging Tool) commands to reference
    
## apt commands

    apt-cache search <string>                   # search for package with string
    apt-get -install <package> [-y]             # install package (optional answer yes to questions) (requires root)
    apt-get remove <package>                    # remove package
    apt-get purge <package>                     # remove package and delete configuration
    
## dpkg (Debian Package) commands (download package file and install locally)

    dpkg -l                                     # display all installed packages
    dpkg -S <filepath>                          # display what package the file belongs to
    dpkg -L <package>                           # display all files in a package
    dpkg -i package.deb                         # install a package
    
