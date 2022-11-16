import socket

class TCPServer:
    recived = 0

    def __init__(self, host='localhost', port=65434):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen()

    def listen(self):
        global recived 
        while True:
            con, addr = self.sock.accept()
            while True:
                data = self.receive(con)
                if data:
                    self.recived += 1
                else:
                    break

    def receive(self, con):
        return con.recvfrom(1024)