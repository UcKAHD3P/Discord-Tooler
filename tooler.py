import os
from tkinter import *
from tkinter import messagebox
import threading
def self1():
    print('Запускаю селф-бота...')
    os.system('python ./tools/selfbot/main.py')
def self2():
    threading.Thread(target=self1).start()
def crashbot1():
    print('Запускаю краш-бота...')
    os.system('python ./tools/crashbot/crashbot.py')
def crashbot2():
    threading.Thread(target=crashbot1).start()
def status1():
    print('Запускаю DiscordRPC...')
    os.system('python ./tools/discordrpc/status.py')
def status2():
    threading.Thread(target=status1).start()
def nuk3r1():
    print("Запускаю D1sk0rd AkkAyHT Ньюkep...")
    os.system('python ./tools/disc0rd-nuk3r/main.py')
def nuk3r2():
    threading.Thread(target=nuk3r1).start()
def obfus1():
    print("Запускаю обфускатор питон...")
    os.system('python ./tools/python_obfuscator.py')
def obfus2():
    threading.Thread(target=obfus1).start()
def about():
    messagebox.showinfo(title='Tooler', message='Discord Tools by internetmilitarist#5585')
root=Tk()
root.title('Discord Tooler v1')
root.geometry('550x320')
root.configure(background='grey')
selfbot = Button(text='Селф-бот',background='red', command=self2, width=10)
selfbot.place(x=10, y=10)
crashbot = Button(text='Краш-бот', background='red', command=crashbot2, width=10)
crashbot.place(x=10, y=45)
status = Button(text='DiscordRPC', background='red', command=status2, width=10)
status.place(x=10, y=85)
obfuscator = Button(text='Python Obfuscator', background='red', command=obfus2, width=15)
obfuscator.place(x=10, y=155)
nuk3r = Button(text='D1sc0rd AkkayHT Nuk3r', background='red', command=nuk3r2, width=20)
nuk3r.place(x=10, y=120)
about = Button(text='About', background='grey', command=about, width=15)
about.place(x=150, y=45)
root.mainloop()