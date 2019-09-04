# Change Timezone

    This will tell Linux to stay up to date with the timezone you specifiy
    
## From the terminal: ##

    Ubuntu and Mint -           sudo dpkg-reconfigure tzdata followed by the admin/user password.
    Redhat -                    redhat-config-date
    CentOS and Fedora -         system-config-date
    'FreeBSD and Slackware -    tzselect
    
    sudo unlink /etc/localtime                                              # Unlink time with current time zone
    sudo ln -s /usr/share/zoneinfo/America/Chicago /etc/localtime           # Add symbolic link between zoneinfo file and localtime file
    date                                                                    # Check date change took effect
    
### More Resources

    https://www.wikihow.com/Change-the-Timezone-in-Linux
    https://vitux.com/how-to-change-the-timezone-on-your-ubuntu-system/
    