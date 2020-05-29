from analyzer.facedetection import FaceDetection
from analyzer.agegender import AgeGender
from analyzer.emotion import Emotion
from utils.logger import Logger
from config.config import Config
import constants

class Analyzer:
    def __init__(self):
        self.logger = Logger()
        configuration = Config()
        self.facedetection = FaceDetection()

        self.emotion = Emotion()
        self.agegender = AgeGender()
        
    def analyze(self, frame):
        faces = self.facedetection.detect(frame)

        if(len(faces) > 0):
            self.analyzeFaces(frame, faces)
        else:
            return []

    def analyzeFaces(self, frame, faces):
        emotions = self.emotion.detect(frame, faces)
        age_genders = self.agegender.detect(frame, faces)

        data = []

        i = 0

        if len(age_genders) > len(emotions):
            for age_gender in age_genders:
                if i < len(emotions):
                    age_gender['emotion'] = emotions[i]
                else:
                    age_gender['emotion'] = None
                i += 1

                obj = {
                    'face_attributes': age_gender
                }

                data.append(obj)
        elif len(emotions) < len(age_genders):
            for emotion in emotions:
                if i < len(age_genders):
                    age_gender['emotion'] = emotions[i]
                    data.append(age_gender)
                else:
                    newObject = {
                        "face_attributes": {
                            "age": None,
                            "gender": None,
                            "emotion": emotions[i]
                        }
                    }
                    data.append(newObject)
        else:
            for age_gender in age_genders:
                age_gender['emotion'] = emotions[i]
                i += 1

                obj = {
                    'face_attributes': age_gender
                }

                data.append(obj)

            self.logger.log(data)

            return data
        return []