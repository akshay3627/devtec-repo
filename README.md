# Fabric Defect Detection

This project implements a defect detection system using OpenCV and Python. The system captures video frames from a webcam, processes them to detect defects, and saves the frames containing detected defects to the local file system.

## Features

- **Real-time Defect Detection**: Uses Canny edge detection and contour detection to identify defects in video frames.
- **Webcam Integration**: Captures frames from the default webcam.
- **Image Saving**: Automatically saves frames containing defects to a specified folder.
- **Customizable Parameters**: Adjust edge detection thresholds and blur settings for fine-tuning.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/fabric-defect-detection.git
   cd fabric-defect-detection
   ```

2. Install the required dependencies:

   ```bash
   pip install opencv-python numpy
   ```

## Usage

1. Ensure your webcam is connected to your system.
2. Run the script:

   ```bash
   python defect_detection.py
   ```

3. The program will start detecting defects in real-time. Press **`q`** to exit the application.

4. If a defect is detected, the frame is saved to the specified file path (default: `C:/Users/OMOLP028/OneDrive/Desktop/fabric/defect_image.jpg`).

## How It Works

1. The program captures frames from the webcam.
2. Each frame is converted to grayscale and blurred to reduce noise.
3. Canny edge detection is applied to highlight edges in the image.
4. Contours are identified from the edges, and if any contours are detected, the program marks the defects in the frame.
5. Frames with defects are saved to the specified location.

## Demo

### Defect Detected:
![Defect Detected](https://via.placeholder.com/600x400?text=Sample+Defect+Frame)

## File Structure

- `defect_detection.py`: Main Python script for detecting defects.
- `README.md`: Project documentation.

## Customization

- **Edge Detection Thresholds**: Modify the values in the `cv2.Canny` function to fine-tune detection:
  ```python
  edges = cv2.Canny(blurred, 50, 150)
  ```
- **Save Path**: Change the file path where detected frames are saved:
  ```python
  file_path = 'your/custom/path/defect_image.jpg'
  ```

## Contribution

Feel free to submit issues and pull requests if you want to contribute to this project.

## License

This project is licensed under the [MIT License](LICENSE).

