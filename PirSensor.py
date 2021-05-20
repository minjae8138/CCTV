from threading import Thread
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LED = 21
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

class Pir(Thread):
    motion_detected = False
    def __init__(self):
        super().__init__()
        self.value = ""

    def run(self):
        while True:
            GPIO.setmode(GPIO.BCM)
            pirPin = 26
            GPIO.setup(pirPin, GPIO.IN)
            time.sleep(2)
            if GPIO.input(pirPin) == 1:
                self.value = 'motion detect'
                GPIO.output(LED, GPIO.HIGH)
                print("on")
            else:
                self.value = 'off'
                GPIO.output(LED, GPIO.LOW)
                print("off")

