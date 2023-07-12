
import socket
import configparser
import os
from protos import packet_pb2 as packet

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class FIRASim(metaclass=SingletonMeta):
    def __init__(self):
        config = configparser.ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_file)

        self.vision_address = str(config['FIRA']['vision_address'])
        self.vision_port = int(config['FIRA']['vision_port'])
        self.command_address = str(config['FIRA']['command_address'])
        self.command_port = int(config['FIRA']['command_port'])

        # create multicast socket for vision
        self.vision_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.vision_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.vision_sock.bind((self.vision_address, self.vision_port))

        # create unicast socket for commands
        # self.command_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.command_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # self.command_sock.bind((self.command_address, self.command_port))

    def receive(self):
        data, addr = self.vision_sock.recvfrom(2048)
        return data
    
    def send(self, package):
        self.command_sock.sendto(package, (self.address, self.command_port))

    def close(self):
        self.vision_sock.close()
        # self.command_sock.close()

    def env(self):
        data = self.receive()
        env = packet.Environment()
        env.ParseFromString(data)
        return env
    
# class Referee(metaclass=SingletonMeta):
# class SSLVision(metaclass=SingletonMeta):