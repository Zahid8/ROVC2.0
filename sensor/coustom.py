from tkinter import *
import cv2
import pigpio
from PIL import Image as Img
from PIL import ImageTk
from tkinter import *
import ms5837
import time
sensor = ms5837.MS5837_30BA() # Default I2C bus is 1 (Raspberry Pi 3)
#sensor = ms5837.MS5837_30BA(0) # Specify I2C bus

# We must initialize the sensor before reading it
if not sensor.init():
    print("Sensor could not be initialized")
    exit(1)

# We have to read values from sensor to update pressure and temperature
if not sensor.read():
    print("Sensor read failed!")
    exit(1)

print(("Pressure: %.2f atm %.2f Torr %.2f psi") % (
sensor.pressure(ms5837.UNITS_atm),
sensor.pressure(ms5837.UNITS_Torr),
sensor.pressure(ms5837.UNITS_psi)))

print(("Temperature: %.2f C %.2f F %.2f K") % (
sensor.temperature(ms5837.UNITS_Centigrade),
sensor.temperature(ms5837.UNITS_Farenheit),
sensor.temperature(ms5837.UNITS_Kelvin)))
def dep():
    freshwaterDepth = sensor.depth() # default is freshwater
    sensor.setFluidDensity(ms5837.DENSITY_SALTWATER)
    saltwaterDepth = sensor.depth() # No nead to read() again
    sensor.setFluidDensity(1000) # kg/m^3
    print(("Depth: %.3f m (freshwater) %.3f m (saltwater)") % (freshwaterDepth, saltwaterDepth))
    f = str(freshwaterDepth * 1)
    s = str(saltwaterDepth * 1)
    e_result = "        depth = freshwater depth   "+ f + ",  salt water depth "+ s
    return e_result
    

# fluidDensity doesn't matter for altitude() (always MSL air density)
print(("MSL Relative Altitude: %.2f m") % sensor.altitude()) # relative to Mean Sea Level pressure in air

# Create an instance of TKinter Window or frame
app = Tk()

width = app.winfo_screenwidth()
height = app.winfo_screenheight()
# Set the size of the window
app.geometry("%dx%d" % (width, height))

# Create thvalue[0] Label to capture the Video frames
# label =Label(app )
# label.place(relwidth=1, relheight=0.45, rely=0.03)
# label.place(x  = 25 , y = 5 , height= 450 , width= 900)
# label.grid(row=0, column=0, columnspan=5, padx = 20 , pady=40)
# cap= cv2.VideoCapture(0)

# Define function to show frame
# def show_frames():
#    # Get the latest frame and convert into Image
#    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
#    img = Image.fromarray(cv2image)
#    # Convert image to PhotoImage
#    imgtk = ImageTk.PhotoImage(image = img)
#    label.imgtk = imgtk
#    label.configure(image=imgtk)
#    # Repeat after an interval to capture continiously
#    label.after(1, show_frames)

# show_frames()

thruster_one = 10    #Enter the PIN Number to Which Thrsuter 1 is coonected
thruster_two = 7    #Enter the PIN Number to Which Thrsuter 2 is coonected
thruster_three = 3  #Enter the PIN Number to Which Thrsuter 3 is coonected
thruster_four = 27  #Enter the PIN Number to Which Thrsuter 4 is coonected

thruster_pins = [thruster_one, thruster_two, thruster_three, thruster_four]

pi = pigpio.pi()

for item in thruster_pins:
    pi.set_servo_pulsewidth(item,1500)



thvalue = [1500, 1500,1500,1500]

def forward(eve):
   if thvalue[0] < 1850 and thvalue[1]<1850:
      thvalue[0] = thvalue[0] + 10
      thvalue[1] = thvalue[1] + 10
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])

   if thvalue[0] > 1500 and thvalue[1] > 1500:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving forward with " + \
      str(abs(1500-thvalue[0])) +  " unit speed \n" + \
            "Thruster 2 is moving forward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"

   elif thvalue[0] == 1500 and thvalue[1] == 1500:
      result_str = "ROV IS AT REST"

   else:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving backward with " + \
      str(abs(1500-thvalue[0])) + " unit speed \n" + \
            "Thruster 2 is moving backward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"
   
   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   if thvalue[2]<1500:
      more_str = " \nROV IS moving Vertically Down with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)
   if thvalue[2]>1500:
      more_str = " \nROV IS moving Vertically UP with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)


def backward(eve):
   if thvalue[0] > 1150 and thvalue[1] > 1150:
      thvalue[0] = thvalue[0] - 10
      thvalue[1] = thvalue[1] - 10
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])

   if thvalue[0] > 1500 and thvalue[1] > 1500:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving forward with " + \
      str(abs(1500-thvalue[0])) + " unit speed \n" + \
            "Thruster 2 is moving forward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"

   elif thvalue[0] == 1500 and thvalue[1] == 1500:
      result_str = "ROV IS AT REST"

   else:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving backward with " + \
      str(abs(1500-thvalue[0])) + " unit speed \n" + \
            "Thruster 2 is moving backward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   if thvalue[2]<1500:
      more_str = " \nROV IS moving Vertically Down with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)
   if thvalue[2]>1500:
      more_str = " \nROV IS moving Vertically UP with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)

def down(eve):
   if thvalue[2] <= 1800 and thvalue[2]>1200:
      thvalue[2] = thvalue[2] - 10
      thvalue[3] = thvalue[3] - 10
      pi.set_servo_pulsewidth(thruster_three, thvalue[2])
      pi.set_servo_pulsewidth(thruster_four, thvalue[3])

   if thvalue[2] > 1500:
      result_str = "Rov is going up with " + str(abs(1500-thvalue[2])) + " unit speed"
   elif thvalue[2] == 1500:
      result_str = "Vertical Motion Of Rov has Stopped"
   else:
      result_str = "Rov is going down with " + str(abs(1500-thvalue[2])) + " unit speed"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   ele.insert(END,dep())
   if thvalue[0]!=1500 or thvalue[1] != 1500:
      more_str =  "\n ROV Is also in Horizontal Forward Motion " + \
          "You can Press Enter to Stop It "
      ele.insert(INSERT, more_str)

def upward(eve):
   if thvalue[2]>=1200 and thvalue[2]<1800:
      thvalue[2] = thvalue[2] + 10
      thvalue[3] = thvalue[3] + 10
      pi.set_servo_pulsewidth(thruster_three, thvalue[2])
      pi.set_servo_pulsewidth(thruster_four, thvalue[3])

   if thvalue[2] > 1500:
      result_str = "Rov is going up with " + str(abs(1500-thvalue[2])) + " unit speed"
   elif thvalue[2] == 1500:
      result_str = "Vertical Motion Of Rov has Stopped"
   else:
      result_str = "Rov is going down with " + str(abs(1500-thvalue[2])) + " unit speed"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   if thvalue[0]!=1500 or thvalue[1] != 1500:
      more_str =  "\n ROV Is also in Horizontal Forward Motion " + \
          "You can Press Enter to Stop It "
      ele.insert(INSERT, more_str)

def left(eve):
   if thvalue[0] > 1500:
      thvalue[0] = thvalue[0] - 50
      thvalue[1] = thvalue[1] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning left and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   elif thvalue[0] == 1500:
      thvalue[1] = thvalue[1] + 10
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Left Thruster is Stopped and Rov is turning left\n and speed of right thruster is " + \
         str(abs(1500-thvalue[1])) + " unit"

   else:
      thvalue[0] = thvalue[0] + 10
      thvalue[1] = thvalue[1] - 10
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning right and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   if thvalue[2]<1500:
      more_str = " \nROV IS moving Vertically Down with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)
   if thvalue[2]>1500:
      more_str = " \nROV IS moving Vertically UP with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)

def right(eve):
   if thvalue[1] > 1500:
      thvalue[1] = thvalue[1] - 50
      thvalue[0] = thvalue[0] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning right and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   elif thvalue[1] == 1500:
      thvalue[0] = thvalue[0] + 10
      # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      result_str = "right Thruster is Stopped and Rov is turning right\n and speed of left thruster is " + str(abs(1500-thvalue[0])) + " unit"

   else:
      thvalue[0] = thvalue[0] - 50
      thvalue[1] = thvalue[1] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning left and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"
   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   if thvalue[2]<1500:
      more_str = " \nROV IS moving Vertically Down with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)
   if thvalue[2]>1500:
      more_str = " \nROV IS moving Vertically UP with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)

def reset(eve):
   thvalue[0] = 1500
   thvalue[1] = 1500
   thvalue[2] = 1500
   thvalue[3] = 1500
   pi.set_servo_pulsewidth(thruster_one, thvalue[0])
   pi.set_servo_pulsewidth(thruster_two, thvalue[1])
   pi.set_servo_pulsewidth(thruster_three, thvalue[2])
   pi.set_servo_pulsewidth(thruster_four, thvalue[3])
   result_str = "ROV IS AT REST"
   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)




result = "Rov is not in Motion \nAll The thrusters aare in Idle State"

e =0

button_forward = Button(app, text="↑" , padx=40, pady=20 , command = lambda : forward(e)).place(x = 160 , y= 510)
button_backward = Button(app, text="↓" , padx=40, pady=20,command = lambda : backward(e)).place(x=160,y=575 )
button_left = Button(app, text="←" , padx=40, pady=20 ,command = lambda : left(e)).place(x=50, y=575 )
button_right = Button(app, text="→" , padx=40, pady=20,command = lambda : right(e)).place(y =575, x = 270  )
button_up = Button(app, text="UP" , padx=40, pady=20,command = lambda : upward(e)).place(x = 380,  y= 510 )
button_down = Button(app, text="Down" , padx=40, pady=20,command = lambda : down(e)).place(x = 380 , y= 575 ) 
button_reset = Button(app, text="RESET" , padx=40, pady=20 , command = lambda : reset(e)).place(x = 100, y  = 680)




app.bind('<Key-Up>',forward)
# app.bind('<KeyRelease-Up>',reset)
app.bind('<Key-Left>',left)
# app.bind('<KeyRelease-Left>',reset)
app.bind('<Key-Down>',backward)
# app.bind('<KeyRelease-Down>',reset)
app.bind('<Key-Right>',right)
# app.bind('<KeyRelease-Right>',reset)
app.bind('<Key-c>',down)
# app.bind('<KeyRelease-c>',reset)
app.bind('<Key-e>',upward)
# app.bind('<KeyRelease-e>',reset)
app.bind('<Return>', reset)




ele = Text(app, width=65, height = 5 ,borderwidth=5)
ele.place(relwidth=0.42 , relheight=0.25 , relx=0.54, rely = 0.63)
ele.insert(INSERT, result)
app.mainloop()

