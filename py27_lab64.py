import Tkinter
import tkFont

displayString = 'value=%d'


def func(scale):
    label.config(text=displayString % int(scale))


top = Tkinter.Tk()
myFont = tkFont.Font(family='Arial', size=30)
value = Tkinter.IntVar()
value.set(0)
label = Tkinter.Label(top, text=displayString % value.get(), font=myFont)
label.pack()
scale = Tkinter.Scale(top, label='Volumn', orient='h', from_=0, to=100,
                      showvalue=True, variable=value)
scale.pack()
top.minsize(400, 150)
top.maxsize(400, 150)
top.mainloop()