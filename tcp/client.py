import socket

class TCPClient:
    def __init__(self, host='localhost', port=65434):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def send(self, data):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        s.send(data.encode())
        s.close()

    def send_with_connection(self, data):
        self.sock.send(data.encode())