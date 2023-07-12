import socket

class Communication():
    def __init__(self, visionAddress = "224.0.0.1", visionPort = 10002, refereeAddress = "224.5.23.2", refereePort = 10003, firaAddress = "127.0.0.1", firaPort = 20011) -> None:
        self.visionAddress = visionAddress
        self.visionPort = visionPort

        self.refereeAddress = refereeAddress
        self.refereePort = refereePort

        self.firaAddress = firaAddress
        self.firaPort = firaPort

    def visionReceive(self) -> str:
        address = (self.visionAddress, self.visionPort)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.bind(address)
        data, addr = sock.recvfrom(2048)
        return data

    def firaSend(self, package) -> None:
        address = (self.firaAddress, self.firaPort)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.sendto(package, address)