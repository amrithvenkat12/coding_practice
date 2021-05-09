import cv2
from random import randrange


#load trained faces
trained_face_data =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
'''
#detect from img.
img = cv2.imread('1.jpg')

#convert to grayscale
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

print(face_coordinates)

for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),10)

#show img
cv2.imshow('Detector',img)
cv2.waitKey()

'''
#webcam capture can give videos too
webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read,frame = webcam.read()


    #convert to grayscale
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),10)
    
    #show img
    cv2.imshow('Detector',frame)
    key=cv2.waitKey(1)

    if key==81 or key==113:
        break

webcam.release()

print("completed succesfully yes")
