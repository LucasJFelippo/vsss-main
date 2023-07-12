from communication.classes.communication import Communication
from communication.settings import ports

from communication.proto_py.packet_pb2 import Packet
from communication.proto_py.replacement_pb2 import BallReplacement

class BallF():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return "Ball:\n   X: {x:.2f}\n   Y: {y:.2f}\n   Z: {z:.2f}".format(x = self.x, y = self.y, z = self.z)

    def replace(self, x = 0, y = 0, vx = 0, vy = 0):
        comm = Communication(Communication(ports["visionAddress"], ports["visionPort"], ports["refereeAddress"], ports["refereePort"], ports["firaAddress"], ports["firaPort"]))
        packet = Packet()

        replacement = BallReplacement()
        replacement.x = x
        replacement.y = y
        replacement.vx = vx
        replacement.vy = vy

        packet.replace.ball.CopyFrom(replacement)
        packet_byte = packet.SerializeToString()

        comm.firaSend(packet_byte)