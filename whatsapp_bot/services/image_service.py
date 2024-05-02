import io

import cv2
import numpy as np
from PIL import Image


class ImageService:

    @staticmethod
    def detect_faces(image_data: bytes) -> bool:
        image = Image.open(io.BytesIO(image_data))

        # Convert image to grayscale
        gray = image.convert('L')

        # Load face detection classifier
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Convert PIL Image to numpy array
        np_image = np.array(gray, 'uint8')

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(np_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        return len(faces) > 0
