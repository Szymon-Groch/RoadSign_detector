from ultralytics import YOLO
import cv2
import math


model = YOLO("znaki.pt")


video_sciezka = input("Podaj scieżke lub nazwę pliku (jeżeli jest w tym samym folderze) mp4: ")
kamerka = cv2.VideoCapture(video_sciezka)

znaki = ['agatka','autostrada','ograniczenie_predkosci','parking','pierszenstwo','prosto','przejscie_pieszych','stop','ustap'] 

#każda klatka
while True:
    ret, klatka = kamerka.read()

    if ret:
        wyniki = model.track(klatka, persist=True)

        # przetwarzanie wykrytych obiektów
        for r in wyniki:
            ramki = r.boxes

            for ramka in ramki:
                # współrzedne ramek
                x1, y1, x2, y2 = ramka.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # rysowanie ramke otaczająca
                cv2.rectangle(klatka, (x1, y1), (x2, y2), (255, 255, 0), 3)

                # pewność detekcji
                confidence = math.ceil((ramka.conf[0] * 100)) / 100

                # nazwa klasy wykrytego obiektu, tj. nazwa wykrytego znaku
                znak = int(ramka.cls[0])
                nazwa_znaku = znaki[znak]

                # wyświetlanie wykrytego znaku i pewność identyfikacji
                org = (x1, y1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2
                detection = f"{nazwa_znaku} {confidence}"
                cv2.putText(klatka, detection, org, font, fontScale, color, thickness)

        # klatka z wykrytym znakiem
        cv2.imshow('Wideo', klatka)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

kamerka.release()
cv2.destroyAllWindows()