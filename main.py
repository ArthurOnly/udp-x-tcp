from threading import Thread

from udp.client import UDPClient 
from udp.server import UDPServer

client_udp = UDPClient()
server_udp = UDPServer()

def benchmark_udp():
    def send():
        while True:
            client_udp.send('ping')
    Thread(target=server_udp.listen).start()
    Thread(target=send).start()

benchmark_udp()