# encoding=UTF-8
import Tkinter
import tkFont

top = Tkinter.Tk()

myFont = tkFont.Font(family='Arial', size=30)
myFont2 = tkFont.Font(family='標楷體', size=30)
myFont3 = tkFont.Font(family='@標楷體', size=30)
for font in tkFont.families():
    print font

label1 = Tkinter.Label(top, text='Hello TK!', bg='#009900', padx=20, pady=10, font=myFont)
label2 = Tkinter.Label(top, text='Hello TKinter!', bg='#000099', fg='#FFFF99', padx=10, pady=20,
                       font=myFont)
label3 = Tkinter.Label(top, text='測試機台', font=myFont2)
label4 = Tkinter.Label(top, text='測試機台', font=myFont3)
label2.pack()
label1.pack()
label3.pack()
label4.pack()
top.mainloop()