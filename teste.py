from vsss_client import FIRASim, Command, Team

fira = FIRASim()

cmd = Command(Team.BLUE, 1, -10, 10)
cmd = Command(Team.YELLOW, 1, 10, -10)
fira.send_command([cmd])

while True:
    robot = fira.robot(Team.BLUE, 1)
    ball = fira.ball()
    
    print(ball.x, ball.y)