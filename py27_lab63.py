import Tkinter
import tkFont


def func1():
    label.config(text='you choose Android')


def func2():
    label.config(text='you choose iOS')


def func():
    if selector.get() == 1:
        label.config(text='you choose Android')
        pass
    elif selector.get() == 2:
        label.config(text='you choose iOS')
        pass
    else:
        label.config(text='internal error')
        pass


top = Tkinter.Tk()
# def a variable
selector = Tkinter.IntVar()
selector.set(1)
myFont = tkFont.Font(family='Arial', size=30)
label = Tkinter.Label(top, font=myFont, text='your choice is:')
radioButton1 = Tkinter.Radiobutton(top, font=myFont,
                                   text='Android', value=1, variable=selector, command=func)
radioButton2 = Tkinter.Radiobutton(top, font=myFont,
                                   text='iOS', value=2, variable=selector, command=func)
label.pack()
radioButton1.pack()
radioButton2.pack()
top.mainloop()