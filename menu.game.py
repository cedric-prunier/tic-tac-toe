from tkinter import *
import subprocess


def open_tictactoe():
    subprocess.Popen(["python3", "tictactoe.py"])
    window1.destroy()


def open_ia():
    subprocess.Popen(["python3", "ia.py"])
    window1.destroy()


def open_accueil():
    subprocess.Popen(["python3", "accueil.py"])
    window1.destroy()


# créer une première fenetre
window1 = Tk()

# personnaliser la fenetre
window1.title("Tic Tac Toe")
window1.geometry("720x480")
window1.minsize(720, 480)
window1.iconbitmap("logo.ico")
window1.config(background="#41B77F")


# créer une frame
frame = Frame(window1, bg="#41B77F")

# créer une image
width = 200
height = 200
image = PhotoImage(file="morpion.png").zoom(12).subsample(32)
canvas = Canvas(
    frame, width=width, height=height, bg="#41B77F", bd=0, highlightthickness=0
)
canvas.create_image(width / 2, height / 2, image=image)
canvas.pack()

label = Label(frame, bg="#41B77F", fg="white", pady=2)
label.pack()

# Ajouter un premier bouton
multijoueur = Button(
    frame,
    text="Mode 2 joueurs",
    font=("Courrier", 25),
    bg="white",
    fg="#41B77F",
    pady=10,
    command=open_tictactoe,
)
multijoueur.pack()

label = Label(
    frame, text="OU", bg="#41B77F", fg="white", font=("Helvetica", 30), pady=10
)
label.pack()

vs_ia = Button(
    frame,
    text="Mode vs IA",
    font=("Courrier", 25),
    bg="white",
    fg="#41B77F",
    pady=10,
    command=open_ia,
)
vs_ia.pack()

button_return = Button(
    text="Retour", font=("Courrier", 25), bg="white", fg="#41B77F", command=open_accueil
)
button_return.pack()
# Ajouter la frame à la fenêtre
frame.pack(expand=YES)

window1.mainloop()
