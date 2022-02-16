# NMAP

    Commonly used nmap scans
    
## Syn Scan
* basically just gets ports
``` 
nmap -sS <ip> 
```

## Ping discovery
* discover host without pinging host
``` 
nmap -Pn <ip>
``` 

## UDP scans
* scan udp ports, note if no ports found then host not detected
``` 
nmap -sU <ip> 
```

## OS scan
* attempt to detect os of host
``` 
nmap -O <ip> 
```

## Version of services running on host
```
nmap -sV <ip>
```

## Verbose and Very Verbose scan
```
nmap -v <ip>
nmap -vv <ip>
```

## Aggressive scan
* note this one is noisy and will likely get you detected
```
nmap -A <ip>
```

## Port scan: specific, all, scripted
* note: scanning all ports is very time consuming
```
nmap -p <port> <ip> 
nmap -p- <ip>
```

## Script scan
* scan via file you create or premade scripts
* find scripts: locate .nse | grep http
* example linux /usr/share/nmap/scripts/*.nse
* example windows: C:\Program Files (x86)\Nmap\scripts\*.nse
```
nmap --script <script_path> <ip>
nmap --script <script> <ip>
ex: nmap --script http-headers earthchildswmo.com
```

## Script Vulnerability scan
```
nmap --script vuln <ip>
```

## Output to xml
```
nmap -<params> -oX <filename> <ip>
```
