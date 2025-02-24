import cv2
import numpy as np

# Open the video file
cap = cv2.VideoCapture("eye_recording.flv")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Define the region of interest (ROI)
    roi = frame[269:795, 537:1416]
    rows, cols, _ = roi.shape

    # Convert ROI to grayscale and apply Gaussian blur
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

    # Threshold the image
    _, threshold = cv2.threshold(gray_roi, 3, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    # Draw contours and rectangles
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
        break

    # Display the results
    cv2.imshow("Threshold", threshold)
    cv2.imshow("Gray ROI", gray_roi)
    cv2.imshow("ROI", roi)
    
    # Exit if the 'Esc' key is pressed
    key = cv2.waitKey(30)
    if key == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
