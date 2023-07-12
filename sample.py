# Receive Multcast

import socket

server_address = ('224.0.0.1', 10002)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(server_address)
data, addr = sock.recvfrom(2048)

# Receive Protobuf
from communication.proto_py.packet_pb2 import Environment
from communication.proto_py.command_pb2 import Command
from communication.proto_py.packet_pb2 import Packet
from communication.proto_py.replacement_pb2 import RobotReplacement
from communication.proto_py.common_pb2 import Robot


environment = Environment()
environment.ParseFromString(data)

print(environment.frame.robots_yellow[0])



# Sending
packet = Packet()
comm = Command()

robre = RobotReplacement()
robot = Robot()
robot.robot_id = 0
robot.x = 0
robot.y = 0
robot.orientation = 90
robot.vx = 0
robot.vy = 0
robre.position.CopyFrom(robot)
robre.yellowteam = True
robre.turnon = True

packet.replace.robots.append(robre)
packet_byte = packet.SerializeToString()
sock.sendto(packet_byte,("127.0.0.1", 20011))