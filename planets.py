import cv2

img = cv2.imread("C:/Users/patha/Downloads/PRO-C116-project-image-main-main/PRO-C116-project-image-main-main/solar-system.jpg")

cv2.putText(img, "sun",(100,80), cv2.FONT_HERSHEY_COMPLEX , 0.5, (0,0,255))
cv2.putText(img, "mercury",(110,180), cv2.FONT_HERSHEY_COMPLEX , 0.5, (0,0,255))
cv2.putText(img, "venus",(200,300), cv2.FONT_HERSHEY_COMPLEX , 0.5, (0,0,255))
cv2.putText(img, "earth",(300,300), cv2.FONT_HERSHEY_COMPLEX , 0.5, (0,0,255))
cv2.putText(img, "mars",(400,300), cv2.FONT_HERSHEY_COMPLEX , 0.5, (0,0,255))
cv2.putText(img, "jupiter",(600,300), cv2.FONT_HERSHEY_COMPLEX , 0.5, (0,0,255))
cv2.putText(img, "saturn",(800,300), cv2.FONT_HERSHEY_COMPLEX , 0.5, (0,0,255))
cv2.putText(img, "urans",(1000,300), cv2.FONT_HERSHEY_COMPLEX , 0.5, (0,0,255))
cv2.putText(img, "neptune",(1100,300), cv2.FONT_HERSHEY_COMPLEX , 0.5, (0,0,255))

cv2.imshow("output",img)
cv2.waitKey(0)