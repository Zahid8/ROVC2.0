#import RPi.GPIO
#import RPi.GPIO
import pigpio
from pysticks import get_controller
con = get_controller()

thruster_1 = 9    #Enter the PIN Number to Which Thrsuter 1 is coonected
thruster_2 = 11    #Enter the PIN Number to Which Thrsuter 2 is coonected
thruster_3 = 25  #Enter the PIN Number to Which Thrsuter 3 is coonected
thruster_4 = 8
thruster_pins = [thruster_1,thruster_2,thruster_3,thruster_4]
thvalue = [1500,1500,1500,1500] 
pi = pigpio.pi()
for item in thruster_pins:
    pi.set_servo_pulsewidth(item,1500)



def map_values(value):
    if value < -1 or value > 1:
        return None
    elif value == 0:
        return 1500
    else:
        return int(1500 + (value * 300))    

def map_to_scale(value):
    return int(value * 300)

def forward():
    con.update()

    move=map_values(con.getPitch())
    #turn=map_values(con.getRoll())
    #move=map_to_scale(con.getPitch())
    turn=map_values(con.getRoll())
    pi.set_servo_pulsewidth(thruster_1, move)
    pi.set_servo_pulsewidth(thruster_3, move)
    pi.set_servo_pulsewidth(thruster_2, move)
    pi.set_servo_pulsewidth(thruster_4, move)
    print(move)



while(1):
    forward()