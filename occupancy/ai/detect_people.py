import cv2
import math
import time

def detect_people():

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(0)

    tracked_faces = []
    total_people = 0

    DISTANCE_THRESHOLD = 70

    start_time = time.time()

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.resize(frame, (900,650))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.05,
            minNeighbors=3,
            minSize=(20,20)
        )

        current_centers = []

        for (x,y,w,h) in faces:

            cx = x + w//2
            cy = y + h//2

            current_centers.append((cx,cy))

            # draw face box
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

        # show count on camera
        cv2.putText(
            frame,
            f"People Count: {total_people}",
            (20,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        cv2.imshow("SPACEIQ Detection", frame)

        key = cv2.waitKey(1) & 0xFF

        # press Q to stop
        if key == ord('q') or key == ord('Q'):
            break

        # auto stop after 10 seconds
        if time.time() - start_time > 10:
            break

    cap.release()
    cv2.destroyAllWindows()

    return total_people