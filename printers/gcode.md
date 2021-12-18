#gcode

    Usefully gcode commands
    https://reprap.org/wiki/G-code#G0_.26_G1:_Move
    
# position

    g90                                 # set to absolute positioning
    g91                                 # set to relative positioning    
    
    G1 X10
    G1 Y10
    G1 Z10
    G1 X000 Y000 Z000
    G1 E20                              # extrude 20mm
    
    M114                                # get current position
    
# home

    G28 Home all 3 axis
    M119                                # get endstop status (triggered bool)
    
# motors

    M18                                 # enable motors
    M17                                 # disable motors    
    
# fan

    M106                                # cooling fan on
    M106 P0                             # cooling fan 0 on
    M106 S255                           # cooling fan on, full speed
    M107                                # cooling fan off
    
# heat

    M104 S100                           # set heat temp
    M108                                # cancel heating    

# dimensions

    g20                                 # set dimensions to inches
    g21                                 # set dimensions to mm
    
# debug

    M111 S1 P15                         # list of debug modules
    M115                                # get firmware info and capabilities
    
# emergency

    M112                                # emergency stop    
    M124                                # immediate motor stop
    
# display

    M117 Hello World
    M118 Change color to blue           # send message to host