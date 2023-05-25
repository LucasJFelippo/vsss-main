from communication.main import Env

env = Env()  # Env has as attributes ball, robots, field and as methods buildEnv
env.buildEnv()  # buildEnv() calls FiraSim infos, build the objects and define the Env's attributes

env.ball  # Ball object has x,y,z as attributes, and a replace method that