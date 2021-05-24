# coding=utf-8
# 파일명 : VideoServer.py
import cv2
import numpy as np
import net
import json


HOST = '192.168.0.62'
PORT = 5000

def receiver(client, addr):
    reader = client.makefile('rb')
    writer = client.makefile('wb')
    while True:
        data, data_len = net.receive(reader)
        if not data:
            break

        print('received ', data)
        data = np.frombuffer(data, dtype=np.uint8)
        image = cv2.imdecode(data, cv2.IMREAD_COLOR)
        cv2.imshow('frame', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        result = json.dumps({'result': 'ok'})
        net.send(writer, result.encode())

    print('exit receiver')


if __name__ == '__main__':
    print('start server...')

    net.server(HOST, PORT, receiver)
