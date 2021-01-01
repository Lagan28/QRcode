#install pyqrcode

#import libraries
import pyqrcode
import tkinter
from tkinter import *

#function to generate qr code using pyqrcode
def generate():
    if len(imp_data_enter.get())!=0:
        global qrcode,img
        qrcode=pyqrcode.create(imp_data_enter.get())
        img=BitmapImage(data=qrcode.xbm(scale=5))
    else:
        messagebox.showinfo('Invalid or empty entry!')
    try:
        qrcode_img()
    except:
        pass

#function to preview the generated qr code
def qrcode_img():
    imagelabel.config(image=img)


#Basic GUI created using tkinter

window = tkinter.Tk()

window.title("QRCODE Generator")

data=Label(window,text='Enter the data: ')

imp_data=StringVar()

imp_data_enter=Entry(window,textvariable=imp_data)
imp_data_enter.grid(row=0,column=1)

btn=Button(window,text="Generate",width=10,command=generate)
btn.grid(row=0,column=2)

imagelabel=Label(window)
imagelabel.grid(row=2,column=1)

sublabel=Label(window,text="")
sublabel.grid(row=3,column=1)

window.mainloop()
