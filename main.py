from lib import FIRASim , Team

fira = FIRASim()

while True:
    robot = fira.robot(Team.BLUE, 1)
    ball = fira.ball()

    print(ball.x, ball.y)
