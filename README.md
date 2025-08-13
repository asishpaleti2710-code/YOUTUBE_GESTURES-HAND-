#  YouTube Gestures – Hand Control (No MediaPipe)

A simple Python-based tool to control YouTube video playback using webcam-detected hand gestures—without MediaPipe. Based on skin tone segmentation using OpenCV, gesture-based controls include play/pause, mute/unmute, and speed adjustments.

---

##  Features

- **Play/Pause**: Center your hand to toggle playback  
- **Mute/Unmute**: Move your hand toward the left side  
- **Increase Speed**: Raise your hand upward  
- **Decrease Speed**: Lower your hand downward  
- **1-second cooldown** between actions to prevent unintended repeats  
- Detects hand gestures via skin-color segmentation in real-time using your webcam

---

##  Requirements

- Python 3.7 or newer  
- Webcam (built-in or external)  
- Dependencies:
  ```bash
  pip install opencv-python numpy pyautogui
Usage Instructions
Clone this repository:

bash
Copy
Edit
git clone https://github.com/asishpaleti2710-code/YOUTUBE_GESTURES-HAND-.git
cd YOUTUBE_GESTURES-HAND-
Install the necessary packages:

bash
Copy
Edit
pip install opencv-python numpy pyautogui
Run the gesture control script:

bash
Copy
Edit
python youtube_gesture.py
Open YouTube in your web browser and start playing a video.

Control playback using simple gestures:

Move hand upward (cy < ~150) → Increase speed

Move hand downward (cy > ~300) → Decrease speed

Move hand left (cx < ~200) → Mute/Unmute

Center hand (else) → Play/Pause

To exit, press q in the gesture-control window.

How It Works
Captures live video from your webcam using OpenCV.

Converts frames to HSV color space and applies a predefined skin-tone range for segmentation.

Uses Gaussian blur to reduce noise and improve contour detection.

Identifies the largest contour (assumed to be your hand), calculates its center position, and draws a visual hull overlay.

Performs actions based on the hand's position relative to the frame (e.g., top, bottom, left, center).

Uses PyAutoGUI to send keyboard shortcuts to the active window (YouTube browser tab).

Tips for Better Performance
Use in a well-lit environment with minimal background distractions.

Consider adjusting HSV thresholds to better match your skin tone and lighting conditions.

Ensure the browser window with YouTube is in focus for the hotkeys to register correctly.

For more accurate detection, you could explore using MediaPipe or include morphological operations (erosion/dilation).

Example
plaintext
Copy
Edit
YouTube Gesture Control (No MediaPipe)
-------------------------------------
* Play/Pause toggled
* Mute/Unmute
* Playback speed increased
* Playback speed decreased
License
This project is licensed under the MIT License. Feel free to fork, modify, and share improvements!

Contributing
Contributions are welcome! Whether it’s refining skin detection, adding gesture types (e.g., swipe for next/previous), improving performance, or switching to more robust libraries—I'd love to see your ideas.

Contact
Developed by asishpaleti2710-code. Feel free to reach out via GitHub issues if you'd like to collaborate or need help.

yaml
Copy
Edit

---

###  Optional Enhancements

Want to make the README even more engaging? Consider adding:

- An **attention-grabbing ASCII art heading** or visual emoji at the top  
- A **screenshot** of the gesture interface in action (`example_screenshot.png`)  
- **Badge icons** for things like license or Python version support  
- A brief **live demo GIF** for visual appeal

Let me know if you'd like help with any of these ideas—I’d be happy to assist!
::contentReference[oaicite:0]{index=0}








Sources

Ask ChatGPT
