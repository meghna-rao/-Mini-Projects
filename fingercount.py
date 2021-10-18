import cv2 
import time
import os
import handTrackingModule as htm

wCam , hCam = 640,480 #height and width of the camera

cap = cv2.VideoCapture(0) 
cap.set(3, wCam) #Creating the dimensions for the webcam
cap.set(4, hCam)

#folderpath = "fingerimages" #direct towards the image folder fingerimages
#myList = os.listdir(folderpath)
#print(folderpath)



detector = htm.handDetector(detectionCon=0.75)

tipIds =[4,8,12,16,20] #These are the numbers given to the top most joints in the hand

while True : #Creating a loop to iterate through each finger in a hand
    
    
    
    success, img = cap.read()
    img = detector.findHands(img)  #calling the handtrackingModule to detect and identify the image
    lmList = detector.findPosition(img,draw = False) #here draw is kept false, to prevent a compressed image of the figure to be shown .
    
    #print(lmList)
    
    #FOR THE THUMB
    
    if len(lmList) != 0:
        fingers = []
        
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1) #FINGER IS RAISED
        else:
            fingers.append(0) #IT MEANS THAT THE FINGER IS NOT RAISED
            
            #FOR FOUR FINGERS
    
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
              
        totalFingers = fingers.count(1)
        print(totalFingers)
        
        
              
        
       
       
       #Making a green box which generates the number based on the finger
       
        cv2.rectangle(img,(20,225),(170,425),(0,255,0),cv2.FILLED)
        cv2.putText(img, str(totalFingers),(45,375),cv2.FONT_HERSHEY_PLAIN,9,(255,0,0), 25)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    #for FPS
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)
    cv2.imshow("Image",img)
    cv2.waitKey(1) #Creating a delay of 1 milli sec
    
    
