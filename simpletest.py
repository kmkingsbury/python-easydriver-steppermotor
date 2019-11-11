import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)




def StepForwardDefault():
  print("Moving forward at default step mode.");
  GPIO.output(direction, GPIO.LOW) # Pull direction pin low to move "forward"
  for x in range(0, 512):
    #GPIO.output(stp,HIGH); # Trigger one step forward
    GPIO.output(step, GPIO.HIGH)
    time.sleep(delayspeed)
    #GPIO.output(stp,LOW);  # Pull step pin low so it can be triggered again
    GPIO.output(step, GPIO.LOW)


def resetEDPins():
  GPIO.output(step, GPIO.LOW)
  GPIO.output(direction, GPIO.LOW)
  GPIO.output(ms1, GPIO.LOW)
  GPIO.output(ms2, GPIO.LOW)
  GPIO.output(enable, GPIO.HIGH)




step = 6 # Gpio6
direction = 5  # gpio5 
ms1 = 26
ms2 = 13
enable = 19

# 0.01 is fast
delayspeed = 0.05

# setup 
GPIO.setup(step, GPIO.OUT)
GPIO.setup(direction, GPIO.OUT)
GPIO.setup(ms1, GPIO.OUT)
GPIO.setup(ms2, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)

StepForwardDefault()
resetEDPins


