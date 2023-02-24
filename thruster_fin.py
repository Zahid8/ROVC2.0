import ms5837  # librarty of preessure sensor
import time
import pigpio
import numpy as np
from pysticks import get_controller
con = get_controller()

thruster_1 = 9  # Enter the PIN Number to Which Thrsuter 1 is coonected
thruster_2 = 11  # Enter the PIN Number to Which Thrsuter 2 is coonected
thruster_3 = 25  # Enter the PIN Number to Which Thrsuter 3 is coonected
thruster_4 = 8
thruster_pins = [thruster_1, thruster_2, thruster_3, thruster_4]
thvalue = [1500, 1500, 1500, 1500]

pid_p = 0
pid_i = 0
pid_d = 0
kp = 655
ki = 0.00
kd = 655


global time_

sensor = ms5837.MS5837_02BA()
if not sensor.init():
    print("Sensor could not be initialized")
    exit(1)

if not sensor.read():
    print("Sensor read failed!")
    exit(1)


pi = pigpio.pi()
for item in thruster_pins:
    pi.set_servo_pulsewidth(item, 1500)

def map_values_int(value,max_val,min_val):
    if value < -1 or value > 1:
        return None
    elif value == 0:
        return 1500
    else:
        scaled_value = (value + 1) / 2 * (max_val - min_val) + min_val
    return int(scaled_value)



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


def forward():
    con.update()

    up=map_values_int(con.getThrottle(),1900,1100)
    move=map_values_int(con.getPitch(),1900,1100)
    turn=sig(con.getYaw())
    pi.set_servo_pulsewidth(thruster_1, move)
    pi.set_servo_pulsewidth(thruster_3, move)
    print("turn : ", map_values(turn))
    print(move)


def map_values_dynamic(value, max_val, min_val):
    scaled_value = (value + 1) / 2 * (max_val - min_val) + min_val
    return float(scaled_value)

def pid():
    target_depth = map_values_dynamic(con.getThrottle(), 5, 0)
    if sensor.read():
        currentDepth = sensor.depth()
        h = currentDepth+0.25
        time_prev = start_time
        run_time = time.time()
        elapsedTime=(run_time-time_prev)/1000
        print(h)
        error = h-target_depth

        #pid
        previous_error=0
        pid_p = kp * error
        if -0.05 < error < 0.05:
            pid_i = pid_i + (ki * error)
        pid_d = kd * ((error - previous_error) / elapsedTime)
        PID = pid_p + pid_i + pid_d
        if PID < -400:
            PID = -400
        if PID > 400:
            PID = 400
        pwmup = 1500 - PID
        if pwmup < 1100:
            pwmup = 1100
        if pwmup > 1900:
            pwmup = 1900
        print(pwmup)
        pi.set_servo_pulsewidth(thruster_1, pwmup)
        pi.set_servo_pulsewidth(thruster_2, pwmup)
        previous_error = error  
    else:
        print("Sensor read failed!")
        exit(1)

start_time=0

while True:
    start_time = time.time()
    con.update()
    #forward()
    up = map_values_dynamic(con.getThrottle(),5,0)
    move = map_values(con.getPitch())
    turn = sig(con.getYaw())
    #con.update()
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
        if turn == 1500 and move == 1500 and up==0:
            pi.set_servo_pulsewidth(thruster_1, 1500)
            pi.set_servo_pulsewidth(thruster_2, 1500)
            pi.set_servo_pulsewidth(thruster_3, 1500)
            pi.set_servo_pulsewidth(thruster_4, 1500)
            print("thruster stop")
            print(move)
        elif turn!=1500: 
            pi.set_servo_pulsewidth(thruster_2, turn+50)
            pi.set_servo_pulsewidth(thruster_3, turn-50)
            pid()
            print("Thruster 1: ", turn+50)
            print("Thruster 2: ", turn-50)
        elif move!=1500:
            pi.set_servo_pulsewidth(thruster_2, move)
            pi.set_servo_pulsewidth(thruster_3, move)
            pid()
            print("forward thrust: ", move)
        elif up!=0:
            pid()
            #pi.set_servo_pulsewidth(thruster_1, up)
            #pi.set_servo_pulsewidth(thruster_4, up)
            print("up thrust: ", up)
            break
