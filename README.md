# Eye Tracking System

This repository contains the code for a basic eye tracking system that processes video frames to detect and highlight a region of interest (ROI) around the eye. The system detects contours in the specified ROI, identifies the largest contour, and draws a bounding rectangle and crosshairs on it to indicate the position of the eye.

## Features

- **Real-time Processing:** Processes video frames in real-time to detect the eye's position.
- **Region of Interest (ROI):** Focuses on a specific area of the video frame to reduce computational load and improve accuracy.
- **Contour Detection:** Identifies the largest contour within the ROI and marks it with a bounding rectangle.
- **Crosshairs:** Draws crosshairs over the detected eye to visualize its center.

## Prerequisites

Before running the code, ensure you have the following installed:

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)

You can install the required Python packages using pip:

```bash
pip install opencv-python numpy
```

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/eye-tracking-system.git
   cd eye-tracking-system
   ```

2. **Add your video file:**

   Ensure that the video file (`eye_recording.flv`) is located in the same directory as the script or update the path in the code if it’s located elsewhere.

3. **Run the code:**

   ```bash
   python eye_tracking.py
   ```

   This will start processing the video and display the following windows:
   - **Threshold:** Shows the binary thresholded image used for contour detection.
   - **Gray ROI:** Displays the grayscale, blurred version of the ROI.
   - **ROI:** Shows the original ROI with the detected contours, bounding rectangle, and crosshairs.

4. **Exit the program:**

   The program will continue to process and display frames until you press the `Esc` key.

## Code Explanation

### Main Components

- **Video Capture:** The video is loaded using `cv2.VideoCapture()`.
- **Region of Interest (ROI):** A specific part of the frame is defined as the ROI where the eye is expected to be.
- **Grayscale and Gaussian Blur:** The ROI is converted to grayscale and blurred to reduce noise.
- **Thresholding:** A binary threshold is applied to highlight the eye.
- **Contour Detection:** Contours are detected, and the largest one is assumed to be the eye.
- **Drawing:** A bounding rectangle and crosshairs are drawn around the detected contour.

### Key Functions

- `cv2.cvtColor`: Converts the image to grayscale.
- `cv2.GaussianBlur`: Applies a Gaussian blur to the image.
- `cv2.threshold`: Applies a binary threshold to the image.
- `cv2.findContours`: Finds the contours in the thresholded image.
- `cv2.boundingRect`: Calculates the bounding rectangle for a contour.
- `cv2.rectangle`: Draws a rectangle on the image.
- `cv2.line`: Draws lines (crosshairs) on the image.
- `cv2.imshow`: Displays the image in a window.

## Customization

- **ROI Size:** Modify the ROI coordinates (`frame[269:795, 537:1416]`) in the code to adjust the area being processed.
- **Threshold Value:** Change the threshold value (`3` in `cv2.threshold`) for different lighting conditions.
- **Contour Area:** You can add more logic to handle multiple contours if needed.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

