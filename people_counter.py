import cv2
import numpy as np
import math

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

tracked_faces = []
total_people = 0

DISTANCE_THRESHOLD = 60

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Resize for better detection of far people
    frame = cv2.resize(frame, (800,600))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(30,30)
    )

    current_centers = []

    for (x,y,w,h) in faces:

        cx = x + w//2
        cy = y + h//2

        current_centers.append((cx,cy))

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    for center in current_centers:

        matched = False

        for tracked in tracked_faces:

            dist = math.hypot(center[0]-tracked[0], center[1]-tracked[1])

            if dist < DISTANCE_THRESHOLD:
                matched = True
                break

        if not matched:
            tracked_faces.append(center)
            total_people += 1

    cv2.putText(
        frame,
        f"Total People: {total_people}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("SPACEIQ Occupancy Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()