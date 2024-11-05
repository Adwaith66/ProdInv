
# Object Detection with Flask and OpenCV

This project implements an object detection system using OpenCV with a MobileNet SSD model and Flask for handling HTTP requests. The system captures video from a webcam, detects objects in real-time, and sends the detected information (including the image) to a Flask server for uploading to s3 and RDS server on AWS.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [File Structure](#file-structure)

## Setup

1. **Clone the Repository:**

   Clone this repository to your local machine singu:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Download the Model:**

   Download the MobileNet SSD model files from the following repository:

   [MobileNet SSD GitHub Repository](https://github.com/djmv/MobilNet_SSD_opencv)

   Place the downloaded files (`MobileNetSSD_deploy.prototxt` and `MobileNetSSD_deploy.caffemodel`) in the `tr` folder.

3. **Folder Structure:**

   Your folder structure should look like this:

   ```
   your-project-folder/
   │── data.py
   │── server.py
   ├── tr/
   │   ├── MobileNetSSD_deploy.prototxt
   │   └── MobileNetSSD_deploy.caffemodel
   └── README.md
   ```

## Usage

1. **Start the Flask Server:**

   Open a terminal and navigate to the `app` folder. Run the Flask server with the following command:

   ```bash
   python server.py
   ```

   The server will start running at `http://localhost:3000`.

2. **Run the Object Detection Script:**

   Open another terminal in the `app` folder and run the object detection script:

   ```bash
   python object_detection.py
   ```

   This script will start capturing video from your webcam. It will detect objects in real-time and send the detected objects along with the image to the Flask server.


## File Descriptions

- `data.py`: This script captures video from the webcam, detects objects using OpenCV's MobileNet SSD model, and sends the detected information to the Flask server.
  
- `server.py`: This Flask server receives detection data, including labels, confidence scores, and images, and processes them.

