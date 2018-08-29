# encoding=UTF-8
import Tkinter
import tkFont

top = Tkinter.Tk()


def motion(event):
    message.config(text='move to:[%d,%d]' % (event.x, event.y))


myFont = tkFont.Font(family='Arial', size=30)

message = Tkinter.Message(top, text='try to move cursor inside')
message.config(bg='#99FF99', font=myFont)
message.bind('<Motion>', motion)
message.pack()
top.minsize(400, 300)
top.maxsize(400, 300)
top.mainloop()