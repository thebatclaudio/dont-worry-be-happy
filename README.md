# Don't worry, be happy

Face detection + Age/Gender Recognition + Emotion Recognition with Python & Tensorflow

## Installation

Clone the repository.

Install these dependencies with `pip3 install <module name>`
-	tensorflow
-	numpy
-	scipy
-	imageio
-	opencv-python
-	pillow
-	pandas
-	matplotlib
-	h5py
-	keras

Compile your `config.json` inside `config` folder.

Now, you can run the project:
`python3 app.py`

or using pm2.

## Models

In `constants.py` you can find the models that I used to detect faces, age, gender and emotions.
I didn't include these models in my repository, but you can download them:

- [HAAR Cascade Frontal Face](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
- [Emotion Model (fer2013_mini_XCEPTION)](https://github.com/oarriaga/face_classification/blob/master/trained_models/emotion_models/fer2013_mini_XCEPTION.102-0.66.hdf5)
- [Age/Gender Model](https://github.com/yu4u/age-gender-estimation/releases/download/v0.5/weights.28-3.73.hdf5)

## To train new models for emotion classification

- Download the fer2013.tar.gz file from [here](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)
- Move the downloaded file to the datasets directory inside this repository.
- Untar the file:
`tar -xzf fer2013.tar`
- Download train_emotion_classifier.py from orriaga's repo [here](https://github.com/oarriaga/face_classification/blob/master/src/train_emotion_classifier.py)
- Run the train_emotion_classification.py file:
`python3 train_emotion_classifier.py`


## Credit
* Computer vision powered by OpenCV.
* Neural network scaffolding powered by Keras with Tensorflow
* Convolutional Neural Network (CNN) deep learning architecture is from this [research paper](https://github.com/oarriaga/face_classification/blob/master/report.pdf)
* Pretrained Keras model and much of the OpenCV code provided by GitHub user [oarriaga](https://github.com/oarriaga)
* Emotion recognition based on [petercunha/Emotion](https://github.com/petercunha/Emotion)
* Age and gender recognition based on [Tony607/Keras_age_gender](https://github.com/Tony607/Keras_age_gender)