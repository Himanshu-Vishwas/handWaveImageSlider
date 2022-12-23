import cv2 as cv
import pyautogui as p
import time as t
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)

video = cv.VideoCapture(0)
his = ["himanshu",t.time()]
#print("level1")
commands=["a","a"]
cd_time = [0,0]
while True:
    #print("while")
    #prev_command = [commands,his[1]]
    ret,frame = video.read()
    hands,img = detector.findHands(frame)
    cv.imshow("Frame",frame)
    if hands:
        #print("ifhands")
        hand1 = hands[0]
        xcor = hand1["center"][0]
        t_dif = t.time() - his[1]
        if t_dif >=2:
            his[0] ="himanshu"
        his[1] = t.time()
        if xcor<=250:
            pos = "left"
            #print("pos",his[0],t_dif)
            if pos != his[0] and t_dif<=0.05:
                print("l2r",t_dif)
                commands[1] = "lll"
                cd_time[0] = t.time()
                his[0] = pos
                his[1] = t.time()
            elif pos == his[0] and t_dif>0.1:
                print("left as is",t_dif)
                his[1] = t.time()
                commands[0] = "lll"
                cd_time[0] = t.time()
        elif xcor>250:
            #print("pos2")
            pos = "right"
            if pos != his[0] and t_dif<=0.05:
                print("r2l",t_dif)
                commands[1] = "rrr"
                cd_time[0] = t.time()
                his[0] = pos
                his[1] = t.time()
            elif pos == his[0] and t_dif>0.1:
                print("right as is",t_dif)
                his[1] = t.time()
                
                commands[0] = "rrr"
                cd_time[0] = t.time()
            if commands[0] != commands[1]:
                # cd_dif = abs(cd_time[0] - cd_time[1])
                # print(cd_dif)
                # if cd_dif>=0.04 and cd_dif<1:
                #print(t_dif)
                if t_dif>=0.04:
                    #print(commands)
                    commands=["a","a"]
        else:
            continue
                

    key = cv.waitKey(1)
    if key == ord('x'):
        break
video.release()
cv.destroyAllWindows()