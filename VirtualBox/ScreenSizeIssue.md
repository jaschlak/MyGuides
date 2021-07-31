# VirtualBox Screen Issue

    At least with my standard Ubuntu 18.04 my screen is tiny on VirtualBox, apparently VB only allows upt o 128MB for display and you need to modify this
       
## Virtual Box VM Settings

    VM Settings->System->Processor Tab
        Extended Features: Enable PAE/NX
        Extended Features: Enable Nested VT-x/AMD-V
        
    VM Settings->Display->Screen Tab
        Graphics Controller: VBoxVGA
        Acceleration: Enable 3D Acceleration