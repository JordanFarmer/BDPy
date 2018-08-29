import Tkinter
import tkFont

def display(event):
    label1.config(text=entry.get())

top = Tkinter.Tk()
myFont = tkFont.Font(family='Arial', size=30)

label1 = Tkinter.Label(top, font=myFont, text='your input will be')
label1.pack()

entry = Tkinter.Entry(top, font=myFont)
entry.pack()
entry.bind('<Return>', display)

button = Tkinter.Button(top, font=myFont, text='submit')
button.pack()
button.bind('<Button-1>', display)

top.mainloop()