# Raspistill

    These are a collection of usefull commands for raspistill, using the ribbon cable camera for the Pi
    
## Turn cameras on

    sudo raspi-config
    Interfaces
    On
    
## Save image

   raspistill -o <filename>.<filetype> 
   
## Save video

    raspivid -o <filename>.h264 <duration (ms)>
    
## More Documentation

    https://glenwperry.github.io/pi/rasberrypi/twitter/2016/12/06/tweeting-motion-cam-rasberry-pi.html