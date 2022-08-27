
# android build unity -> apk -> quest

    How to build and push to quest
    
## PreReq

    Quest must be connected via usb-c (link cable)

    Must have unzipped Oculus ADB Driver to your computer somewhere https://developer.oculus.com/downloads/package/oculus-adb-drivers/
    
    Must have installed the android sdk
    https://developer.android.com/studio/releases/platform-tools
    (Download SDK Platform-Tools for Windows)

    Must have built your unity project to Android Platform (produced apk)
    
## Commands

    #open command prompt and navigate to your adb location on your computer
    cd <adb directory>
 
    #look for connected devices
    adb devices
 
    #install with adb
    adb install <apk filepath>
    
