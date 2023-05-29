import time

from communication.main import Env


env = Env()
env.buildEnv()

print(env)

env.ball.replace(0.5, 0.5, 10, 20)

robot1 = env.robots[0]
print(robot1.x)
robot1.on(5, 5)
time.sleep(2)
print(robot1.x)