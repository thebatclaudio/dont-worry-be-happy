from config.config import Config

class Logger:
    def __init__(self):
        configuration = Config()
        self._DEBUG = configuration.get('DEBUG')

    def log(self, message):
        if(self._DEBUG):
            print(message)
