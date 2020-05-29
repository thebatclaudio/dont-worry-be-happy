# Class used to get frames from input camera

import time, constants, cv2
from config.config import Config

class Eye:
    def __init__(self):

        configuration = Config()

        self.input_camera = configuration.get('INPUT_CAMERA')

        self.camera = cv2.VideoCapture(0)

    def capture(self):
        if self.input_camera == constants.USB_CAMERA:
            ret, frame = self.camera.read()
            return frame

        return None