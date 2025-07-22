import cv2
import mediapipe as mp
import requests
import time
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

def is_open_hand(landmarks):
    """Check if all fingers are extended (open palm)"""
    tips = [landmarks[4], landmarks[8], landmarks[12], landmarks[16], landmarks[20]]
    return all(tip.y < landmarks[0].y - 0.03 for tip in tips)  # 0.03 sensitivity adjustment

cap = cv2.VideoCapture(0)
last_action_time = 0
COOLDOWN = 1.0  # seconds

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark
            mp.solutions.drawing_utils.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Thumb-Index distance
            thumb = landmarks[4]
            index = landmarks[8]
            distance = math.sqrt((thumb.x - index.x)**2 + (thumb.y - index.y)**2)

            current_time = time.time()
            if current_time - last_action_time > COOLDOWN:
                # Pinch gesture (calculate)
                if distance < 0.05:
                    requests.post("http://localhost:5000/calculate", 
                                data={"expression": "1+1"})
                    cv2.putText(frame, "CALCULATED: 2", (50, 50), 
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    last_action_time = current_time

                # Open hand (reset)
                elif is_open_hand(landmarks):
                    requests.post("http://localhost:5000/calculate",
                                data={"expression": "0"})
                    cv2.putText(frame, "RESET: 0", (50, 50),
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    last_action_time = current_time

    cv2.imshow('Gesture Control (Press Q to quit)', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()