import cv2
import mediapipe as mp
import threading
import time
from codrone_edu.drone import Drone

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize CoDrone EDU
drone = Drone()
drone.pair()
# Open Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

# Drone control function
def control_drone(command):
    if command == "HOVER":
        drone.hover(1)
    elif command == "TAKEOFF":
        drone.takeoff()
    elif command == "LAND":
        drone.land()
    elif command == "MOVE RIGHT":
        drone.set_roll(10)  # Move right
    elif command == "MOVE LEFT":
        drone.set_roll(-10)  # Move left
    time.sleep(0.3)  # Short delay to avoid rapid commands

# Gesture Control Loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for selfie mode
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    command = "UNKNOWN"

    if result.multi_hand_landmarks:
        for landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Get coordinates
            finger_tips = [landmarks.landmark[i].y for i in [8, 12, 16, 20]]
            wrist_x = landmarks.landmark[0].x
            index_base_x = landmarks.landmark[5].x

            # Gesture recognition
            if all(y < landmarks.landmark[6].y for y in finger_tips):  
                command = "HOVER"
            elif landmarks.landmark[8].y < landmarks.landmark[6].y and all(y > landmarks.landmark[6].y for y in finger_tips[1:]):  
                command = "TAKEOFF"
            elif all(y > landmarks.landmark[6].y for y in finger_tips):  
                command = "LAND"
            elif wrist_x > index_base_x + 0.05:  # Hand rotated right
                command = "MOVE RIGHT"
            elif wrist_x < index_base_x - 0.05:  # Hand rotated left
                command = "MOVE LEFT"

            # Run drone commands in a separate thread
            threading.Thread(target=control_drone, args=(command,)).start()

            # Display command on frame
            cv2.putText(frame, command, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Drone Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
drone.land()
drone.close()
