from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

fenetre = Tk()
fenetre.title("Formulaire Étudiant")
fenetre.geometry("300x350")

# Variables
nom_var = StringVar()
age_var = StringVar()
niveau_var = StringVar()
boursier_var = IntVar()

def enregistrer():
    # Récupération des valeurs
    nom = nom_var.get()
    age = age_var.get()
    niveau = niveau_var.get()

    if boursier_var.get() == 1:
        boursier = "Oui"
    else:
        boursier = "Non"

    # Vérification du nom
    if nom == "":
        messagebox.showerror("Erreur", "Le nom ne doit pas être vide.")
        return
    
    # Vérification de l'âge
    if not age.isdigit():
        messagebox.showerror("Erreur", "L'âge doit être un nombre.")
        return

    # Affichage
    texte = f"Nom : {nom}\nAge : {age}\nNiveau : {niveau}\nBoursier : {boursier}"
    label_result.config(text=texte)

    # Sauvegarde dans le fichier
    with open("etudiants.txt", "a") as f:
        f.write(texte + "\n\n")

# Interface 
Label(fenetre, text="Nom :").pack()
Entry(fenetre, textvariable=nom_var).pack()

Label(fenetre, text="Age :").pack()
Entry(fenetre, textvariable=age_var).pack()

Label(fenetre, text="Niveau :").pack()
Combobox(fenetre, values=["L1", "L2", "L3", "M1", "M2"], textvariable=niveau_var).pack()

Checkbutton(fenetre, text="Boursier", variable=boursier_var).pack()

Button(fenetre, text="Enregistrer", command=enregistrer).pack(pady=10)

label_result = Label(fenetre, text="", fg="blue")
label_result.pack(pady=10)

fenetre.mainloop()
