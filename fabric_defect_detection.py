import cv2
import numpy as np
import os

# Initialize the webcam
cap = cv2.VideoCapture(0)

def detect_defects(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Use Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    # Find contours of the edges
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours around defects
    cv2.drawContours(image, contours, -1, (0, 0, 255), 2)
    
    return image, len(contours) > 0

# Main loop
while True:
    # Capture frame from webcam
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Detect defects
    result_frame, defect_detected = detect_defects(frame.copy())
    
    # Display the resulting frame
    cv2.imshow("Defect Detection", result_frame)
    
    # Save the frame if defect is detected
    if defect_detected:
        file_path = 'C:/Users/OMOLP028/OneDrive/Desktop/fabric/defect_image.jpg'
        cv2.imwrite(file_path, result_frame)
    
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()