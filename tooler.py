import os
from tkinter import *
import time
from tkinter import messagebox
def self():
    print('Запускаю селф-бота...')
    time.sleep(3)
    os.system('python ./tools/selfbot/main.py')
def crashbot():
    print('Запускаю краш-бота...')
    time.sleep(3)
    os.system('python ./tools/crashbot.py')
def about():
    messagebox.showinfo(title='Tooler', message='Discord Tools by internetmilitarist#5585')
root=Tk()
root.title('TOOLER BY INTERNETMILITARIST')
root.geometry('550x320')
root.configure(background='grey')
selfbot = Button(text='Селф-бот',background='red', command=self, width=10)
selfbot.place(x=10, y=10)
crashbot = Button(text='Краш-бот', background='red', command=crashbot, width=10)
crashbot.place(x=10, y=45)
about = Button(text='About tooler', background='grey', command=about, width=20)
about.place(x=150, y=45)
root.mainloop()