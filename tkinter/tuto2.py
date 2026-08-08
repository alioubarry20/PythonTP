from tkinter import*

#creation winbd
fenetre= Tk()
fenetre.title("Generateur de mots de passe")
fenetre.geometry("720x480")
fenetre.config(background="#4054A4")

#img avec canva
width = 300
height= 300
image = PhotoImage(file="hacker.png").zoom(35).subsample(32)
canvas = Canvas(fenetre,width=width,height=height,bg="#4054A4")
canvas.create_image(width/2,height/2,image=image)
canvas.pack(expand=YES)


fenetre.mainloop()