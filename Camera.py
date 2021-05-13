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
        sleep(2)

    def takepicture(self):
        now = datetime.datetime.now()
        sleep(2)
        filename = '/home/pi/whoareyou/images/%s.jpg' % now
        print(filename + "사진이 생성되었습니다.")
        self.camera.capture(filename)
        return filename

    def stop(self):
        self.camera.stop_preview() # 미리보기 화면 정지

