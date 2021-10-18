import cv2 #imported in this file to count the fingers
import os  #imported in this file to interact through the webcam
import time #to calculate time related operations
import handTrackingModule as htm #to acces the handTrackingModule
def getNumber(ar): #fxn to determine the no from the array
    s=""
    for i in ar:
       s+=str(ar[i]);
       
    if(s=="00000"):
        return (0)   #the number is 0
    elif(s=="01000"):
        return(1)    #the number is 1
    elif(s=="01100"):
        return(2)    #the number is 2
    elif(s=="01110"):
        return(3)    #the number is 3
    elif(s=="01111"):
        return(4)    #the number is 4
    elif(s=="11111"):
        return(5)    #the number is 5
     
 
wcam,hcam=640,480 #height and width of the image
cap=cv2.VideoCapture(0) #to return webcam from the computer
cap.set(4,wcam) #dimensions for width
cap.set(4,hcam) #dimensions for height
pTime=0
detector = htm.handDetector(detectionCon=0.75)
while True:
    success,img=cap.read()
    img = detector.findHands(img, draw=True )
    lmList=detector.findPosition(img,draw=False)
    #print(lmList)
    tipId=[4,8,12,16,20]
    if(len(lmList)!=0):
        fingers=[]
        #thumb
        if(lmList[tipId[0]][1]>lmList[tipId[0]-1][1]):
                fingers.append(1) #thumb is open
        else :
                fingers.append(0) #thumb is closed
        #4 fingers
        for id in range(1,len(tipId)):
            
            if(lmList[tipId[id]][2]<lmList[tipId[id]-2][2]):
                fingers.append(1) #finger is open
            
            else :
                fingers.append(0) #finger is closed
        
           
        cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)   
        cv2.putText(img,str(getNumber(fingers)),(45,375),cv2.FONT_HERSHEY_PLAIN,
                                     10,(255,0,0),20)  
        
     
    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, f'FPS: {int(fps)}',(400,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),3)
    cv2.imshow("image",img)
    if(cv2.waitKey(1) & 0xFF== ord('q')):
        break


