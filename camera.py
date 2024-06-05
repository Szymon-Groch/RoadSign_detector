from ultralytics import YOLO
import cv2
import math 

# wybór kamerki i rozdzielczości przechwytywanego obrazu
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


model = YOLO("znaki.pt")


znaki = ['agatka','autostrada','ograniczenie_predkosci','parking','pierszenstwo','prosto','przejscie_pieszych','stop','ustap'] 


while True:
    success, img = cap.read()
    wyniki = model(img, stream=True)


    for r in wyniki:
        ramki = r.boxes

        for ramka in ramki:
            # definowanie oznaczającej ramki 
            x1, y1, x2, y2 = ramka.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) 

            # umieszczenie ramki w obrazie z kamery
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 3)

            # pewność identyfikacji znaku
            confidence = math.ceil((ramka.conf[0]*100))/100
            print("Confidence --->",confidence)

            # nazwa znaku
            znak = int(ramka.cls[0])
            print("Nazwa znaku -->", znaki[znak])

            
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            
            color = (255, 0, 0)
            thickness = 2
            detection = znaki[znak] + " " + str(confidence)
            cv2.putText(img, detection, org, font, fontScale, color, thickness)

    cv2.imshow('Kamerka', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()