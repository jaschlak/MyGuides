# PacketCapture

    This will run a packet capture from command prompt, probably not too useful since Wireshark will sniff and analyze while this only sniffs. 
    Furthermore it creates a .etl and you can convert to .txt but you still need the MicrosoftAnalyzer (Windows Performance Analyzer) or convert with a 3rd party program (ETL2PCAPNG). 
    Either way, if wireshark is not allowed, this is probably not allowed.
    
    Update pktmon works for Windows 10 only, use netsh for Windows Server
    
## Add prefilter (optional)

    pktmon filter add -p 80                               Filters to port 80
    
## Start a capture file

    (navigate to the desired folder for output)
    pktmon start --etw -m
    
## Stop the capture
    pktmon stop
    
## Convert to .txt

    pktmon format <filename>.etl <desiredfilename>.txt
    
## pktmon help
    
    pktmon help
    pktmon <component> help
    pktmon comp help
    

    