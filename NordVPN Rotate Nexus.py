import sys
import os
import subprocess
from time import sleep as wait
import datetime


nordpath = 'C:/Program Files/NordVPN'
inpute = ['nordvpn', '-c']

class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[0;94m'
   GREEN = '\033[0;92m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'
   MAGENTA = '\033[0;95m'
   WHITE = '\033[0;97m'



os.system("cls")
print('\n')
print('                                     ' + color.MAGENTA + '███╗   ██╗' + color.BLUE + '███████╗' + color.WHITE + '██╗  ██╗' + color.BLUE + '██╗   ██╗' + color.MAGENTA + '███████╗')
print('                                     ' + color.MAGENTA + '████╗  ██║' + color.BLUE + '██╔════╝' + color.WHITE + '╚██╗██╔╝' + color.BLUE + '██║   ██║' + color.MAGENTA + '██╔════╝')
print('                                     ' + color.MAGENTA + '██╔██╗ ██║' + color.BLUE + '█████╗  ' + color.WHITE + ' ╚███╔╝ ' + color.BLUE + '██║   ██║' + color.MAGENTA + '███████╗')
print('                                     ' + color.MAGENTA + '██║╚██╗██║' + color.BLUE + '██╔══╝  ' + color.WHITE + ' ██╔██╗ ' + color.BLUE + '██║   ██║' + color.MAGENTA + '╚════██║')
print('                                     ' + color.MAGENTA + '██║ ╚████║' + color.BLUE + '███████╗' + color.WHITE + '██╔╝ ██╗' + color.BLUE + '╚██████╔╝' + color.MAGENTA + '███████║')
print('                                     ' + color.MAGENTA + '╚═╝  ╚═══╝' + color.BLUE + '╚══════╝' + color.WHITE + '╚═╝  ╚═╝' + color.BLUE + ' ╚═════╝ ' + color.MAGENTA + '╚══════╝')
print(color.YELLOW + 'Nexus NordVPN Rotate'.center(118))
print(color.RED + 'by Neexuus_#1337\n'.center(118) + color.WHITE)

time = input(color.CYAN + " [~] How much time between changes (seconds)? -> ")

if(time == ''):
    print(color.RED + " [!] You didn't set a specific time, using default 180s (3 minutes)")
    time = 180
elif not time.isdigit():
    print(color.RED + " [!] You specified invalid time, using default 180s (3 minutes)")
    time = 180


firstconn = subprocess.Popen(inpute, shell=True, cwd=nordpath)
firstconn.wait()
print(color.WHITE + f' [!] Please wait {time} seconds for next connection ;)\n')



def conn():
    now = datetime.datetime.now()
    print(color.GREEN + " [{}:{}:{}] Connecting to optimal server...".format(now.hour, now.minute, now.second))
    new_connection = subprocess.Popen(inpute, shell=True, cwd=nordpath)
    new_connection.wait()
    



while True:
    wait(int(time))
    conn()