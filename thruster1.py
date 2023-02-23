#import RPi.GPIO
#import RPi.GPIO
import pigpio
import numpy as np
from pysticks import get_controller
con = get_controller()

thruster_one = 9    #Enter the PIN Number to Which Thrsuter 1 is coonected
thruster_two = 11    #Enter the PIN Number to Which Thrsuter 2 is coonected
thruster_3 = 25  #Enter the PIN Number to Which Thrsuter 3 is coonected
thruster_4 = 8
thruster_pins = [thruster_one,thruster_two,thruster_3,thruster_4]
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
        return int((np.sign(value) * (27*(abs(value)) - 1) / (27*(1) - 1)) * 300 + 1500)  
    


def map_to_scale(value):
    return int(value * 300)

def forward():
    con.update()

    move=map_values(con.getPitch())
    #move=sig(con.getYaw())
    #turn=map_values(con.getRoll())
    #move=map_to_scale(con.getPitch())
    #turn=map_to_scale(con.getRoll())
    pi.set_servo_pulsewidth(thruster_one, move)
    pi.set_servo_pulsewidth(thruster_3, move)
    #print("move : ",map_values(move))
    #print("turn : ",map_values(turn))

    #thvalue[0] = move
    #thvalue[1] = move
    # if move==1500 and turn == 1500:

    #     pi.set_servo_pulsewidth(thruster_one, 1500)
    #     pi.set_servo_pulsewidth(thruster_two, 1500)

    # if move !=1500:
    #     thvalue[0] = move
    #     thvalue[1] = move
    #     pi.set_servo_pulsewidth(thruster_one, move)
    #     pi.set_servo_pulsewidth(thruster_two, move)
    # if turn != 1500:
    #     thvalue[0] = turn
    #     thvalue[1] = turn
    #     if turn > 1500:  #right
    #         pi.set_servo_pulsewidth(thruster_one, 1500+turn)
    #         pi.set_servo_pulsewidth(thruster_two, 1500-turn)

    #     if turn < 1500: #left
    #         pi.set_servo_pulsewidth(thruster_one, 1500-turn)
    #         pi.set_servo_pulsewidth(thruster_two, 1500+turn)
    print(move)











    # if turn >= -300 and turn < 0:
    #     pi.set_servo_pulsewidth(thruster_one, 1500+turn)
    #     pi.set_servo_pulsewidth(thruster_two, 1500-turn)

    # elif turn >= 0 and turn <= 300:
    #     pi.set_servo_pulsewidth(thruster_one, 1500-turn)
    #     pi.set_servo_pulsewidth(thruster_two, 1500+turn)

    # if move >= 1200 and move < 1500:
    #     pi.set_servo_pulsewidth(thruster_one, move)
    #     pi.set_servo_pulsewidth(thruster_two, move)

    # elif move >= 1500 and move <= 1800:
    #     pi.set_servo_pulsewidth(thruster_one, move)
    #     pi.set_servo_pulsewidth(thruster_two, move)

while(1):
    forward()
# def backward():
#     if (0.66< pwm and pwm < 0.83):
#         x= pwm - 0.66 
#         x= x*100
#         X=x/2.82
#         X= X*50
#     thvalue[0] = thvalue[0] + X
#     pi.set_servo_pulsewidth(thruster_one, thvalue[0])
#     print(thvaue[0])
# pi.set_servo_pulsewidth(thruster_one,1500)
# pi.set_servo_pulsewidth(thruster_two,1500)
# pi.set_servo_pulsewidth(thruster_3,1500)
# pi.set_servo_pulsewidth(thruster_4,1500)
# while (1):              # loop for taking input continiously


#         key = int(input("enter the opertion you want to perform \na) 1 for thruster_1 \n b) 2 for thuster_2 \nc)3 for both\n d) 4 for stop\n"))
#         print("option:\t")
#         print(key)
#         if (key ==1):   
#             thvalue[0] = thvalue[0] + 50
#             thvalue[0] = thvalue[1] + 50
#             pi.set_servo_pulsewidth(thruster_one, thvalue[0])
#             pi.set_servo_pulsewidth(thruster_two, thvalue[1])
#             print("thrusters are moving forward pwm value")
#             print(thvalue[0])
#         if (key == 2):
#             thvalue[0]=1500
#             thvalue[1]=1500
#             pi.set_servo_pulsewidth(thruster_one,1500)
#             pi.set_servo_pulsewidth(thruster_two, 1500)
#             print("thrusters are at rest  pwm value")
#             print(thvalue[0])
#         if (key == 3):
#             thvalue[0] = thvalue[0] - 50
#             thvalue[0] = thvalue[1] - 50
#             pi.set_servo_pulsewidth(thruster_one, thvalue[0])
#             pi.set_servo_pulsewidth(thruster_two, thvalue[1])
#             print("thrusters are moving with pwm value")
#             print(thvalue[0])
#         if (key == 4):   
#             thvalue[2] = thvalue[2] + 50
#             thvalue[3] = thvalue[3] + 50
#             pi.set_servo_pulsewidth(thruster_3, thvalue[2])
#             pi.set_servo_pulsewidth(thruster_4, thvalue[3])
#             print("thrusters are moving upward pwm value")
#             print(thvalue[0])
        