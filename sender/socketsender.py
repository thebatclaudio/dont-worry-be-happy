import socket, sys
from config.config import Config
from utils.logger import Logger

class SocketSender:
    tcp_socket = None

    def __init__(self):
        self.tcp_socket = socket.socket()
        self.logger = Logger()
        configuration = Config()

        try:
            self.tcp_socket.connect((configuration.get('SOCKET_HOST'), configuration.get('SOCKET_PORT')))
        except socket.error:
            self.logger.log("Can't connect to socket "+configuration.get('SOCKET_HOST')+":"+str(configuration.get('SOCKET_PORT')))
            sys.exit(0)
            
    def __del__(self):
        if(self.tcp_socket):
            self.tcp_socket.close()

    def send(msg):
        self.logger.log('SENDING DATA VIA SOCKET')
        self.logger.log(msg)
        self.tcp_socket.send(msg)