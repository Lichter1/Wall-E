
import cv2

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def getImg(display= False,size=[720,480]):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
      cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    if display:
        cv2.imshow('IMG',img)
        key = cv2.waitKey(1)
    return img

if __name__ == '__main__':
    while True:
        img = getImg(True)