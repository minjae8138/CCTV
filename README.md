# CCTV

### 구현부분(라즈베리파이 서버)
- YOLOv5 모델을 통해서 카메라에 찍힌 사진에서 정해둔 물체를 탐지해서 라벨값 추출
- Face_recognition을 통해 DB에 등록된 사람인지 아닌지 판별하여 family, known, unknown으로 구분하여 추출
- 위에 추출한 값을 바탕으로 위험도 등급을 도출하여 EC2로 보낸다(MQTT통신)
