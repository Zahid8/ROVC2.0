#import RPi.GPIO
#import RPi.GPIO
import pigpio
thruster_1 = 9
thruster_2 = 11
thruster_3= 16
thruster_4= 8
thruster_pins = [thruster_1,thruster_2,thruster_3,thruster_4]
thvalue = [1500, 1500,1500,1500] 
pi = pigpio.pi()
for item in thruster_pins:
     pi.set_servo_pulsewidth(item,1500)



#thvalue=input("enter the pwm value ")

pi.set_servo_pulsewidth(thruster_1,1500)
pi.set_servo_pulsewidth(thruster_2,1500)
pi.set_servo_pulsewidth(thruster_3,1500)
pi.set_servo_pulsewidth(thruster_4,1500)
