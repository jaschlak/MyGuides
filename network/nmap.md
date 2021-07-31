# NMAP

    Commonly used nmap scans
    
    ## Simple Scan
    *basically just gets ports
    ``` 
    nmap -sS <ip> 
    ```

    ## UDP scans
    *Scan udp ports, note if no ports found then host not detected
    ``` 
    nmap -sU <ip> 
    ```

    ## OS scan
    *attempt to detect os of host
    ``` 
    nmap -O <ip> 
    ```