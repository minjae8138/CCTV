from flask import Flask, render_template, request, Response
import MyCamera

app = Flask(__name__)


def show(camera):
    while True:
        frame = camera.getStreaming()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/show")
def showVideo():
    return Response(show(MyCamera.MyCamera()), mimetype="multipart/x-mixed-replace;boundary=frame")


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True, threaded=True)

    except KeyboardInterrupt:
        print("종료")

