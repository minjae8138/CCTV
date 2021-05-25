import paho.mqtt.client as mqtt
import MyCamera
import paho.mqtt.publish as publish


class MyMqtt():
    def __init__(self, topic, value):
        super().__init__()
        client = mqtt.Client()

        client.connect("192.168.0.62", 1883, 60)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("connect.." + str(rc))
        if rc == 0:
            client.subscribe("sensor")
        else:
            print("연결실패")

    def on_message(self, client, userdata, msg):
        myval = msg.payload.decode("utf-8")
        print(myval)
        print(msg.topic + "----" + str(myval))
        camera = MyCamera.MyCamera()
        if myval == "start":
            while True:
                frame = camera.getStreaming()
                publish.single("web", frame, hostname="192.168.0.182")
        else:
            pass



if __name__ == "__main__":
    try:
        mymqtt = MyMqtt("sensor", "test")
        mymqtt.client.on_connect = mymqtt.on_connect
        mymqtt.client.on_message = mymqtt.on_message

    except KeyboardInterrupt:
        print("종료")