from tkinter import *
from pyalge.alge import *


current_mode = "Alge"


def generate():
    if current_mode == "Alge":
        output.config(text=generate_alge())
    elif current_mode == "Megaalge":
        output.config(text=generate_megaalge())
    elif current_mode == "Farbe":
        output.config(text=generate_colour())


def change_to_alge():
    global current_mode
    current_mode = "Alge"
    output.config(text="Alge")


def change_to_megaalge():
    global current_mode
    current_mode = "Megaalge"
    output.config(text="Megaalge")


def change_to_colour():
    global current_mode
    current_mode = "Farbe"
    output.config(text="Farbe")


window = Tk()
window.geometry("500x200")
window.title("Alge Alge Alge")

output = Label(window, text="Alge")
generate_button = Button(window, text="Generieren", command=generate)

menu = Menu(window)
modes_bar = Menu(menu, tearoff=0)
modes_bar.add_command(label="Alge", command=change_to_alge)
modes_bar.add_command(label="Megaalge-Farbe", command=change_to_megaalge)
modes_bar.add_command(label="Farbe", command=change_to_colour)
modes_bar.add_separator()
modes_bar.add_command(label="Exit", command=window.quit)
menu.add_cascade(label="Starten", menu=modes_bar)
window.config(menu=menu)

output.pack()
generate_button.pack()

window.mainloop()
