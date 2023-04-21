from tkinter import *
import subprocess


def open_menugame():
    subprocess.Popen(["python3", "menu.game.py"])
    window.destroy()


# créer une première fenetre
window = Tk()

# personnaliser la fenetre
window.title("Tic Tac Toe")
window.geometry("720x480")
window.minsize(720, 480)
window.config(background="#41B77F")

# créer une frame
frame = Frame(window, bg="#41B77F")

# Ajouter un premier texte
label_title = Label(
    frame,
    text="Bienvenu sur Tic Tac Toe :)",
    font=("Courrier", 60),
    bg="#41B77F",
    fg="white",
)
label_title.pack()

# Ajouter un second texte
label_subtitle = Label(
    frame,
    text="Ready pour une nouvelle partie ?!",
    font=("Courrier", 40),
    bg="#41B77F",
    fg="white",
)
label_subtitle.pack()

# Ajouter un premier bouton
entry_button = Button(
    frame,
    text="Accéder au jeu",
    font=("Courrier", 25),
    bg="white",
    fg="#41B77F",
    width=30,
    command=open_menugame,
)
entry_button.pack(pady=25)

sortie_button = Button(
    frame,
    text="Quitter",
    font=("Courrier", 25),
    bg="white",
    fg="#41B77F",
    width=30,
    command=window.quit,
)
sortie_button.pack(pady=25)


# Ajouter la frame à la fenêtre
frame.pack(expand=YES)

# Afficher la fenêtre
window.mainloop()
