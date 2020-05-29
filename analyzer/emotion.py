import cv2, os, io, numpy as np
from PIL import Image
from keras.models import load_model
from analyzer.utils.datasets import get_labels
from analyzer.utils.inference import detect_faces
from analyzer.utils.inference import draw_text
from analyzer.utils.inference import draw_bounding_box
from analyzer.utils.inference import apply_offsets
from analyzer.utils.inference import load_detection_model
from analyzer.utils.preprocessor import preprocess_input
from config.config import Config
import constants

class Emotion:
    def __init__(self):
        # loading models
        script_dir = os.path.dirname(__file__)
        emotion_model_path = os.path.join(constants.ROOT_DIR, constants.EMOTION_MODEL)

        configuration = Config()

        self.input_camera = configuration.get('INPUT_CAMERA')

        self.emotion_classifier = load_model(emotion_model_path)
        self.emotion_target_size = self.emotion_classifier.input_shape[1:3]
        self.emotion_labels = get_labels('fer2013')
        self.emotion_offsets = (20, 40)

    def detect(self, frame, faces):
        if self.input_camera == constants.USB_CAMERA:
            gray_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        data = []

        for face_coordinates in faces:
            x1, x2, y1, y2 = apply_offsets(face_coordinates, self.emotion_offsets)
            gray_face = gray_image[y1:y2, x1:x2]
            try:
                gray_face = cv2.resize(gray_face, (self.emotion_target_size))
            except:
                continue

            gray_face = preprocess_input(gray_face, True)

            gray_face = np.expand_dims(gray_face, 0)
            gray_face = np.expand_dims(gray_face, -1)
            emotion_prediction = self.emotion_classifier.predict(gray_face)

            emotion_probability = np.max(emotion_prediction)
            emotion_label_arg = np.argmax(emotion_prediction)
            emotion_text = self.emotion_labels[emotion_label_arg]

            face = {
                "anger": emotion_prediction[0][0],
                "disgust": emotion_prediction[0][1],
                "fear": emotion_prediction[0][2],
                "happiness": emotion_prediction[0][3],
                "sadness": emotion_prediction[0][4],
                "surprise": emotion_prediction[0][5],
                "neutral": emotion_prediction[0][6],
            }

            data.append(face)

        return data
