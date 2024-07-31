import cv2
import tkinter as tk
import numpy as np
from tkinter import filedialog

convert = lambda image: convert_to_vector(image)


def convert_to_vector(image):
    # Read the input image

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection to find outlines
    edges = cv2.Canny(gray_image, 100, 200)

    # Find contours (shapes) in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a new blank image to draw the vectorized image
    vector_image = np.zeros_like(image)

    # Draw contours on the blank image to form vectorized shapes
    cv2.drawContours(vector_image, contours, -1, (255, 255, 255), 1)
    print(contours)
    # Save the vectorized image
    cv2.imshow("face", resize_image(vector_image))


def crop_face(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h),
                      (0, 0, 255), 2)

        faces = img[y:y + h, x:x + w]
        cv2.imshow("face", resize_image(img))
        cv2.imwrite('face.jpg', resize_image(img))
        #cv2.waitKey(0)
        # Destroying present windows on screen
    return faces


def resize_image(img):

    scale_percent = 25  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    return resized

def select_image():
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select a file
    file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    return file_path


if __name__ == '__main__':

    image = crop_face(select_image())
    img = cv2.imread('face.jpg')
    cv2.imshow('image',resize_image(image))

    cv2.imshow('image1',img)
    convert(image)
    cv2.waitKey(0)
    # Destroying present windows on screen
    cv2.destroyAllWindows()
