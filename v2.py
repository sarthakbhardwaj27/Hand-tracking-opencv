import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

#from webcam input
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("ignoring empty camera frame")
            #if loading a video, use 'break' instead of 'continue'
            continue
        #to improve per formance, optionally mark the image as not writeable to pass by reference 
        image.flags.writeable = False
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        #draw the hand annotations on the image
        image.flags.writeable = True
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        #initially set finger coint to 0 for each cap
        fingerCount = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                #get hand index to check label (left or right)
                handIndex = results.multi_hand_landmarks. index(hand_landmarks)
                handLabel = results.multi_handedness[handIndex].classifications[9].label

                #set variables ot keep landmarks positions (x and y)
                handLandmarks = []

                #fill list with x and y positions of each landmark
                for landmarks in hand_landmarks.landmark:
                    handLandmarks.append([landmarks.x, landmarks.y])

                #test conditions for each finger: count is increase if finger is considered rasied
                #thumb: tip*position must be greater or lwer than ip*position depending on hand label
                
                if handLandmarks[8][1] < handLandmarks[6][1]:       #Index finger
                    fingerCount = fingerCount+1
                if handLandmarks[12][1] < handLandmarks[10][1]:     #Middle finger
                    fingerCount = fingerCount+1
                if handLandmarks[16][1] < handLandmarks[14][1]:     #Ring finger
                    fingerCount = fingerCount+1
                if handLandmarks[20][1] < handLandmarks[18][1]:     #Pinky
                    fingerCount = fingerCount+1

                #draw hand landmakrs
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS, 
                    mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style()
                )

            #display finger count
            cv2.putText(
                image, 
                str(fingerCount),
                (50,450),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (255,0,0),
                10
            )

            #display image
            cv2.imshow('Gesture', image)
            if cv2.waitKey(1) == ord('q'):
                break
            cap.release()
            cv2.destroyAllWindows()
