import socket

class TCPClient:
    def __init__(self, host='localhost', port=65434):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def send(self, data):
        self.sock.send(data.encode())