from communication.classes.communication import Communication
from communication.settings import ports

from communication.proto_py.packet_pb2 import Packet
from communication.proto_py.command_pb2 import Command
from communication.proto_py.replacement_pb2 import RobotReplacement
from communication.proto_py.common_pb2 import Robot

class RobotF():
    def __init__(self, id, team, x, y, orientation, vx, vy, vorientation) -> None:
        self.id = id
        self.team = team
        self.x = x
        self.y = y
        self.orientation = orientation
        self.vx = vx
        self.vy = vy
        self.vorientation = vorientation

    def on(self, left, right) -> None:
        comm = Communication(Communication(ports["visionAddress"], ports["visionPort"], ports["refereeAddress"], ports["refereePort"], ports["firaAddress"], ports["firaPort"]))
        packet = Packet()
        cmd = Command()

        cmd.id = self.id
        cmd.yellowteam = self.team
        cmd.wheel_left = left
        cmd.wheel_right = right

        packet.cmd.robot_commands.append(cmd)
        packet_byte = packet.SerializeToString()

        comm.firaSend(packet_byte)

    def replace(self, x = 0, y = 0, orientation = 0) -> None:
        comm = Communication(Communication(ports["visionAddress"], ports["visionPort"], ports["refereeAddress"], ports["refereePort"], ports["firaAddress"], ports["firaPort"]))
        packet = Packet()

        replacement = RobotReplacement()
        robot = Robot()
        robot.robot_id = self.id
        robot.x = x
        robot.y = y
        robot.orientation = orientation
        replacement.position.CopyFrom(robot)
        replacement.yellowteam = self.team
        replacement.turnon = True

        packet.replace.robots.append(replacement)
        packet_byte = packet.SerializeToString()

        comm.firaSend(packet_byte)