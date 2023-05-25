from communication.classes.communication import Communication
from communication.settings import ports
from communication.proto_py.packet_pb2 import Environment

from communication.classes.ball import BallF
from communication.classes.robot import RobotF
from communication.classes.field import FieldF


class Env():
    def __init__(self) -> None:
        self.ball = None
        self.robots = []
        self.field = None

    def buildEnv(self) -> None:
        comm = Communication(ports["visionAddress"], ports["visionPort"], ports["refereeAddress"], ports["refereePort"], ports["firaAddress"], ports["firaPort"])
        data = comm.visionReceive()

        environment = Environment()
        environment.ParseFromString(data)

        ball = environment.frame.ball
        self.ball = BallF(ball.x, ball.y, ball.z)

        if self.robots:
            self.robots = []
        for rob in environment.frame.robots_yellow:
            robot = RobotF(id = rob.robot_id, team = True, x = rob.x, y = rob.y, orientation = rob.orientation, vx = rob.vx, vy = rob.vy, vorientation = rob.vorientation)
            self.robots.append(robot)
        for rob in environment.frame.robots_blue:
            robot = RobotF(id = rob.robot_id, team = False, x = rob.x, y = rob.y, orientation = rob.orientation, vx = rob.vx, vy = rob.vy, vorientation = rob.vorientation)
            self.robots.append(robot)

        field = environment.field
        self.field = FieldF(field.width, field.length, field.goal_width, field.goal_depth)