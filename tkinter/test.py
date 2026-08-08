from tkinter import *

fenetre = Tk()

# Définir la TAILLE de la fenêtre
fenetre.geometry("800x640")

# Définir la COULEUR de la fenêtre
fenetre.config(bg="blue")

label=Label(fenetre, text="Bonjour Tout le Monde", font=("Arial", 32), bg="blue")
label.pack()

label2=Label(fenetre, text="Supdeco", font=( "Arial", 32), bg="blue")
label2.pack()
# Créer un bouton
btn1= Button(fenetre, text="Fermer", command=fenetre.quit)
btn1.pack()

fenetre.mainloop()


# creer un compteur simple avec tkinter
counter = 0
def increment_counter():
    global counter
    counter += 1
    label_counter.config(text=f"Compteur: {counter}")
btn_increment = Button(fenetre, text="Incrémenter", command=increment_counter)
btn_increment.pack()
label_counter = Label(fenetre, text=f"Compteur: {counter}", font=("Arial", 24), bg="blue")
label_counter.pack()

value = StringVar()
value.set("Texte")
input_field = Entry(fenetre, textvariable=value, width=100, font=("Arial", 20))
input_field.pack()
# case a cocher
case_a_cocher = Checkbutton(fenetre, text="Cochez-moi", bg="blue")
case_a_cocher.pack()
fenetre.mainloop()