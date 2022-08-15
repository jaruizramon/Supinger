import RPi.GPIO as GPIO
from time import sleep

print("Starting PIR Module")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
sleep(2)

print('Ready')

while True:
    if GPIO.input(17) or GPIO.input(18):
        
        print("Sensor B has detected some motion...")
        sleep(0.5)
