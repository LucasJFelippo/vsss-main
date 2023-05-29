from communication.main import Env

env = Env()
env.buildEnv()

print(env.ball)
print(env.robots)
print(env.robots[0])
print(env.robots[0].x)

env.ball.replace(0.5, 0.5, 10, 20)

robot1 = env.robots[0]
robot1.on(5, 5)
