
import socket

class UDPServer:
    recived = 0
    unordered = 0

    def __init__(self, host='localhost', port=65433):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        # self.sock.listen() udp does not have listen

    def receive(self):
        try:
            data, addr = self.sock.recvfrom(1024)
            return [data, addr]
        except:
            return None

    def listen(self):
        previous = 0
        while True:
            data = self.receive()
            if data:
                data, addr = data
                self.recived += 1
                data = int(data.decode('utf-8').split(';')[0])
                if data != previous + 1:
                    print(f'Unordered: {data} != {previous + 1}')
                    self.unordered += 1
                previous = data
