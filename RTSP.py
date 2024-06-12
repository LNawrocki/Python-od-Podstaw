import cv2
import cv2.data

video = cv2.VideoCapture("rtsp://user:haslo@ip:554/cam/realmonitor?channel=28&subtype=1")

while True:
    success, frame = video.read()

    gray_image = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("RTSP", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyWindow()
