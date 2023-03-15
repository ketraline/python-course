from tkinter import *

 # 1

window = Tk()
window.title("Logowanie")

def sprawdz():
    pin = "1234"
    mojpin = polepin.get()

    if pin == mojpin:
        komunikat.config(text = "PIN poprawny", fg = "blue")
    else:
        komunikat.config(text = "PIN błędny", fg = "red")

#2

nazwa = Label(window, text = "Logowanie do banku",
            font = ("Arial", 18),
            padx = 8, pady = 8,
            bg = "white"
            )
podajpin = Label(window, text = "Podaj swój PIN", pady = 5)
polepin = Entry(window)
dostep = Label(window, text = "Dostęp", pady = 5)
komunikat = Label(window, text = "Zablokowany", pady = 5, fg = "red")
przycisk = Button(window, text = "Sprawdź PIN", bg = "lightgrey", width = 28)

#3
nazwa.grid(row = 0, column = 0, columnspan = 2)
podajpin.grid(row = 1, column = 0)
polepin.grid(row = 1, column = 1)
dostep.grid(row = 2, column = 0)
komunikat.grid(row = 2, column = 1)
przycisk.grid(row = 3, column = 0, columnspan = 2)

#4

window.mainloop()
