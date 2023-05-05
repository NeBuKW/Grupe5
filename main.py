import tkinter as tk
from PIL import Image, ImageTk


def mygtuko_veiksmas():

    print( field.get() )

    lbl.config( text = "Vardas: " + field.get() )

def antro_mygtuko_veiksmas():
    lbl = tk.Label(window, text="Naujas tekstas ")
    lbl.pack()

def knopkute():
    nuotrauka = Image.open("bobute.jpg")
    photo = ImageTk.PhotoImage(nuotrauka)
    label = tk.Label(image=photo)
    label.image = photo
    label.pack()



window = tk.Tk()
window.geometry( "300x400" )


lbl = tk.Label(window, text="Vardas: ")
field = tk.Entry(window)


btn = tk.Button(window, text="Pridėti studentą", command=mygtuko_veiksmas)
btn2 = tk.Button(window, text="Pridėti naują tekstą", command=antro_mygtuko_veiksmas)
knopke = tk.Button(window, text="Paspausk Knopkutę, išlys Bobutė", command=knopkute)


lbl.pack()
field.pack()
btn.pack()
btn2.pack()
knopke.pack()


window.mainloop()
