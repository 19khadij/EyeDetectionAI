# EyeDetectionAI
# Webcam Face and Eye Detection

This Python script captures video from a webcam and performs real-time face and eye detection using OpenCV's Haar Cascade classifiers. It detects faces in the video feed, draws rectangles around them, and adds a "FACE" label. It also detects eyes within the detected face regions and adds "EYE" labels for each eye.

## Getting Started

### Prerequisites

- Python
- OpenCV (cv2)
- Haar Cascade XML files for face and eye detection (e.g., "haarcascade_frontalface_default.xml" and "haarcascade_eye.xml")

You can install OpenCV using pip:

```bash
pip install opencv-python

Usage
Clone this repository to your local machine:

git clone https://github.com/yourusername/your-repo.git

Navigate to the project directory:

cd your-repo

Run the Python script:

python webcam_face_eye_detection.py
Press the 's' key to stop the webcam and close the application.
