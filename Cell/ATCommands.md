# AT Commands

    How to communicate with you cell carrier
    Note: the hardware in place is raspberry pi and quectel BG96 modem on a HAT issued by sixfab 
    Video Resource: https://www.youtube.com/watch?v=g1nxe_J3DVI
    Document Resource: https://support.emnify.com/hc/en-us/articles/360005408633-AT-Command-sequence-for-proper-network-connection-disconnection
    
## Open a connection

    screen /dev/ttyS0 115200                            - open a screen to the tty Serial interface and set the baud rate
        
## Commands 
    
    ### Test Commands   
    AT                                                  test that you can communicate
    ATI                                                 request specs for the modem (IMEI, Manufacturer, Model)
        
    ### Read Commands   
    AT+CPIN?                                            check status of the SIM
    AT+CMEE=2                                           enables extra info when requesting status from the CPIN command above
    AT+QCFG="band"?                                     request modem band configuration -user config
    AT+CREG?                                            what is the network registration status (device state)
    AT+CREG=2                                           enables network registration verbose mode
    AT+COPS?                                            check network registration status 0=none
    AT+CSQ                                              check for signal quality (below 15 = standing next to tower, 30> is bad)
    AT+QCSQ                                             detailed signal info
    AT+QNWINFO                                          check network info
    AT+CGDCONT?                                         get APN info
    AT+CGACT?                                           PDP activation status
    AT+CEDRXRDP                                         check if current cell supports edrx (sleep mode)
        
    Check existing SMS/Read SMS 
    AT+CMGL="ALL"                                       all mode
    AT+CMGF=1                                           text Mode
    AT+CMGL=4   
        
    ### Set Commands
    AT+CGDCONT=<ID>, "<IP(PDP type)>","<APN>"           set communication parameters
    AT+CGDCONT=1,"IPV4V6","vzwinternet"                 set comm example
    AT+QCFG="band",<gsm_band>,<catm1_band>,<nb_band>,1  
    AT+QCFG="band",00000001                             set the GSM band to 900MHZ
    AT+QCFG="band",F,400A0E189F,A0E189F,1               use any band
    AT+CGACT=1,1                                        make active
        
    Band RAT    
    AT+QCFG="nwscanmode"                                configure RATs to be searched
    AT+QCFG="nwscanseq"                                 configure RAT searching sequence
    AT+QCFG="iotopmode"                                 configure network category to be searched under LTE RAT
        
        
    ### Execution Commands  
    AT+CFUN=1,1                                         restart modem
    AT+QPING=1,"google.com"                             ping server/website
        
    Send SMS
    AT+CMGS="+4912223334444
    CTRL_Z=\x1A
    
## Normal Cell Conversation

    Attach (RAN - Radio Access Network)
    Register (Authentication)
    PDN Session (bringing up your APN to get an IP) 