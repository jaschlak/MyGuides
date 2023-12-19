Services

    Service maintenance on Linux
    
Recon

    # services (all)
    systemctl list-units --type=service
    ls -l /etc/systemd/system /usr/lib/systemd/service | egrep .service$
    service --status-all
    
    # individual service details
    systemctl status <service name>
    
Control

    Commands: stop start restart

    systemctl <command> <service name>