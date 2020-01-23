from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import time
import sys
import imutils
import cv2 #v4.1.2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str,
        help="path to imput video file")
args = vars(ap.parse_args())



tracker = cv2.TrackerKCF_create()
initBB = None

vs = cv2.VideoCapture(args["video"])
#vs = cv2.VideoCapture("./tdata/test.mp4")


ok, frame = vs.read()
    #frame = frame[1] if args.get("video", False) else frame
if not ok:
     print("cant read file")
     sys.exit()

bbox = (50,50,40,100)

bbox = cv2.selectROI(frame, False)

ok = tracker.init(frame, bbox)
mem = []
f = 0 
while True:
    
    ok, frame = vs.read()
    if not ok:
        break

    timer = cv2.getTickCount()

    ok, bbox = tracker.update(frame)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() -timer)

    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        #print(frame)
        cv2.rectangle(frame,p1,p2, (255,0,0), 2, 1)
    else:
        cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)


    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Tracking",frame)
    k = cv2.waitKey(1)
    f += 1
    mem.append(frame)
    print(f)
    print(np.shape(mem))
    while k not in [27, ord('k'), ord('j')]:
        k = cv2.waitKey(0)
    
    if k == ord('j'):
        fref = f
        f -= 1
        print(str(f)+"t")
        while f <= fref:

            cv2.imshow("Tracking", mem[f])
            k = cv2.waitKey(1)
            while k not in [27, ord('k'), ord('j')]:
                k = cv2.waitKey(0)

            if k == 27:
                break

            if k == ord('k'):
                f += 1

            if k == ord('j'):
                f -= 1

            if f == 0:
                break

    if k == 27:
        break



    if frame is None:
        break
    
    #frame = imutils.resize(frame, width = 500)
    #(H, W) = np.ndim(frame)[:2]

    ###############
    #stuff missing#
    ###############

    #cv2.imshow("Frame", frame)
    #key = cv2.waitKey(1) & 0xFF





