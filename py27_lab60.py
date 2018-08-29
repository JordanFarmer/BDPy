# encoding=UTF-8
import Tkinter
import tkFont

x = 0


def action():
    global x
    label1.config(text='clicked %d times' % x)
    x += 1


top = Tkinter.Tk()

myFont = tkFont.Font(family='Arial', size=30)
label1 = Tkinter.Label(top, text='Hello TK!', bg='#009900', padx=20, pady=10, font=myFont)
button1 = Tkinter.Button(top, text='click', font=myFont, command=action)

label1.pack()
button1.pack()
top.mainloop()