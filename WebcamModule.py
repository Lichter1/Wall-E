
import cv2
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

position=90
VB1 = 0
def getImg(display= False,size=[320,240]):
    global position , VB1 , x_medium , y_medium
    center =[size[0]/2 , size[1]/2]
    if VB1 <1:
        x_medium = int(size[0] / 2)
        y_medium = int(size[1] / 2)
        VB1 = VB1 + 1
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        x_medium = int((x+x+w)/2)
        y_medium = int((y+y+h)/2)
    print(position)
    cv2.line(img, (x_medium,0), (x_medium , size[1]), (0,255,0) ,2)
    cv2.line(img, (0,y_medium), (size[0],y_medium), (0, 255, 0), 2)
    if x_medium < center[0] - 40:
        if position <180:
            position += 2
    elif x_medium > center[0] + 40:
        if position >0:
            position -=2
    if display:
        cv2.imshow('IMG',img)
        key = cv2.waitKey(1)
    return img

if __name__ == '__main__':
    while True:
        img = getImg(True)