import socket
import os
import getpass

# Important Variables
import time

user = getpass.getuser()
s = socket.socket()
host = "192.168.1.179"
port = 5004
server_address = (host, port)
buf_size = 999999


def connect_to_server():
    connected = False
    while not connected:
        try:
            s.connect(server_address)
            connected = True
            receive_commands()
        except socket.error:
            pass


def receive_commands():
    while True:
        command = s.recv(buf_size).decode().lower()
        print(command)
        if command == 'exit':
            s.close()
            print('closed connection')
            connect_to_server()
        else:
            print(command)


def main():
    connect_to_server()


main()
