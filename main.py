from threading import Thread
from time import sleep

from udp.client import UDPClient 
from udp.server import UDPServer
from tcp.client import TCPClient
from tcp.server import TCPServer

client_udp = UDPClient()
server_udp = UDPServer()

server_tcp = TCPServer()
client_tcp = TCPClient()

def benchmark_udp():
    def send():
        while True:
            client_udp.send('ping')
    def log():
        elapsed_time = 1
        while True:
            print(f'UDP - {int(server_udp.recived/elapsed_time)}/s')
            elapsed_time += 2
            sleep(2)
    Thread(target=server_udp.listen).start()
    Thread(target=send).start()
    Thread(target=log).start()

def benchmark_tcp():
    def send():
        while True:
            client_tcp.send('ping')
    def log():
        elapsed_time = 1
        while True:
            print(f'TCP - {int(server_tcp.recived/elapsed_time)}/s')
            elapsed_time += 2
            sleep(2)
    Thread(target=server_tcp.listen).start()
    Thread(target=send).start()
    Thread(target=log).start()

benchmark_tcp()
benchmark_udp()