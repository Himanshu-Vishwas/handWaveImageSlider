import cv2 as cv
import pyautogui as p
import time as t
from cvzone.HandTrackingModule import HandDetector


detector = HandDetector(detectionCon=0.8, maxHands=1)

video = cv.VideoCapture(0)
history = ["himanshu",int(t.time())]


#welcome
print("\n\n\tHAND WAVE SLIDER\n\twave your hand right or left in front of camera to press \"right\" or \"left\".\n")

#final output code
def final(loc,tdif):
    if loc != history[0]:
                if tdif <=0.04 and tdif>=0.0003:
                    if history[0] != "himanshu":
                        print(history[0],"to",loc)
                        p.press(loc)
                    history[0] = loc
                    history[1] = tdif


while True:
    ret,frame = video.read()
    hands,img = detector.findHands(frame)
    cv.imshow("Frame",frame)


    if hands:
        hand1 = hands[0]
        xcor = hand1["center"][0]
        t_his = t.time()/0.01

        history[1] = t_his
        
        if xcor<=250:
            pos = "left"
            t_dif = (t.time()/0.01)- t_his
            final(pos,t_dif)


        elif xcor>250:
            pos="right"
            t_dif = (t.time()/0.01)- t_his
            final(pos,t_dif)
            
            
        else:
            continue

    if not hands:
        history[0] = "himanshu"


#to close
    key = cv.waitKey(1)
    if key == ord('x'):
        break

video.release()
cv.destroyAllWindows()