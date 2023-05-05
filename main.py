from tkinter import *
print("akujens  pakeitimas")
def mygtuko_veiksmas():

    print( field.get() )

    lbl.config( text = "Vardas: " + field.get() )

def antro_mygtuko_veiksmas():
    lbl = Label( window, text="Naujas tekstas " )
    lbl.pack()


window = Tk()
window.geometry( "300x400" )


lbl = Label( window, text="Vardas: " )
field = Entry( window )


btn = Button(window, text="Pridėti studentą", command=mygtuko_veiksmas )
btn2 = Button( window, text="Pridėti naują tekstą", command=antro_mygtuko_veiksmas)


lbl.pack()
field.pack()
btn.pack()
btn2.pack()


window.mainloop()
