from time import sleep
import RPi.GPIO as GPIO
DIR = 20
STEP = 21
CW = 1
CCW = 0
SPR = 200

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CCW)
if GPIO.input(20):
    print("hi")
else:
    print("low")
step_count = SPR
delay = .0208

for x in range(0,6):
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        delay = delay/2
    
delay = .0208
sleep(.5)
GPIO.output(DIR, 1)
sleep(.5)

for x in range(0,6):
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        delay = delay/2
    
print(delay)
if GPIO.input(20):
    print("hi")
else:
    print("low")
GPIO.cleanup()