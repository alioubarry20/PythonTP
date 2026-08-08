from tkinter import *

fenetre = Tk()
# un label
label = Label(fenetre,text="Hello guys",bg="red",fg="white")
label.pack()

# un entre/input
value = StringVar()
value.set("la cybersecurite est dangereuse")
entree = Entry(fenetre,textvariable="ssss",width=30)
entree.pack()


#checkbutton il propose a UT  de choisir une option
boutton =Checkbutton(fenetre,text="celibataire",width=50)
boutton.pack()

#buttonRadio multiple choix un seul  est selectionner
value = StringVar()
button1 = Radiobutton(fenetre,text="YES",variable=value,value=1)
button2 = Radiobutton(fenetre,text="NO",variable=value,value=2)
button3 = Radiobutton(fenetre,text="May Be",variable=value,value=3)
button1.pack()
button2.pack()
button3.pack()

#liste 
liste =Listbox(fenetre)
liste.insert(1,"Flask")
liste.insert(2,"Diango")
liste.insert(3,"Tkinter")
liste.insert(4,"Streamlit")
liste.pack()

fenetre.mainloop()