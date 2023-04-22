import random
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkmacosx import Button
from tkinter import Label
import subprocess

# Interface graphique
root = Tk()
root.title("Le Morpion")
root.config(background="#EDEDED")
root.geometry("720x480")

# Constantes
joueur1 = "X"
ia = "0"

# Variables globales
clique = True
count_c = 0
gagne = False

# Les boutons du morpion
btns = []


# Fonction pour vérifier si un joueur a gagné
def check_gagne():
    global gagne
    gagne = False

    # Combinaisons gagnantes
    combinaisons = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # Lignes
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # Colonnes
        [0, 4, 8],
        [2, 4, 6],  # Diagonales
    ]

    for comb in combinaisons:
        if (
            btns[comb[0]]["text"]
            == btns[comb[1]]["text"]
            == btns[comb[2]]["text"]
            == joueur1
        ):
            gagne = True
            messagebox.showinfo("Morpion", "Bravo ! le joueur X a gagné")
            desactiver_autres_boutons()
            break
        elif (
            btns[comb[0]]["text"]
            == btns[comb[1]]["text"]
            == btns[comb[2]]["text"]
            == ia
        ):
            gagne = True
            messagebox.showinfo("Morpion", "Bravo ! le joueur 0 a gagné")
            desactiver_autres_boutons()
            break

    if count_c == 9 and not gagne:
        messagebox.showinfo("Perdu", "Match nul :)")
        desactiver_autres_boutons()


# Fonction pour désactiver les boutons non cliqués
def desactiver_autres_boutons():
    for btn in btns:
        if btn["text"] == " ":
            btn.config(state=DISABLED)


# Fonction pour le tour de l'IA
def IA():
    global clique, count_c

    if not clique and count_c < 9:
        choix = True
        while choix:
            x = random.randint(0, 8)
            if btns[x]["text"] == " ":
                btns[x]["text"] = ia
                choix = False
            Label(
                root,
                text=("Au tour de " + joueur1),
                bg="white",
                font=("Helvetica", 30),
                fg="#41B77F",
            ).grid(row=2, column=3, padx=15)

        clique = True
        count_c += 1
        check_gagne()


# Fonction pour gérer le clic sur un bouton
def clic_sur_bouton(btn):
    global clique, count_c

    if btn["text"] == " " and clique:
        btn["text"] = joueur1
        clique = False
        count_c += 1
        check_gagne()
        Label(
            root,
            text=("Au tour de " + ia),
            bg="white",
            font=("Helvetica", 30),
            fg="#41B77F",
        ).grid(row=2, column=3, padx=15)

        if not gagne and not clique and count_c < 9:
            root.after(1000, IA)


# Fonction pour réinitialiser le jeu
def rejouer():
    global clique, count_c, gagne, btns
    clique = True
    count_c = 0
    gagne = False
    Label(
        root,
        text=("Au tour de " + joueur1),
        bg="white",
        font=("Helvetica", 30),
        fg="#41B77F",
    ).grid(row=2, column=3, padx=15)

    for btn in btns:
        btn.config(state=NORMAL, text=" ")


# Créer les boutons
for i in range(9):
    btn = Button(
        root,
        text=" ",
        font=("Courrier", 50),
        height=120,
        width=120,
        bg="#7A7A7A",
        command=lambda x=i: clic_sur_bouton(btns[x]),
    )
    btns.append(btn)

# Placer les boutons sur la grille
for i in range(3):
    for j in range(3):
        btns[i * 3 + j].grid(row=i + 2, column=j)


# Fonction pour ouvrir le menu principal
def open_menugame():
    subprocess.Popen(["python3", "menu.game.py"])
    root.destroy()


# Titre
Label(
    root,
    text="THE NEW GAME",
    fg="#41B77F",
    bg="white",
    font=("Helvetica", 20),
    width=23,
).grid(row=0, column=3, pady=15, padx=40)

# Tour du joueur
tour_label = Label(
    root,
    text=("Au tour de " + joueur1),
    font=("Helvetica", 30),
    bg="white",
    fg="#41B77F",
)
tour_label.grid(row=2, column=3, padx=15)

# bouton de fontion
Button(root, text="Rejouer", width=10, command=rejouer).grid(
    row=3,
    column=3,
    padx=100,
    pady=30,
    sticky="nsew",
)
Button(root, text="Retour", command=open_menugame).grid(
    row=4,
    column=3,
    padx=100,
    pady=30,
    sticky="nsew",
)
root.mainloop()
