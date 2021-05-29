from picamera import PiCamera
from time import sleep
import datetime


class Camera():
    def __init__(self):
        # 파일로 저장하기

        super().__init__()
        self.camera = PiCamera()
        # 사진을 180도 회전해서 출력한다.
        self.camera.rotation = 180
        self.camera.start_preview()
        sleep(1)

    def takepicture(self):
        now = datetime.datetime.now()
        filename = '/home/pi/Pictures/%s.jpg' % now
        self.camera.capture(filename)
        return filename

    def stop(self):
        self.camera.stop_preview() # 미리보기 화면 정지

