# 파일명 : VideoClient1.py
import io
import socket
import struct
import time
import picamera
# 서버에 연결
client_socket = socket.socket()
client_socket.connect('192.168.0.62', 5000)
# 연결에서 파일과 같은 객체 만들기
connection = client_socket.makefile('wb')
try:
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(2)
    start = time.time()
    stream = io.BytesIO()

    for foo in camera.capture_continuous(stream, 'jpeg'):
        # 이미지의 길이를 스트림에 쓰고, 플러시(실제 전송)
        connection.write(struct.pack('<L', stream.tell()))
        connection.flush()
        # 스트림을 되감고, 이미지를 전송
        stream.seek(0)
        connection.write(stream.read())
        # 시작한지 30초가 지났다면 종료
        if time.time() - start > 30: break
        # 다음 캡처를 위해 스트림을 리셋
        stream.seek(0)
        stream.truncate()
    # 메시지의 끝을 알리는 길이 0 값을 기록
    connection.write(struct.pack('<L', 0))

finally:
    connection.close()
    client_socket.close()