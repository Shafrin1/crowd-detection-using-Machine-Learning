import cv2
import numpy as np

# Load the face cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capture the video from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture the current frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Count the number of faces detected
    face_count = len(faces)
    print("face_count:",face_count)
    if face_count>=1:
        print("crowd detected")
    else:
        print("no Crowd")

    # Draw a rectangle around each face detected
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the frame with the detected faces
    cv2.imshow('Face Detection', frame)

    # Quit if the user presses `q`
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()

# Close all windows
cv2.destroyAllWindows()
