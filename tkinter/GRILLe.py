from tkinter import *
import tkinter as tk
fenetre = tk.Tk()

fenetre.geometry("800x640")
fenetre.config(bg="blue")

val = 0
for ligne in range(5):
    for colonne in range(5):
        val += 1
        h2=Button(fenetre,text=str(val),borderwidth=1,font=('verdana'),fg='white').grid(row=ligne,column=colonne)
        

fenetre.mainloop()