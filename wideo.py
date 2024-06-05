from ultralytics import YOLO
import cv2
import math

model = YOLO("znaki.pt")

video_path = input("Enter the path or filename (if in the same folder) of the mp4 file: ")
camera = cv2.VideoCapture(video_path)

znaki = ['agatka', 'autostrada', 'ograniczenie_predkosci', 'parking', 'pierszenstwo', 'prosto', 'przejscie_pieszych', 'stop', 'ustap']

# Each frame
while True:
    ret, frame = camera.read()

    if ret:
        results = model.track(frame, persist=True)

        # Processing detected objects
        for r in results:
            boxes = r.boxes

            for box in boxes:
                # Coordinates of the boxes
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # Drawing the bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 3)

                # Detection confidence
                confidence = math.ceil((box.conf[0] * 100)) / 100

                # Class name of the detected object, i.e., the name of the detected sign
                sign = int(box.cls[0])
                sign_name = znaki[sign]

                # Displaying the detected sign and confidence level
                org = (x1, y1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2
                detection = f"{sign_name} {confidence}"
                cv2.putText(frame, detection, org, font, fontScale, color, thickness)

        # Frame with detected signs
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
