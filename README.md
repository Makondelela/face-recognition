"""
## Face Detection and Vectorization App

This Python application allows you to select an image, detect faces within it, and convert the detected face into a vectorized image using edge detection. The app utilizes OpenCV for image processing and Tkinter for file selection.

### Features

- **Face Detection:** Detects faces in an image using a Haar Cascade Classifier.
- **Vectorization:** Converts the detected face into a vectorized image by applying Canny edge detection and drawing contours.
- **Image Selection:** Users can select an image file from their system using a graphical file dialog.
- **Image Display:** Displays the original, cropped, and vectorized images using OpenCV's `imshow` function.

### Installation

#### Prerequisites

- Python 3.x
- OpenCV
- Tkinter
- NumPy

#### Install Dependencies

To install the required Python packages, run:

bash
pip install opencv-python-headless numpy
Note: opencv-python-headless is used for environments where GUI functions like imshow are not required. Replace it with opencv-python if you need full GUI functionality.

## Usage
Prepare the Haar Cascade XML File:

Download the haarcascade_frontalface_alt2.xml file from the OpenCV GitHub repository and place it in the same directory as your script.
Run the Script:

## Start the application by running:
bash
Copy code
python qachat.py
Select an Image:

A file dialog will appear allowing you to select an image file (.jpg, .jpeg, .png).
Face Detection and Vectorization:

The application will detect faces in the selected image, display the original and cropped face, and generate a vectorized version of the detected face.
View Results:

The processed images will be displayed in separate windows.
Code Explanation
crop_face(filename): Detects and crops the face from the image using the Haar Cascade Classifier.
convert_to_vector(image): Converts the cropped face image into a vectorized form using edge detection and contour finding.
select_image(): Opens a file dialog for the user to select an image file.
resize_image(img): Resizes images to 25% of their original size for easier viewing.
Example
Here is an example workflow:

The application will prompt you to select an image.
Once selected, it will detect the face(s) in the image.
The detected face will be displayed, and a vectorized version will be generated and shown.
Contributions
Feel free to fork this repository, open issues, and submit pull requests. Contributions are always welcome!
