import cv2
from goprocam import GoProCamera, constants
from time import time
import socket

gpCam = GoProCamera.GoPro()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
t = timw()

gpCam.livestream("start")

# Set resolution and FPS of the camera
goCam.gpControlsSet(constants.Stream.WINDOW_SIZE, constants.Stream.WindowSize.R720)

# capture via UDP address

cap = cv2.VideoCapture("udp://10.5.5.9:8554", cv2.CAP_FFMPEG)

while True:
    nmat, frame = cap.read()
    cv2.imshow("GoPro OpenCV", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if time() - t >= 2.5:
        sock.sendto("_GPHD_:0:0:2:0.000000\n".encode(), ("10.5.5.9", 8554))
        t = time()

cap.release()
cv2.destroyAllWindow()

