import cv2
import numpy as np
import pyautogui
import time

cap = cv2.VideoCapture(0)
last_action_time = time.time()

def perform_action(action):
    global last_action_time
    if time.time() - last_action_time < 1:  # 1-second cooldown
        return
    last_action_time = time.time()
    
    if action == "play_pause":
        pyautogui.press('space')
        print("Play/Pause toggled")
    elif action == "mute":
        pyautogui.press('m')
        print("Mute/Unmute")
    elif action == "speed_up":
        pyautogui.hotkey('shift', '>')
        print("Playback speed increased")
    elif action == "speed_down":
        pyautogui.hotkey('shift', '<')
        print("Playback speed decreased")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  # Mirror view
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Skin color range for detection
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Noise reduction
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 5000:
            hull = cv2.convexHull(max_contour)
            cv2.drawContours(frame, [hull], -1, (0, 255, 0), 2)
            
            # Find moments to detect hand position
            M = cv2.moments(max_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                
                cv2.circle(frame, (cx, cy), 7, (255, 0, 0), -1)
                
                # Simple gesture logic
                if cy < 150:
                    perform_action("speed_up")
                elif cy > 300:
                    perform_action("speed_down")
                elif cx < 200:
                    perform_action("mute")
                else:
                    perform_action("play_pause")
    
    cv2.imshow("YouTube Gesture Control (No Mediapipe)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
