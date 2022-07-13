import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BCM)
soundpin = 17
led = 27
check_on = 0
GPIO.setwarnings(False)
GPIO.setup(soundpin, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)

try: 
   while True:
      if GPIO.input(soundpin):
         check_on += 1
         print ("sound 1")
         sleep(1)
         if(check_on == 3):
            print ("sound 3")
            GPIO.output(led, GPIO.HIGH)
            sleep(1)
            check_on = 0
      else:
         GPIO.output(led, GPIO.LOW)

finally:
   GPIO.cleanup()