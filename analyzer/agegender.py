import cv2, os, numpy as np
from time import sleep
from keras.utils.data_utils import get_file
from analyzer.wideresnet import WideResNet
from config.config import Config
import constants

class AgeGender:
    def __init__(self):
        # loading models
        script_dir = os.path.dirname(__file__)
        emotion_model_path = os.path.join(constants.ROOT_DIR, constants.AGE_GENDER_MODEL)

        configuration = Config()

        self.input_camera = configuration.get('INPUT_CAMERA')

        model_dir = os.path.join(os.getcwd(), "pretrained_models").replace("//", "\\")
        self.model = WideResNet(64, depth=16, k=8)()
        fpath = get_file(emotion_model_path,
                    "https://github.com/Tony607/Keras_age_gender/releases/download/V1.0/weights.18-4.06.hdf5",
                    cache_subdir=model_dir)
        self.model.load_weights(fpath)

    def crop_face(self, imgarray, section, margin=40, size=64):
        """
        :param imgarray: full image
        :param section: face detected area (x, y, w, h)
        :param margin: add some margin to the face detected area to include a full head
        :param size: the result image resolution with be (size x size)
        :return: resized image in numpy array with shape (size x size x 3)
        """
        img_h, img_w, _ = imgarray.shape
        if section is None:
            section = [0, 0, img_w, img_h]
        (x, y, w, h) = section
        margin = int(min(w,h) * margin / 100)
        x_a = x - margin
        y_a = y - margin
        x_b = x + w + margin
        y_b = y + h + margin
        if x_a < 0:
            x_b = min(x_b - x_a, img_w-1)
            x_a = 0
        if y_a < 0:
            y_b = min(y_b - y_a, img_h-1)
            y_a = 0
        if x_b > img_w:
            x_a = max(x_a - (x_b - img_w), 0)
            x_b = img_w
        if y_b > img_h:
            y_a = max(y_a - (y_b - img_h), 0)
            y_b = img_h
        cropped = imgarray[y_a: y_b, x_a: x_b]
        resized_img = cv2.resize(cropped, (size, size), interpolation=cv2.INTER_AREA)
        resized_img = np.array(resized_img)
        return resized_img, (x_a, y_a, x_b - x_a, y_b - y_a)

    def detect(self, frame, faces):
        face_imgs = np.empty((len(faces), 64, 64, 3))

        data = []

        for i, face in enumerate(faces):
            face_img, cropped = self.crop_face(frame, face, margin=40, size=64)
            (x, y, w, h) = cropped
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 200, 0), 2)
            face_imgs[i,:,:,:] = face_img
        if len(face_imgs) > 0:
            # predict ages and genders of the detected faces
            results = self.model.predict(face_imgs)
            predicted_genders = results[0]
            ages = np.arange(0, 101).reshape(101, 1)
            predicted_ages = results[1].dot(ages).flatten()


        for i, face in enumerate(faces):
            face = {
                "gender": 'male',
                "age": int(predicted_ages[i])
            }

            if(predicted_genders[i][0] > 0.5):
                face['gender'] = 'female'

            data.append(face)

        return data