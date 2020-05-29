import os, cv2 as cv, numpy as np
from PIL import Image
from config.config import Config
import constants

class FaceDetection:
    def __init__(self):
        # loading models
        script_dir = os.path.dirname(__file__)
        classifier_abs_path = os.path.join(constants.ROOT_DIR, constants.FRONTALFACE_CLASSIFIER)

        configuration = Config()

        self.face_cascade = cv.CascadeClassifier(classifier_abs_path)
        self.input_camera = configuration.get('INPUT_CAMERA')
    
    def detect(self, frame):

        if self.input_camera == constants.USB_CAMERA:
            grayScaleImg = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

        # face detection
        faces = self.face_cascade.detectMultiScale(grayScaleImg, 1.3, 5)

        return faces