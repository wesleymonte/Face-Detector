import cv2
import argparse
from modules.facedetector import FaceDetector
from modules import resolution

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", default=".\\haarcascade_frontalface.xml",
                help="Path to where the face cascade resides")
ap.add_argument("-v", "--video",
                help="Path to the (optional) video")
ap.add_argument("-r", "--record",
                help="The video file name of the (optional) recording")
ap.add_argument("-re", "--resolution", default="720p",
                help="Video Resolution")
args = vars(ap.parse_args())

camArg = 0
if args["video"] is not None:
    camArg = args["video"]

cam = cv2.VideoCapture(camArg)
resolution.change_res(cam, args["resolution"])
fc = FaceDetector(args["face"])
out = None

if args["record"] is not None:
    out = cv2.VideoWriter(args["record"], 0x7634706d, 24.0, resolution.STD_DIMENSIONS[args["resolution"]])

while True:
    (grabbed, frame) = cam.read()

    if args.get("Video") and not grabbed:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = fc.detect(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if out is not None:
        out.write(frame)

    cv2.imshow("Cam", frame)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break