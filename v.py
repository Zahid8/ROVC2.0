#!/usr/bin/env python3
'''
tester.py: Test program for PySticks

Requires: pygame

Copyright (C) Simon D. Levy 2016

This file is part of Hackflight.

Hackflight is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License 
along with this code.  If not, see <http:#www.gnu.org/licenses/>.
'''
import pigpio
from pysticks import get_controller
con = get_controller()
global x
thruster_one = 9    #Enter the PIN Number to Which Thrsuter 1 is coonected
thruster_two = 11    #Enter the PIN Number to Which Thrsuter 2 is coonected
thruster_3 = 25  #Enter the PIN Number to Which Thrsuter 3 is coonected
thruster_4 = 8
thruster_pins = [thruster_one,thruster_two,thruster_3,thruster_4]
thvalue = [1500, 1500,1500,1500] 
pi = pigpio.pi()
for item in thruster_pins:
    pi.set_servo_pulsewidth(item,1500)

    
while True:

    try:

        con.update
        print('Throttle: %+2.2f   Roll: %+2.2f   Pitch: %+2.2f   Yaw: %+2.2f   Aux: %+2.2f' %(con.getThrottle(), con.getRoll(), con.getPitch(), con.getYaw(), con.getAux()))
                #f forward():
        
        # pwm = con.getThrottle()
        # if (con.getThrottle()>0.83):
            
            # x = pwm - 0.83 
            # x= x*100
            # x=x/2.82
            # x= x*50 + thvalue[0]
        thvalue[0] = (((con.getThrottle() - 0.83) *100)/2.83)*50+ thvalue[0]
        print(thvalue[0])
        pi.set_servo_pulsewidth(thruster_one, thvalue[0])
        print(thvalue[0])
        
                # forward()
    except KeyboardInterrupt:
        break