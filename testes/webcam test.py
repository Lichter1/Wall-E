
import cv2

cap = cv2.VideoCapture(0)

if __name__ == '__main__':
    while True:
        _, img = cap.read()
        size=[640,480]
        img = cv2.resize(img,(size[0],size[1]))
        cv2.imshow('IMG',img)
        key = cv2.waitKey(1)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()
#
    #while True:
   #    img = getImg(True)