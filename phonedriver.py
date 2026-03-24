import cv2
from flask import Flask, Response

app = Flask(__name__)

# DroidCam stream
cam = cv2.VideoCapture("http://10.221.42.119:4747/mjpegfeed")

def generate():
    while True:
        success, frame = cam.read()
        if not success:
            break
        
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video')
def video():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def home():
    return "Server is running ✅"

app.run(host='0.0.0.0', port=4747)