from tkinter import *

fenetre = Tk()

# Définir la TAILLE de la fenêtre
fenetre.geometry("800x640")
fenetre.config(bg="blue")

def getButton(caractere):
    Entry().insert

label=Label(fenetre, text="Calculatrice", font=("Arial", 12), bg="blue",fg='yellow')
label.pack()
input = Entry(fenetre, textvariable=value, width=100, font=("Arial", 20))
input.pack()
value = StringVar()


i = 0
for ligne in range(3):
    for colonne in range(3):
        #i += 1

        Button(fenetre,text='0',borderwidth=1,font=('verdana'),fg='red').grid(row=0,column=4)
        Button(fenetre,text='%s'%(i+1),borderwidth=1,font=('verdana'),fg='red').grid(row=ligne+1,column=colonne)
        i+=1
        Button(fenetre,text='%',borderwidth=1,font=('verdana'),fg='red',command=div).grid(row=0,column=4)
        Button(fenetre,text='*',borderwidth=1,font=('verdana'),fg='red').grid(row=1,column=4)
        Button(fenetre,text='-',borderwidth=1,font=('verdana'),fg='red').grid(row=2,column=4)
        Button(fenetre,text='+',borderwidth=1,font=('verdana'),fg='red').grid(row=3,column=4)
        Button(fenetre,text='=',borderwidth=1,font=('verdana'),fg='red').grid(row=4,column=4)

fenetre.mainloop()