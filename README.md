# ROVC2.0

```pip install pysticks```



# USB forwarding(USB IP)


### On the server side(linux):

1. ```sudo apt-get install linux-tools-generic```

2. ```sudo modprobe usbip_host```

3. ```sudo nano /etc/modules```

4. add ```usbip_host``` to the end of texts

5. ```lsusb``` to see a list of attached USB devices

6. ```sudo usbip list -p -l```

7. ```sudo usbip bind --busid="Bus ID"``` enter busid from the above list command

8. ```sudo usbipd```

### On the client side(rpi):

1. ```wget http://raspbian.mirror.net.in/raspbian/raspbian/pool/main/l/linux/usbip_2.0+5.10.158-2+rpi1_armhf.deb```

2. ```sudo apt install ./usbip_2.0+5.10.158-2+rpi1_armhf.deb```

3. ```sudo modprobe vhci-hcd```

4. ```sudo nano /etc/modules```

5. add ```vhci-hcd``` to the end of texts

6. ```sudo usbip attach -r "IP Address" -b "Bus ID"```


# Installing OpenCV in Raspberry Pi

* Check if you're using all of your system memory with:
``` df -h ```
* If you're not using most of it, then run: 
``` sudo raspi-config ```
 go to advanced -> expand filesystem -> reboot your pi

* Open terminal and type: 
``` sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev ```

* If you're using a PiCamera run:
``` pip install "picamera[array]" ```
* Users of PiCamera may also have to enable Camera Support:
 ``` sudo raspi-config ```
 Inferface Options -> Legacy Camera Support -> Enable

* Install OpenCV
``` pip install opencv-contrib-python ```
