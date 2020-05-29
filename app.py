import datetime

from eye.eye import Eye
from analyzer.analyzer import Analyzer
from sender.sender import Sender
from config.config import Config

configuration = Config()

eye = Eye()
analyzer = Analyzer()
sender = Sender()

frame = eye.capture()
while True:
    data = analyzer.analyze(frame)

    sender.send(data)

    frame = eye.capture()