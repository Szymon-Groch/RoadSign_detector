from ultralytics import YOLO
import cv2
import math

# Choosing the camera and setting the resolution of the captured image
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

model = YOLO("znaki.pt")

signs = ['agatka', 'autostrada', 'speed_limit', 'parking', 'priority', 'straight', 'pedestrian_crossing', 'stop', 'yield'] 

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes

        for box in boxes:
            # Defining bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Placing bounding box on the camera image
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 3)

            # Confidence of sign identification
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # Sign name
            sign = int(box.cls[0])
            print("Sign name -->", signs[sign])

            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            detection = signs[sign] + " " + str(confidence)
            cv2.putText(img, detection, tuple(org), font, fontScale, color, thickness)

    cv2.imshow('Camera', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
