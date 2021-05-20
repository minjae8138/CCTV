import serial
from threading import Thread
import time
import RPi.GPIO as GPIO

ser = serial.Serial('/dev/ttyAMA1', 9600, timeout=1);



class Arduino(Thread) :
    def __init__(self, client, value):
        super().__init__()
        self.value = ""
        self.client = client

    def run(self):
        while True:
            cStr = "";
            rLine = ser.readline();

            if rLine is not None :
                for i in range(len(rLine)):
                    if i > 2 :
                        continue;
                    cStr += chr(rLine[i]);

                print("2 %s" % cStr);
            else :
                print("error")

            self.value = '2 ' + cStr
            self.client.publish("iot/ARD", self.value)













