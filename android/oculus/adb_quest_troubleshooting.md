# Troubleshoot Quest Development

    Tools to troubleshoot Quest Development
    
## Connect to your quest wirelessly (requires wire upon initial connection)

  1) Download the [Android Debug Bridge SDK](https://developer.android.com/tools/releases/platform-tools)
  2) Extract the directory somewhere
  3) Add that directory to your PATH
  4) Power on your Quest (must be on same wifi network)
  5) Confirm Quest enabled Settings -> Developer -> USB Link Auto-Connect
  6) Check ip address of the Quest Settings -> Wifi -> Select Network -> Scroll down to "IP address"
  7) Connect the laptop to your Quest via USB
  8) On the Quest display click the notification to allow usb debugging
  9) open terminal, run listener server on port 5555, and pass it to wireless
    ```
    adb tcpip 5555
    adb connect <wifi address>:5555
    ```
  10) Unplug Quest
  
  You are now connected to the headset
  
## See devices connected

  `adb devices`
  
## Tear Down Server

  `adb kill-server`
  
## See Unity related logs

  `adb logcat | findstr "Unity"