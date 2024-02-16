# Hand Tracking using OpenCV

## Introduction

This Python script captures video from the default camera (or specified camera index) using OpenCV and displays it in real-time. The script utilizes OpenCV's `VideoCapture` module to access the camera feed and `imshow` function to display the video stream.

## Prerequisites

- Python 3.x
- OpenCV (cv2) library
- NumPy library

## Installation

1. Make sure you have Python installed on your system. If not, download and install it from [Python's official website](https://www.python.org/downloads/).

2. Install the required Python libraries:

    ```pip install numpy opencv-python```

## Usage

1. Clone this repository to your local machine or download the `main.py` file.

2. Run the Python script `main.py` using the following command:

    ```python3 ./main.py```

3. If the script is unable to access the camera or fails to receive frames, an error message will be displayed.

4. To exit the script, press the 'q' key while the OpenCV window is in focus.

## Code Explanation

- The script begins by importing the necessary libraries: `numpy` for numerical operations and `cv2` (OpenCV) for computer vision functionalities.

- It initializes a `VideoCapture` object to access the camera feed. The argument `0` indicates the default camera index.

- If the camera fails to open, the script prints an error message and exits.

- The main loop continuously reads frames from the camera using the `read()` method.

- If the frame is not received (`ret` is False), the script prints an error message and exits the loop.

- The script displays the captured frame in a window titled 'Hand Tracking' using the `imshow()` function.

- Pressing the 'q' key terminates the loop and releases the camera resources.

- Finally, the script closes all OpenCV windows using `destroyAllWindows()`.

