# VIRTUAL-NOTEPAD-USING-OPENCV-AND-MEDIAPIPE

This project implements a Virtual Notepad using hand gestures detected through a webcam. You can draw, change colors, and erase using simple gestures.

#Features

Draw using index-thumb pinch gesture.

Change Colors by bringing index and middle fingers close together.

Eraser Mode by showing an open palm.

Color Options: Blue, Green, Red, Yellow.

Adjustable Brush Size for drawing and erasing.


🖥 Demo

 (Add a GIF or screenshot of the app in action)

📂 Project Structure

├── main.py                 # Main application code
├── README.md               # Project documentation
└── requirements.txt        # Required Python libraries

⚙ Installation

1. Clone the repository:



git clone https://github.com/YourUsername/Virtual-Notepad-With-Eraser.git
cd Virtual-Notepad-With-Eraser

2. Create a virtual environment (Optional but recommended):



python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install required libraries:



pip install -r requirements.txt

4. Run the application:



python main.py

🛠 Requirements

Python 3.7+

OpenCV (cv2)

MediaPipe (mediapipe)

Numpy (numpy)


Install the dependencies with:

pip install opencv-python mediapipe numpy

🎯 How to Use

Drawing Mode: Pinch your index finger and thumb together.

Change Color: Bring index and middle fingers close together.

Eraser Mode: Show an open palm to activate the eraser.

Exit: Press 'q' to quit the application.


🧠 How It Works

1. Hand Detection: MediaPipe tracks hand landmarks.

2. Gesture Recognition: Specific hand gestures trigger drawing, color change, and eraser modes.

3. Drawing on Canvas: Uses OpenCV to draw on a transparent canvas and merge it with the video feed.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8.0-orange)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

