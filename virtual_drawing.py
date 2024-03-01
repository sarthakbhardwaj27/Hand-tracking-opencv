import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize OpenCV
cap = cv2.VideoCapture(0)

# Define a list to store the trajectory of the finger
finger_trajectory = []

# Define the eraser mode
eraser_mode = False

# Main loop
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe
        results = hands.process(rgb_frame)

        # If landmarks are detected, draw on the screen
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get the coordinates of the index finger tip
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                height, width, _ = frame.shape
                finger_x, finger_y = int(index_finger_tip.x * width), int(index_finger_tip.y * height)

                # Check if the eraser mode is activated
                if index_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y:
                    eraser_mode = True
                    finger_trajectory = []  # Clear the trajectory when eraser mode is activated
                else:
                    eraser_mode = False

                # Add the finger tip coordinates to the trajectory list if not in eraser mode
                if not eraser_mode:
                    finger_trajectory.append((finger_x, finger_y))

                    # Draw the trajectory of the finger
                    if len(finger_trajectory) > 1:
                        for i in range(1, len(finger_trajectory)):
                            cv2.line(frame, finger_trajectory[i - 1], finger_trajectory[i], (0, 255, 0), 4)

                # Check if the finger is lifted off the screen
                if index_finger_tip.z > 0.2:  # Adjust threshold as per your need
                    finger_trajectory = []

        # Add text to the frame
        cv2.putText(frame, 'Move your index finger to draw. Raise your hand to erase.', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        # Show the output frame
        cv2.imshow('MediaPipe Hands', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the capture and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
