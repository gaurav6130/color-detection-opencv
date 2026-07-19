# Color Detection using OpenCV

A real-time color detection project built with Python and OpenCV. This application detects yellow-colored objects from a webcam using the HSV (Hue, Saturation, Value) color space and highlights them with bounding boxes.

## Features

- Real-time webcam input
- Detects yellow-colored objects
- Uses HSV color thresholding
- Finds contours of detected objects
- Draws bounding boxes around detected objects

## Technologies Used

- Python 3
- OpenCV
- NumPy

## Project Structure

```
color-detection-opencv/
│── main.py
│── colors.py
│── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/gaurav6130/color-detection-opencv.git
```

2. Move into the project folder

```bash
cd color-detection-opencv
```

3. Install dependencies

```bash
pip install opencv-python numpy
```

## Run the Project

```bash
python main.py
```

## How It Works

1. Captures video from the webcam.
2. Converts each frame from BGR to HSV.
3. Applies the HSV range for yellow.
4. Creates a binary mask.
5. Detects contours.
6. Draws a bounding box around the detected object.

## Future Improvements

- Detect multiple colors
- Display object center coordinates
- Track moving objects
- Save detection results
- Add a graphical interface (GUI)

## Author

**Gaurav Singh**