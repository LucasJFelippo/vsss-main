from lib import FIRASim

fira = FIRASim()

while True:
    data = fira.env()
    print(data)
