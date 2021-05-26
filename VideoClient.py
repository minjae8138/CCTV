# ���ϸ� : VideoClient1.py
import io
import socket
import struct
import time
import picamera
# ������ ����
client_socket = socket.socket()
client_socket.connect('192.168.0.62', 5000)
# ���ῡ�� ���ϰ� ���� ��ü �����
connection = client_socket.makefile('wb')
try:
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(2)
    start = time.time()
    stream = io.BytesIO()

    for foo in camera.capture_continuous(stream, 'jpeg'):
        # �̹����� ���̸� ��Ʈ���� ����, �÷���(���� ����)
        connection.write(struct.pack('<L', stream.tell()))
        connection.flush()
        # ��Ʈ���� �ǰ���, �̹����� ����
        stream.seek(0)
        connection.write(stream.read())
        # �������� 30�ʰ� �����ٸ� ����
        if time.time() - start > 30: break
        # ���� ĸó�� ���� ��Ʈ���� ����
        stream.seek(0)
        stream.truncate()
    # �޽����� ���� �˸��� ���� 0 ���� ���
    connection.write(struct.pack('<L', 0))

finally:
    connection.close()
    client_socket.close()