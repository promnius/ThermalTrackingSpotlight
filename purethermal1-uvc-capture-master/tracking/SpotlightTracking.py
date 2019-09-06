
import time
import cv2
import numpy as np
import imutils

def findHotObjects(img,thermalCuttoff):
    imgBlurred = cv2.GaussianBlur(img,(9,9),cv2.BORDER_DEFAULT)
    imgBlurredF = (((imgBlurred-27315).astype(float)*(1.8/100))+32)     
    ret,imgThreshold = cv2.threshold(imgBlurredF.astype(np.uint8),thermalCuttoff,255,cv2.THRESH_BINARY) # cuttoff at 82F
    return imgThreshold

def findTargetCoordinates(img): #(img, detector):
    imgBorder = cv2.copyMakeBorder(img,top=5,bottom=5,left=5,right=5,borderType=cv2.BORDER_CONSTANT, value=(0,0,0))
    #keypoints = detector.detect(imgBorder)
    #im_with_keypoints = cv2.drawKeypoints(imgBorder,keypoints,np.array([]),(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    #return im_with_keypoints
    contours, heirarchy = cv2.findContours(imgBorder.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    maxSize = 0
    for contour in contours:
        if cv2.contourArea(contour) > maxSize:
            maxSize = cv2.contourArea(contour)
    largeContours = []
    for contour in contours:
        if cv2.contourArea(contour) > maxSize/5:
            largeContours.append(contour)
    #cv2.drawContours(imgBorder, largeContours, -1, (0,255,0), 2)
    imgColor = cv2.cvtColor(imgBorder, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(imgColor, largeContours, -1, (0,255,0), 2)
    centerX = len(imgColor)/2
    centerY = len(imgColor[0])/2
    distances = []
    for contour in contours:
        M = cv2.moments
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m10"]/M["m00"])
        dist = math.sqrt( ((cX-centerX)**2)+((cY-centerY)**2) )
        distances.append(dist)
    if len(distances)>0:
        targetContour = contours[distances.index(min(distances))]
        cv2.drawContours(imgColor, [targetContour], -1 (0,0,255), 2)
    else:
        print("No Target Found")
            
    return imgColor
        
