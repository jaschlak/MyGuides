# Check Encryption Ciphers

    These are tricks to scan for encryption settings on a machine
    
## nmap (TLS and ciphers)

    nmap -sV --script ssl-enum-ciphers -p 443 <ip or url>