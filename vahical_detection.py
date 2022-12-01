import cv2
import imutils
alg ="cars.xml"
car_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)

while True:
    detected =0
    _, img = cam.read()
    img = imutils.resize(img,width=300)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(grayImg,1.1,1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255),2)
    cv2.imshow("VahicalDetection", img)
    b = str(len(cars))
    a = int(b)
    detected = a
    n = detected
    print("---------------------------------")
    print("North: %d"%(n))
    if n>2:
        print("north more Trsffic")
    else:
        print("no traffic")    


    key = cv2.waitKey(10) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
