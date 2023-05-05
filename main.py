from tkinter import *
import tkinter as tk
import os

def mygtuko_veiksmas():

    print( field.get() )

    lbl.config( text = "Vardelis: " + field.get() )

def antro_mygtuko_veiksmas():
    lbl = Label( window, text="Naujas tekstas " )
    lbl.pack()

def shutdown():
    def shutdown():
        os.system("shutdown /s /t 1")

window = Tk()
window.geometry( "300x400" )


lbl = Label( window, text="Vardelis: " )
field = Entry( window )


btn = Button(window, text="Pridėti studentą", command=mygtuko_veiksmas )
btn2 = Button( window, text="Pridėti naują tekstą", command=antro_mygtuko_veiksmas)
btn3 = tk.Button(window, text="NESPAUSK!!!", command=shutdown)

lbl.pack()
field.pack()
btn.pack()
btn2.pack()
btn3.pack()


window.mainloop()
