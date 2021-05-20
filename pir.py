from threading import Thread
import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish

GPIO.setmode(GPIO.BCM)
LED = 21
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

class Pir(Thread):
    def __init__(self,camera):
        super().__init__()
        self.value = ""
        self.filename = None
        self.camera = camera
        

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
                # 사진촬영
                self.filename = self.camera.takepicture()
                # 사진저장
                # 사진전송
                f = open(self.filename, "rb")
                imagebin = f.read()
                byteArray = bytearray(imagebin)
                publish.single("mydata/whoareyou/getimage", byteArray, hostname="ec2-52-78-81-16.ap-northeast-2.compute.amazonaws.com")

            else:
                self.value = 'off'
                GPIO.output(LED, GPIO.LOW)
                print("off")


            #self.client.publish("iot/pir", self.value)
            #self.client.loop(2)
