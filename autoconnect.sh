#!/bin/bash
a=$(lsusb | grep Logitech)
b=${a:23:9} 
var=$(usbip list -p -l | grep $b)
bus=${var:6:3} 
echo "bus-id" $bus
sudo usbip bind --busid=$bus
sudo usbipd
