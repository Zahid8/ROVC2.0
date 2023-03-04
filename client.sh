#!/bin/bash
a=$(ifconfig | grep -m 1 inet)
b=${a:12:10} 
c=$(echo $b | cut -d " " -f 2)
d=$(echo $b | cut -d "." -f 4)
e=$(echo $c | sed "s/$d/1/")
echo "Enter bus-id : "
read $bus
sudo usbip attach -r $e -b $bus
