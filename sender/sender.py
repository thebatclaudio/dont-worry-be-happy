import time, constants, requests, json, numpy as np
from sender.socketsender import SocketSender
from sender.numpyencoder import NumpyEncoder
from config.config import Config

class Sender:
    def __init__(self):
        configuration = Config()
        self.send_via_api = configuration.get('SEND_VIA_API')
        self.send_via_socket = configuration.get('SEND_VIA_SOCKET')
        self.device_id = configuration.get('DEVICE_ID')
        self.api_endpoint = configuration.get('API_ENDPOINT').replace(':id', str(self.device_id))
        self.api_token = configuration.get('API_TOKEN')

        if(self.send_via_socket):
            self.socket = SocketSender()

    def send(self, data):
        if(self.send_via_api):
            self.sendViaApi(data)

        if(self.send_via_socket):
            self.sendViaSocket(data)

    def sendViaApi(self, data):
        params = {
            'data' : json.dumps(data, cls=NumpyEncoder),
            'timestamp': time.time(),
            'device_id': self.device_id
        }

        headers = {
            'Authorization': self.api_token
        }

        return requests.post(url = self.api_endpoint, data = params, headers = headers)

    def sendViaSocket(self, data):
        return self.socket.send(json.dumps(data, cls=NumpyEncoder).encode())