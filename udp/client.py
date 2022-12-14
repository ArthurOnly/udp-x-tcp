import socket

class UDPClient:
    def __init__(self, host='localhost', port=65433):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data):
        self.sock.sendto(data.encode(), (self.host, self.port))