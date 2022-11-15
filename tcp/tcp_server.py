# echo-server.py

import socket
from threading import Thread
from time import sleep

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
rec = 0
time = 0

def pass_minute():
    global time
    global rec
    while True:
        rec = 0
        #time += 1
        sleep(1)
        print("TCP - Pacotes/s", rec)
        

Thread(target=pass_minute).start()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            rec+=1