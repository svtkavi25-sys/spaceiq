import cv2

def detect_people():

    cap = cv2.VideoCapture(0)

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    people_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        boxes, weights = hog.detectMultiScale(frame)

        people_count = len(boxes)

        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.putText(frame, f'People Count: {people_count}',
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2)

        cv2.imshow("SPACEIQ Camera", frame)

        # Press Q to close camera
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return people_count