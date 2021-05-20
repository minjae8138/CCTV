import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

from pir import Pir
import RPi.GPIO as GPIO
import Camera


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
#     print("메세지도착 " + str(myval))
#     if str(myval) == 'videostreaming':
# <<<<<<< HEAD
# =======
#         # 이미지 파일 전송
# >>>>>>> 8215553bf873d8797daddb49c81e07f094780de0
#         f = open("/home/pi/Pictures/cam.jpg", "rb")
#         imagebin = f.read()
#         byteArray = bytearray(imagebin)
#         mqttClient.publish("mydata/whoareyou/getimage", byteArray, 0)
#         # 비디오스트리밍 시작


mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("ec2-52-78-81-16.ap-northeast-2.compute.amazonaws.com", 1883, 60)


camera = Camera.Camera()

pir = Pir(camera)
pir.start()


#ard = ArduinoSensorUART.Arduino(mqttClient, "")
#ard.start()

mqttClient.loop_forever()


