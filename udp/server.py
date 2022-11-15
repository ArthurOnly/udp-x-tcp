
import socket

class UDPServer:
    recived = 0

    def __init__(self, host='localhost', port=65433):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        self.sock.setblocking(0)

    def receive(self):
        try:
            data, addr = self.sock.recvfrom(1024)
            return [data, addr]
        except:
            return None

    def listen(self):
        while True:
            data = self.receive()
            if data:
                data, addr = data
                self.recived += 1
                print(f"UDP RECIVE: {data}-{addr}-{self.recived}")
                self.send(data, addr)

    def send(self, data, addr):
        self.sock.sendto(data, addr)