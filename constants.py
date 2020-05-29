import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTALFACE_CLASSIFIER = 'resources/models/haarcascade_frontalface_default.xml'
# EMOTION_MODEL = 'resources/models/emotion_model.hdf5'
EMOTION_MODEL = 'resources/models/fer2013_mini_XCEPTION.65-0.66.hdf5'
AGE_GENDER_MODEL = 'resources/models/age_gender_model.hdf5'

# INPUT CAMERA
USB_CAMERA = 0