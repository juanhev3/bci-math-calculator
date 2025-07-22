import cv2
import numpy as np
import requests

# Initialize camera
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        # Draw face rectangle
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
        # Detect head position
        face_center = x + w//2
        screen_center = frame.shape[1] // 2
        
        # Send commands based on head position
        if face_center < screen_center - 100:  # Left
            requests.post("http://localhost:5000/calculate", data={"expression": "1+1"})
            cv2.putText(frame, "LEFT: 1+1", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        elif face_center > screen_center + 100:  # Right
            requests.post("http://localhost:5000/calculate", data={"expression": "2+2"})
            cv2.putText(frame, "RIGHT: 2+2", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    
    cv2.imshow('Head Control', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()