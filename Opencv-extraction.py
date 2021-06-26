import cv2
cap=cv2.VideoCapture(0)
cap.set(3,1000)#length
cap.set(4,1000)#breadth
cap.set(10,100)#brightness
start_point=(0,300)
end_point=(300,600)
color=(0,0,255)
thickness=5
while True:
    success,image=cap.read()
    image = image[300:600,0:300]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (200, 200))
    image = cv2.threshold(image, 0, 255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #        cv2.THRESH_BINARY,11,2)
    #blur = cv2.GaussianBlur(image,(5,5),0)
    #ret3,image = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #image=cv2.rectangle(image, start_point, end_point, color, thickness)
    cv2.imshow("video",image)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break