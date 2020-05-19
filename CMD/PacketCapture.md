# PacketCapture

    This will run a packet capture from command prompt, probably not too useful since Wireshark will sniff and analyze while this only sniffs. Furthermore it creates a .etl and you can convert to .txt but you still need the Microsoft Analyzer (Windows Performance Analyzer) or convert with a 3rd party program (ETL2PCAPNG). Either way if you can't use wireshark they probably don't want you packet analyzers running and wont allow installation of these programs
    
## Add prefilter 

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
    

    