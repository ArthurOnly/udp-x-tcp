
import socket

class UDPServer:
    recived = 0
    unordered = 0
    inner_buffer = ""
    last = 0

    def __init__(self, host='localhost', port=65433):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        # self.sock.listen() udp does not have listen

    def receive(self):
        try:
            data, addr = self.sock.recvfrom(2048)
            return [data, addr]
        except:
            return None

    def listen(self):
        while True:
            data = self.receive()
            if data:
                data, from_addr = data
                for char in data.decode('utf-8'):
                    self.parse_recived(char)

    def parse_recived(self, char):
        if char == ';':
            self.recived += 1

            if int(self.inner_buffer) != self.last + 1:
                self.unordered += 1
            self.last = int(self.inner_buffer)
            self.inner_buffer = ""
        else:
            self.inner_buffer += char