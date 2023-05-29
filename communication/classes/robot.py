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

    def __str__(self) -> str:
        color = "Yellow" if self.team == True else "Blue"
        return "Robot {color} {id}:\n   x: {x:.2f}\n   y: {y:.2f}\n   orientation: {orientation:.2f}\n   vx: {vx:.2f}\n   vy: {vy:.2f}\n   Vorientation: {vorientation:.2f}".format(color = color, id = self.id, x = self.x, y = self.y, orientation = self.orientation, vx = self.vx, vy = self.vy, vorientation = self.vorientation)

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