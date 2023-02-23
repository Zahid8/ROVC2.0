import pigpio       # import the library
thruster_one = 5   #gpio8-->the PIN Number to Which Thrsuter 1 is coonected
thruster_two = 7    #gpio7--> the PIN Number to Which Thrsuter 2 is coonected

thruster_pins = [thruster_one, thruster_two] #declaring thruster pins as a  set 
pi = pigpio.pi()

for item in thruster_pins:
    pi.set_servo_pulsewidth(item,1500)


thvalue = [1500, 1500]  # declaring a array of stoping pwm values for thrusters
                        # base pwm values

while (1):              # loop for taking input continiously 
        key = input("enter the opertion you want to perform a) 1 for thruster_1 \n b) 2 for thuster_2 \nc)3 for both\n d) 4 for stop ")
        print("option")
        print(key)
       if (key ==1):   # thruster 1 will move forward 
            thvalue[0] = thvalue[0] + 50
            pi.set_servo_pulsewidth(thruster_one, thvalue[0])
          


        if (key ==2):   # thruster 2 will move forward 
            thvalue[1] = thvalue[1] + 50
            pi.set_servo_pulsewidth(thruster_two, thvalue[1])
           

        if (key ==3):   # both will move forward 
            thvalue[0] = thvalue[0] + 50
            thvalue[1] = thvalue[1] + 50
            pi.set_servo_pulsewidth(thruster_one, thvalue[0])
            pi.set_servo_pulsewidth(thruster_two, thvalue[1])
           
        if (key ==4):   # both will move forward 
            thvalue[0] = 1500
            thvalue[1] = 1500
            pi.set_servo_pulsewidth(thruster_one, thvalue[0])
            pi.set_servo_pulsewidth(thruster_two, thvalue[1])





