import pigpio, time

thruster_one = 18    #Enter the PIN Number to Which Thrsuter 1 is coonected
thruster_two = 8    #Enter the PIN Number to Which Thrsuter 2 is coonected
thruster_three = 12 #Enter the PIN Number to Which Thrsuter 3 is coonected

thruster_pins = [thruster_one, thruster_two, thruster_three]

pi = pigpio.pi()

for item in thruster_pins:
    pi.set_servo_pulsewidth(item,1500)


def idle():
    print(f"\n********* Thruster 1 is in idle state *********\n")
    print(f"\n********* Thruster 2 is in idle state *********\n")
    print(f"\n********* Thruster 3 is in idle state *********\n")

def w(a,b):
    if a >1500 and b >1500:
        print("ROV IS IN MOTION")
        print(f"Thruster 1 is moving forward with {abs(1500-a)} unit speed")
        print(f"Thruster 2 is moving forward with {abs(1500-b)} unit speed")
    elif a == 1500 and b == 1500:
        print("ROV IS AT REST")
    else:
        print("ROV IS IN MOTION")
        print(f"Thruster 1 is moving backward with {abs(1500-a)} unit speed")
        print(f"Thruster 2 is moving backward with {abs(1500-b)} unit speed")

def x(a,b):
    if a >1500 and b> 1500:
        print(f"Thruster 1 is moving forward with {abs(1500-a)} unit speed")
        print(f"Thruster 2 is moving forward with {abs(1500-b)} unit speed")
    elif a==1500 and b == 1500:
        print("ROV IS AT REST")
    else:
        print(f"Thruster 1 is moving backward with {abs(1500-a)} unit speed")
        print(f"Thruster 2 is moving backward with {abs(1500-b)} unit speed")

def cd(m):
    if m>1500:
        print(f"Rov is going up with {abs(1500-m)} unit speed")
    else:
        print(f"Rov is going down with {abs(1500-m)} unit speed")

def e(c):
    if c>1500:
        print(f"Rov is going up with {abs(1500-c)} unit speed")
    else:
        print(f"Rov is going down with {abs(1500-c)} unit speed")

def al(a,b):
    if a == 1500:
        print(f"Left Thruster is Stopped and Rov is turning left and speed of right thruster is {abs(1500-b)}")
    else:
        print(f"Rov is turning Left and speed of thruster 1 is {abs(1500-a)} unit and thruster 2 is {abs(1500-b)} unit")


def d(a,b):
    if b == 1500:
        print(f"right Thruster is Stopped and Rov is turning right and speed of left thruster is {abs(1500-a)}")
    else:
        print(f"Rov is turning right and speed of thruster 1 is {abs(1500-a)} unit and thruster 2 is {abs(1500-b)} unit")

def r():
    print("ROV IS AT REST")


idle()
a = 1500    #Thruster 1
b = 1500    #Thruster 2
c = 1500    #Thruster 3
while True:
    
    val = input()
    if val.lower() == 'w':
        if a<1650 and b<1650:
            a = a + 50
            b = b + 50
            
            pi.set_servo_pulsewidth(thruster_one,a)
            pi.set_servo_pulsewidth(thruster_two,b)
            #pi.set_servo_pulsewidth(thruster_three,c)
            w(a,b)
    if val.lower() == 'x':
        if a>1350 and b> 1350:
            a = a- 50
            b = b - 50
            pi.set_servo_pulsewidth(thruster_one,a)
            pi.set_servo_pulsewidth(thruster_two,b)
            x(a,b)
    if val == 'c':
        c = c - 50
        pi.set_servo_pulsewidth(thruster_three,c)
        cd(c)
    if val == 'e':
        pi.set_servo_pulsewidth(thruster_three,c)
        c = c + 50
        e(c)
    if val.lower() == 'a':
        if a > 1500:
            a = a - 50
        b = b + 50
        pi.set_servo_pulsewidth(thruster_one,a)
        pi.set_servo_pulsewidth(thruster_two,b)
        al(a,b)
        time.sleep(1)
        b = 1500
        a = 1500
        pi.set_servo_pulsewidth(thruster_one,a)
        pi.set_servo_pulsewidth(thruster_two,b)
    if val.lower() == 'd':
        if b > 1500:
            b = b - 50
        a = a +  50
        pi.set_servo_pulsewidth(thruster_one,a)
        pi.set_servo_pulsewidth(thruster_two,b)
        d(a,b)
        time.sleep(1)
        a = 1500
        b = 1500
        pi.set_servo_pulsewidth(thruster_one,a)
        pi.set_servo_pulsewidth(thruster_two,b)
    if val.lower() == 'r':
        a = 1500
        b = 1500
        pi.set_servo_pulsewidth(thruster_one,a)
        pi.set_servo_pulsewidth(thruster_two,b)
        r()
    if val == 'q':
        break