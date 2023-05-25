import threading
import time

from communication.classes.environment import Env


env = Env()

def runEnv():
    env.buildEnv()
    time.sleep(0.016)
