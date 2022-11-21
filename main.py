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
        num = 1
        while True:
            client_udp.send(str(num)+";")
            num += 1
    def log():
        elapsed_time = 1
        while True:
            print(f'{elapsed_time} UDP - {int(server_udp.recived/elapsed_time)}/s | unordered: {server_udp.unordered/elapsed_time}/s | last: {server_udp.last}')
            elapsed_time += 2
            sleep(2)
    Thread(target=server_udp.listen).start()
    Thread(target=send).start()
    Thread(target=log).start()

def benchmark_tcp():
    def send():
        num = 1
        while True:
            client_tcp.send_with_connection(str(num)+";")
            num += 1
    def log():
        elapsed_time = 1
        while True:
            print(f'{elapsed_time} TCP - {int(server_tcp.recived/elapsed_time)}/s | unordered: {server_tcp.unordered/elapsed_time}/s | last: {server_tcp.last}')
            elapsed_time += 2
            sleep(2)
    Thread(target=server_tcp.listen).start()
    Thread(target=send).start()
    Thread(target=log).start()

benchmark_tcp()
#benchmark_udp()