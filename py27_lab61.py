# encoding=UTF-8
import Tkinter
import tkFont


def func1(e):
    label1.config(bg='#FFFF00', text='cursor in', fg='#0000FF')


def func2(e):
    label1.config(bg='#009900', text='cursor out', fg='#000000')


def func3(e):
    label1.config(text='single click', bg='#009999', fg='#000000')

def func4(e):
    label1.config(text='scroll drag', bg='#999900', fg='#666666')
def func5(e):
    label1.config(text='right double click', bg='#990099', fg='#222222')

top = Tkinter.Tk()

myFont = tkFont.Font(family='Arial', size=30)
label1 = Tkinter.Label(top, text='Hello TK!', bg='#009900', fg='#000000', padx=20, pady=10, font=myFont)
button1 = Tkinter.Button(top, text='click', font=myFont, padx=20, pady=20)
# bind event
button1.bind('<Enter>', func1)
button1.bind('<Leave>', func2)
button1.bind('<Button-1>', func3)
button1.bind('<B2-Motion>', func4)
button1.bind('<Double-3>', func5)
# fix UI
label1.pack()
button1.pack()
top.mainloop()