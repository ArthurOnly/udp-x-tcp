import socket

class TCPServer:
    recived = 0
    unordered = 0
    inner_buffer = ""
    last = 0

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
                    for char in data.decode('utf-8'):
                        self.parse_recived(char)
                else:
                    break

    def receive(self, con):
        return con.recv(2048)

    def parse_recived(self, char):
        if char == ';':
            self.recived += 1

            if int(self.inner_buffer) != self.last + 1:
                self.unordered += 1
            self.last = int(self.inner_buffer)
            self.inner_buffer = ""
        else:
            self.inner_buffer += char