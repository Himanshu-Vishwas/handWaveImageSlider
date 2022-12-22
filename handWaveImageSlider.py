import cv2 as cv
import pyautogui as p
import time as t
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)

video = cv.VideoCapture(0)
loc_his = ["himanshu",int(t.time())]
#main_time = t.time()/0.01
while True:
    #loc_his ="himanshu"
    ret,frame = video.read()
    hands,img = detector.findHands(frame)
    cv.imshow("Frame",frame)
    # loc_his ="himanshu"
    if hands:
        hand1 = hands[0]

        xcor = hand1["center"][0]
        #loc_his ="himanshu"
        t_his = t.time()/0.01
        loc_his[1] = t_his
        if xcor<=250:
            loc = "left"
            t_dif = (t.time()/0.01)- t_his
            if loc != loc_his[0]:
                if t_dif <=2 and t_dif>=0.0003:
                    print("l2r",t_dif)
                    p.press("right")
                    loc_his[0] = loc
                    loc_his[1] = t_his
            else:
                if t_dif >2:
                    print("r2l2",t_dif)
                    p.press("left")
                    loc_his[0] = loc
                    loc_his[1] = t_his
        elif xcor>250:
            loc="right"
            t_dif = (t.time()/0.01)- t_his
            if loc != loc_his[0]:
                if t_dif <=2 and t_dif>=0.0003:
                    print("r2l",t_dif)
                    p.press("left")
                    loc_his[0] = loc
                    loc_his[1] = t_his
            else:
                if t_dif >2:
                    print("l2r2",t_dif)
                    p.press("right")
                    loc_his[0] = loc
                    loc_his[1] = t_his
        else:
            continue
        #print(xcor,loc,loc_his)
    key = cv.waitKey(1)
    if key == ord('x'):
        break
video.release()
cv.destroyAllWindows()