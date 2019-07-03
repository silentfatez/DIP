# DIP
BLE Functionality for pin forked from frawau/aioblescan

to install rpi screen follow following steps.

cd ~/

git clone https://github.com/tianyoujian/MZDPI.git

cd MZDPI/vga

sudo chmod +x mzdpi-vga-autoinstall-online

sudo ./mzdpi-vga-autoinstall-online

sudo reboot

the BLE feature is forked from aioble scan and it basically plays a video.
Use sudo  to run it with dependencies.

Basically the dip folders files,media and python files, are to be put into their respective rpi and the ble folder files are to be put into rpi 1. It will interact with rpi 2
however we may need to change the ip addresses for us to adapt it to new projects. 
Ssh into the project and register it before using the files provided.
