import random
import socket
import os
import getpass
import time

# Important variables
user = getpass.getuser()
s = socket.socket()
server_host = socket.gethostbyname(socket.gethostname())
server_port = 5004
server_address = (server_host, server_port)
bit_size = 999999


# On start of the program
def on_start():
    print("""
██████╗ ██╗   ██╗██╗   ██╗███████╗██████╗ ███████╗███████╗    ██╗   ██╗██████╗ 
██╔══██╗╚██╗ ██╔╝██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝    ██║   ██║╚════██╗
██████╔╝ ╚████╔╝ ██║   ██║█████╗  ██████╔╝███████╗█████╗      ██║   ██║ █████╔╝
██╔═══╝   ╚██╔╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝      ╚██╗ ██╔╝ ╚═══██╗
██║        ██║    ╚████╔╝ ███████╗██║  ██║███████║███████╗     ╚████╔╝ ██████╔╝
╚═╝        ╚═╝     ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝      ╚═══╝  ╚═════╝""")
    print(f"[+] Listening for skids...")


# Bind Server
def bind_server():
    try:
        s.bind(server_address)
        s.listen(1)
    except Exception as binding_error:
        print(f"{binding_error}")
        time.sleep(1)
        bind_server()


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def send_commands(conn, addr):
    while True:
        command = input("izaannoman: ").lower()
        if command == 'exit':
            print(f'Closing connection with {addr}...')
            conn.send(command.encode())
            s.close()
            conn.close()
            break
        else:
            print(f'No such command as "{command}".')


def main():
    on_start()
    bind_server()
    conn, addr = s.accept()
    print(f"{addr} has been pwned.")
    send_commands(conn, addr)


main()
