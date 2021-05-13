from threading import Thread
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED = 26
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

class Pir(Thread):
    def __init__(self,client,value):
        super().__init__()
        self.value = ""
        self.client = client

    def run(self):
        while True:
            GPIO.setmode(GPIO.BCM)
            pirPin = 17
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


            #self.client.publish("iot/pir", self.value)
            #self.client.loop(2)
