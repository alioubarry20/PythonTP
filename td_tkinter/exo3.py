from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import pygame

# --- Fenêtre ---
fen = Tk()
fen.title("Galerie d'images")
fen.geometry("500x500")

# --- Initialisation du son ---
pygame.mixer.init()

# Liste des images du dossier images/
liste_images = ["photo1.jpg", "photo2.jpg", "photo3.png"]

# Variable pour la liste déroulante
image_choisie = StringVar()

# Label pour afficher l'image
zone_image = Label(fen)
zone_image.pack(pady=10)

# --- Fonction pour afficher l’image ---
def afficher_image():
    fichier = image_choisie.get()
    chemin = "images/" + fichier

    try:
        img = Image.open(chemin)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)

        zone_image.config(image=img_tk, text="")
        zone_image.image = img_tk

    except:
        zone_image.config(text="Erreur : image introuvable", image="")

# --- Fonction pour jouer le son ---
def jouer_son():
    pygame.mixer.music.load("clic.wav")
    pygame.mixer.music.play()

# --- Interface ---
Label(fen, text="Choisir une image :").pack()

Combobox(fen, values=liste_images, textvariable=image_choisie).pack()

Button(fen, text="Afficher", command=afficher_image).pack(pady=10)
Button(fen, text="Jouer un son", command=jouer_son).pack(pady=10)

fen.mainloop()
