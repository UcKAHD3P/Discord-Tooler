import os
from tkinter import *
import time
from tkinter import messagebox
import threading
def selfbot():
    print('Запускаю селф-бота...')
    os.system('python ./tools/selfbot/main.py')
def start_selfbot():
    threading.Thread(target=self).start()
def crashbot():
    print('Запускаю краш-бота...')
    os.system('python ./tools/crashbot.py')
def start_crashbot():
    threading.Thread(target=crashbot).start()
def status():
    print('Запускаю DiscordRPC...')
    os.system('python ./tools/discordrpc/status.py')
def start_status():
    threading.Thread(target=status).start()
def about():
    messagebox.showinfo(title='Tooler', message='Discord Tools by internetmilitarist#5585')
root=Tk()
root.title('TOOLER BY INTERNETMILITARIST')
root.geometry('550x320')
root.configure(background='grey')
selfbot = Button(text='Селф-бот',background='red', command=start_selfbot, width=10)
selfbot.place(x=10, y=10)
crashbot = Button(text='Краш-бот', background='red', command=start_crashbot, width=10)
crashbot.place(x=10, y=45)
status = Button(text='DiscordRPC', background='red', command=start_status, width=10)
status.place(x=10, y=85
about = Button(text='About tooler', background='grey', command=about, width=20)
about.place(x=150, y=45)
root.mainloop()
