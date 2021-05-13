import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

from pir import Pir
import RPi.GPIO as GPIO
from MyCamera import MyCamera


#import ArduinoSensorUART

pir = None


def show(camera):
    while True:
        frame = camera.getStreaming()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def on_connect(client,usedata,flags,rc):
    global pir
    print("connect.."+str(rc))
    if rc == 0:
        client.subscribe("mydata/whoareyou/request") # mydata/whoareyou - 토픽명
    else:
        print("연결실패")

# 메세지가 도착했을 때 처리할 일들 - 여러가지 장비 제어, Mongodb에 저장
def on_message(client,userdata,msg):
    GPIO.setmode(GPIO.BCM)
    global pir
    myval = msg.payload.decode("utf-8")
    print("메세지도착 " + str(myval))
    if str(myval) == 'videostreaming':
        f = open("/home/pi/whoareyou/cam2.jpg", "rb")
        imagebin = f.read()
        byteArray = bytearray(imagebin)
        mqttClient.publish("mydata/whoareyou/getimage", byteArray, 0)
        # 비디오스트리밍 시작


mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("192.168.0.55", 1883, 60)

pir = Pir(mqttClient, "")
pir.start()

#ard = ArduinoSensorUART.Arduino(mqttClient, "")
#ard.start()

mqttClient.loop_forever()


