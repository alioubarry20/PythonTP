from tkinter import *

fenetre = Tk()
fenetre.geometry("800x640")
fenetre.config(bg="blue")

value = StringVar()

def getButton(caractere):
    input.insert(END, caractere)

def effacer():
    input.delete(0, END)

# Fonction calculer SANS eval()
def calculer():
    expression = input.get()

    if "+" in expression:
        a, b = expression.split("+")
        resultat = float(a) + float(b)

    elif "-" in expression:
        a, b = expression.split("-")
        resultat = float(a) - float(b)

    elif "*" in expression:
        a, b = expression.split("*")
        resultat = float(a) * float(b)

    elif "/" in expression:
        a, b = expression.split("/")
        if float(b) == 0:
            resultat = "Erreur"
        else:
            resultat = float(a) / float(b)

    else:
        resultat = "Erreur"

    input.delete(0, END)
    input.insert(END, resultat)


label = Label(fenetre, text="Calculatrice", font=("Arial", 20), bg="blue", fg='yellow')
label.pack(pady=10)

input = Entry(fenetre, textvariable=value, width=20, font=("Arial", 28), justify="right")
input.pack(pady=10)

frame = Frame(fenetre, bg="blue")
frame.pack()

# Boutons 1 à 9
i = 1
for ligne in range(3):
    for colonne in range(3):
        Button(frame, text=str(i), width=5, height=2, font=("Arial", 20),
               command=lambda x=i: getButton(str(x))).grid(row=ligne, column=colonne, padx=5, pady=5)
        i += 1

# Bouton 0
Button(frame, text="0", width=5, height=2, font=("Arial", 20),
       command=lambda: getButton("0")).grid(row=3, column=1, padx=5, pady=5)

# Boutons opérateurs
Button(frame, text="+", width=5, height=2, font=("Arial", 20),
       command=lambda: getButton("+")).grid(row=0, column=3)
Button(frame, text="-", width=5, height=2, font=("Arial", 20),
       command=lambda: getButton("-")).grid(row=1, column=3)
Button(frame, text="*", width=5, height=2, font=("Arial", 20),
       command=lambda: getButton("*")).grid(row=2, column=3)
Button(frame, text="/", width=5, height=2, font=("Arial", 20),
       command=lambda: getButton("/")).grid(row=3, column=3)

# Bouton =
Button(frame, text="=", width=5, height=2, font=("Arial", 20),
       command=calculer).grid(row=3, column=2)

# Bouton C
Button(frame, text="C", width=5, height=2, font=("Arial", 20),
       command=effacer).grid(row=3, column=0)

fenetre.mainloop()
