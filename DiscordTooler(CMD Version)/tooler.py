from colorama import Fore, init
import os
init()
def nuk3r():
    os.system('python ./tools/disc0rd-nuk3r/main.py')
def self():
    os.system('python ./tools/selfbot/main.py')
def crashbot():
    os.system('python ./tools/crashbot/crashbot.py')
def discordrpc():
    os.system('python ./tools/discordrpc/status.py')
def obfus():
    os.system('python ./tools/python_obfuscator.py')
def about():
    print(Fore.RED + "Discord Tools by internetmilitarist#5585")
print(f'''
{Fore.MAGENTA}[ 1 ] D1sk0rd AkkayHT Nuk3r
[ 2 ] Селф-бот
[ 3 ] Краш-бот
[ 4 ] DiscordRPC
[ 5 ] Python Obfuscator
[ 6 ] О туллере{Fore.RESET}''')
choice = input('[ ? ] Выбери что ты хочешь запустить >>> ')
if choice == '1':
    nuk3r()
elif choice == '2':
    self()
elif choice == '3':
    crashbot()
elif choice == '4':
    discordrpc()
elif choice == '5':
    obfus()
elif choice == '6':
    about()
else:
    print('Такого варианта нету!')
input()