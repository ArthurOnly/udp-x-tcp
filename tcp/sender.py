import socket
from threading import Thread
from time import sleep

s_tcp = 0
s_udp = 0

def tcp_client():
    global s_tcp

    host = 'localhost'  # as both code is running on same pc
    port = 65432  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = "PING"

    while True:
        client_socket.send(message.encode())
        s_tcp += 1


def udp_client():
    global s_udp
    UDP_IP = "127.0.0.1"
    UDP_PORT = 65433

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

    message = b"PING"

    while True:
        sock.sendto(message, (UDP_IP, UDP_PORT))
        s_udp += 1

def print_s():
    global s_tcp
    global s_udp
    while True:
        print("TCP - Pacotes/s", s_tcp)
        print("UDP - Pacotes/s", s_udp)
        s_tcp = 0
        s_udp = 0
        sleep(1)

if __name__ == '__main__':
    Thread(target=udp_client).start()
    Thread(target=print_s).start()
    tcp_client()