Hand Gesture Drone Control

Overview

This project enables controlling a CoDrone EDU drone using hand gestures captured through a webcam. It utilizes OpenCV and MediaPipe for hand tracking and gesture recognition, and sends corresponding commands to the drone.

Requirements

Hardware:

CoDrone EDU

Computer with a webcam

Software:

Python 3.x

OpenCV

MediaPipe

CoDrone EDU Python SDK

Installation

Install required dependencies:

pip install opencv-python mediapipe codrone_edu

Ensure the CoDrone EDU is charged and ready for pairing.

Run the script:

python hand_gesture_drone.py

Gesture Controls

Palm Open (Fingers Extended Upward): HOVER

Index Finger Up, Others Down: TAKEOFF

All Fingers Down: LAND

Tilt Hand Right: MOVE RIGHT

Tilt Hand Left: MOVE LEFT

Usage

Ensure the drone is paired before running the script.

Launch the script to start the webcam-based gesture detection.

Perform gestures to control the drone.

Press 'q' to exit the program.

Troubleshooting

Ensure the webcam is working and properly detecting hand gestures.

Check that the CoDrone EDU is successfully paired.

Adjust the detection confidence thresholds if recognition is unreliable.

License

This project is open-source and free to use under the MIT License.

