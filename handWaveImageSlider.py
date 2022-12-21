import cv2 as cv
import pyautogui as p
import time as t
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)

video = cv.VideoCapture(0)

while True:
    #loc_his ="himanshu"
    #main_time = t.time()/0.01
    ret,frame = video.read()
    hands,img = detector.findHands(frame)
    cv.imshow("Frame",frame)
    if hands:
        hand1 = hands[0]
        xcor = hand1["center"][0]
        loc_his ="himanshu"
        t_his = t.time()/0.01
        if xcor<250:
            loc = "left"
            if loc == loc_his:
                continue
            else:
                loc_his = loc
                t_dif = (t.time()/0.01)- t_his
                if t_dif <=2:
                    print("l2r")
                    p.press("right")
        elif xcor>300:
            loc="right"
            if loc == loc_his:
                continue
            else:
                loc_his = loc
                t_dif = (t.time()/0.01)- t_his
                if t_dif <=2:
                    print("r2l")
                    p.press("left")
        else:
            continue
        #print(xcor,loc,loc_his)
    key = cv.waitKey(1)
    if key == ord('x'):
        break
video.release()
cv.destroyAllWindows()