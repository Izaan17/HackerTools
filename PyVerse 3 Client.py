import socket
import os
import subprocess
import threading
import time

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 5004
buffsize = 1024


def connect_to_sock():
    while 1:
        try:
            s.connect((host, port))
            break
        except socket.error:
            time.sleep(5)
            continue


connect_to_sock()


while 1:
    command = s.recv(buffsize).decode()
    print(command)