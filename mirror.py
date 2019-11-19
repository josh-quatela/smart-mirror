import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time

Sensor1 = 23
Sensor2 = 24
Sensor3 = 25
Sensor4 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(Sensor1, GPIO.IN)
GPIO.setup(Sensor2, GPIO.IN)
GPIO.setup(Sensor3, GPIO.IN)
GPIO.setup(Sensor4, GPIO.IN)
var = True

try:
    time.sleep(2)

    while var:
        if GPIO.input(23):
            print("Display 1")
        elif GPIO.input(24):
            print("Display 2")
        elif GPIO.input(25):
            print("Display 3")
        elif GPIO.input(12):
            print("Screen off")
except:
    GPIO.cleanup()
        
