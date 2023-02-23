#import RPi.GPIO
#import RPi.GPIO
import pigpio
import numpy as np
from pysticks import get_controller
con = get_controller()

thruster_1 = 9    #Enter the PIN Number to Which Thrsuter 1 is coonected
thruster_2 = 11    #Enter the PIN Number to Which Thrsuter 2 is coonected
thruster_3 = 16  #Enter the PIN Number to Which Thrsuter 3 is coonected
thruster_4 = 8
thruster_pins = [thruster_1,thruster_2,thruster_3,thruster_4]
thvalue = [1500,1500,1500,1500] 
pi = pigpio.pi()
for item in thruster_pins:
    pi.set_servo_pulsewidth(item,1500)


# def ip():

#     con.update()

#     print('Throttle: %+2.2f   Roll: %+2.2f   Pitch: %+2.2f   Yaw: %+2.2f   Aux: %+2.2f' %(con.getThrottle(), con.getRoll(), con.getPitch(), con.getYaw(), con.getAux()))
#     nonlocal pwm = con.getThrottle()
    
def map_values(value):
    if value < -1 or value > 1:
        return None
    elif value == 0:
        return 1500
    else:
        return int(1500 + (value * 300))    

def sig(value):
    if value < -1 or value > 1:
        return None
    elif value == 0:
        return 1500
    else:
        return int((np.sign(value) * (27**(abs(value)) - 1) / (27**(1) - 1)) * 300 + 1500)  

def forward():
    con.update()

    up=map_values(con.getThrottle())
    move=map_values(con.getPitch())
    turn=sig(con.getYaw())
    toggle = con.getAux()

    while(1):
        up=map_values(con.getThrottle())
        move=map_values(con.getPitch())
        turn=sig(con.getYaw())
        toggle = con.getAux()
        prev=1
        curr=toggle
        if(prev==toggle):
            pi.set_servo_pulsewidth(thruster_1, 1500)
            pi.set_servo_pulsewidth(thruster_2, 1500)
            pi.set_servo_pulsewidth(thruster_3, 1500)
            pi.set_servo_pulsewidth(thruster_4, 1500)
            print("thruster off")
            break
        else:
            if turn == 1500 and move == 1500 and up==1500 :
                pi.set_servo_pulsewidth(thruster_1, 1500)
                pi.set_servo_pulsewidth(thruster_2, 1500)
                pi.set_servo_pulsewidth(thruster_3, 1500)
                pi.set_servo_pulsewidth(thruster_4, 1500)
                print("thruster stop")
                print(move)
            elif turn!=1500: 
                pi.set_servo_pulsewidth(thruster_2, turn+50)
                #pi.set_servo_pulsewidth(thruster_1, up)
                #pi.set_servo_pulsewidth(thruster_1, turn+50)
                pi.set_servo_pulsewidth(thruster_3, turn-50)
                print("Thruster 1: ", turn+50)
                print("Thruster 2: ", turn-50)
            elif move!=1500:
                pi.set_servo_pulsewidth(thruster_2, move)
                #pi.set_servo_pulsewidth(thruster_1, up)
                #pi.set_servo_pulsewidth(thruster_1, move)
                pi.set_servo_pulsewidth(thruster_3, move)
                print("forward thrust: ", move)
            elif up!=1500:
                pi.set_servo_pulsewidth(thruster_1, up)
                pi.set_servo_pulsewidth(thruster_4, up)
                #pi.set_servo_pulsewidth(thruster_1, up)
                #pi.set_servo_pulsewidth(thruster_1, move)
                print("up thrust: ", up)
            break

while(1):
    forward()
