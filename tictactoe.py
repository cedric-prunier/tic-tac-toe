from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkmacosx import Button
from tkinter import Label
import subprocess

gagne = True
clique = True


root = Tk()
root.title("Le Morpion")
root.config(background="#EDEDED")
root.geometry("720x480")
clique = True
count_c = 0


def open_menugame():
    subprocess.Popen(["python3", "menu.game.py"])
    root.destroy()


def disactive_autre_bouton():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)


gagne = True
joueur1 = "X"
joueur2 = "0"


def checkGagne():
    global gagne

    if (
        btn1["text"] == "X"
        and btn2["text"] == "X"
        and btn3["text"] == "X"
        or btn4["text"] == "X"
        and btn5["text"] == "X"
        and btn6["text"] == "X"
        or btn7["text"] == "X"
        and btn8["text"] == "X"
        and btn9["text"] == "X"
        or btn1["text"] == "X"
        and btn4["text"] == "X"
        and btn7["text"] == "X"
        or btn2["text"] == "X"
        and btn5["text"] == "X"
        and btn8["text"] == "X"
        or btn3["text"] == "X"
        and btn6["text"] == "X"
        and btn9["text"] == "X"
        or btn1["text"] == "X"
        and btn5["text"] == "X"
        and btn9["text"] == "X"
        or btn3["text"] == "X"
        and btn5["text"] == "X"
        and btn7["text"] == "X"
    ):
        gagne = True
        messagebox.showinfo("Morpion", "Bravo ! le joueur X a gagné")
        disactive_autre_bouton()

    elif (
        btn1["text"] == "0"
        and btn2["text"] == "0"
        and btn3["text"] == "0"
        or btn4["text"] == "0"
        and btn5["text"] == "0"
        and btn6["text"] == "0"
        or btn7["text"] == "0"
        and btn8["text"] == "0"
        and btn9["text"] == "0"
        or btn1["text"] == "0"
        and btn4["text"] == "0"
        and btn7["text"] == "0"
        or btn2["text"] == "0"
        and btn5["text"] == "0"
        and btn8["text"] == "0"
        or btn3["text"] == "0"
        and btn6["text"] == "0"
        and btn9["text"] == "0"
        or btn1["text"] == "0"
        and btn5["text"] == "0"
        and btn9["text"] == "0"
        or btn3["text"] == "0"
        and btn5["text"] == "0"
        and btn7["text"] == "0"
    ):
        gagne = True
        messagebox.showinfo("Morpion", "Bravo ! le joueur 0 a gagné")
        disactive_autre_bouton()

    elif count_c == 9 or gagne == False:
        # mettre que 2 arguments max pour showinfo !!!!!
        messagebox.showinfo("Perdu", "Match nul :)")
        disactive_autre_bouton()
    else:
        None


label = Label(
    root,
    text="THE NEW GAME",
    fg="#41B77F",
    bg="white",
    font=("Helvetica", 20),
    width=23,
).grid(row=0, column=3, pady=15, padx=40)

label = Label(
    root,
    text=("Au tour de " + joueur1),
    font=("Helvetica", 30),
    bg="white",
    fg="#41B77F",
).grid(row=2, column=3)


def Button_click(b):
    global clique, count_c
    if b["text"] == " " and clique == True:
        b["text"] = "X"
        clique = False
        count_c += 1
        checkGagne()
        Label(
            root,
            text=("Au tour de " + joueur2),
            bg="white",
            font=("Helvetica", 30),
            fg="#41B77F",
        ).grid(row=2, column=3, padx=15)

    elif b["text"] == " " and clique == False:
        b["text"] = "0"
        clique = True
        count_c += 1
        checkGagne()
        Label(
            root,
            text=("Au tour de " + joueur1),
            bg="white",
            font=("Helvetica", 30),
            fg="#41B77F",
        ).grid(row=2, column=3, padx=15)


def rejouer():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    global clique, count_c
    clique = True
    count_c = 0
    Label(
        root,
        text=("Au tour de " + joueur1),
        bg="white",
        font=("Helvetica", 30),
        fg="#41B77F",
    ).grid(row=2, column=3, padx=15)

    btn1 = Button(
        root,
        text=" ",
        font=("Courrier", 50),
        height=120,
        width=120,
        bg="#7A7A7A",
        command=lambda: Button_click(btn1),
    )
    btn2 = Button(
        root,
        text=" ",
        font=("Courrier", 50),
        height=120,
        width=120,
        bg="#7A7A7A",
        command=lambda: Button_click(btn2),
    )
    btn3 = Button(
        root,
        text=" ",
        font=("Courrier", 50),
        height=120,
        width=120,
        bg="#7A7A7A",
        command=lambda: Button_click(btn3),
    )
    btn4 = Button(
        root,
        text=" ",
        font=("Courrier", 50),
        height=120,
        width=120,
        bg="#7A7A7A",
        command=lambda: Button_click(btn4),
    )
    btn5 = Button(
        root,
        text=" ",
        font=("Courrier", 50),
        height=120,
        width=120,
        bg="#7A7A7A",
        command=lambda: Button_click(btn5),
    )
    btn6 = Button(
        root,
        text=" ",
        font=("Courrier", 50),
        height=120,
        width=120,
        bg="#7A7A7A",
        command=lambda: Button_click(btn6),
    )
    btn7 = Button(
        root,
        text=" ",
        font=("Courrier", 50),
        height=120,
        width=120,
        bg="#7A7A7A",
        command=lambda: Button_click(btn7),
    )
    btn8 = Button(
        root,
        text=" ",
        font=("Courrier", 50),
        height=120,
        width=120,
        bg="#7A7A7A",
        command=lambda: Button_click(btn8),
    )
    btn9 = Button(
        root,
        text=" ",
        font=("Courrier", 50),
        height=120,
        width=120,
        bg="#7A7A7A",
        command=lambda: Button_click(btn9),
    )
    btn1.grid(row=2, column=0)
    btn2.grid(row=2, column=1)
    btn3.grid(row=2, column=2)

    btn4.grid(row=3, column=0)
    btn5.grid(row=3, column=1)
    btn6.grid(row=3, column=2)

    btn7.grid(row=4, column=0)
    btn8.grid(row=4, column=1)
    btn9.grid(row=4, column=2)


# bouton de fontion
Button(root, text="Rejouer", width=10, command=rejouer).grid(
    row=3,
    column=3,
    padx=100,
    pady=30,
    sticky="nsew",  # Nouvelle rangée pour le bouton "Recommencer"
)
Button(root, text="Retour", command=open_menugame).grid(
    row=4,
    column=3,
    padx=100,
    pady=30,
    sticky="nsew",  # Nouvelle colonne pour le bouton "Fermer"
)

rejouer()
root.mainloop()
