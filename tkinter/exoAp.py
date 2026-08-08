from tkinter import *

fenetre = Tk()

# Définir la TAILLE de la fenêtre
fenetre.geometry("800x640")

# Définir la COULEUR de la fenêtre
fenetre.config(bg="blue")


label=Label(fenetre, text="saisie des info", font=("Arial", 12), bg="blue")
label.pack()
value = StringVar()
value.set("Entrez  votre nom")
input_field = Entry(fenetre, textvariable=value, width=100, font=("Arial", 20))
input_field.pack()

value.set("Entrez  age")
input_field = Entry(fenetre, textvariable=value, width=100, font=("Arial", 20))
input_field.pack()

input_field.pack()
# un radio box genre hommme femme
genre = StringVar()
radio_homme = Radiobutton(fenetre, text="Homme", variable=genre, value="Homme", bg="blue")
radio_homme.pack()
radio_femme = Radiobutton(fenetre, text="Femme", variable=genre, value="Femme", bg="blue")
radio_femme.pack()
# une liste deroulante de pays
liste = Listbox(fenetre)
liste.insert(1, "senegal")
liste.insert(2, "gongo")
liste.insert(3, "zambie")
liste.insert(4, "cap-vert")
liste.insert(5, "guinee")
liste.pack()
def recup():
    """showInfo("Alert","Nom"+)"""

bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()
fenetre.mainloop()