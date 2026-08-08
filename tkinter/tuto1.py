from tkinter import*
import webbrowser


def openYoutube():
    webbrowser.open_new("https://youtube.com")

#creer une premier fenetre

fenetre =Tk()

#personaliser cette fenetre
fenetre.title("My Appli")
fenetre.geometry("720x360")
fenetre.maxsize(480,360)
fenetre.iconbitmap()# ajouter juste un logo
fenetre.config(bg="#41B77F")

# cree la boite
frame =Frame(fenetre,bg="#41B77F",)#bd=1,relief=SUNKEN  pour voir le frame
# ajout un text
label_title=Label(frame,text="Bienvenue sur l'aapli",font=("Courrier",30),background="#41B77F",fg="white")
label_title.pack()


#ajout dun second test
label_subtitle=Label(frame,text="hey salut cest MELO",font=("Courrier",20),background="#41B77F",fg="white")
label_subtitle.pack(pady=25,fill=X)

#boutton 1

button =Button(frame,text="Ouvrir Youtube",font=("Courrier",25),background="white",fg="#41B77F",command=openYoutube)
button.pack()
#ajouter et enpacter le frame
frame.pack(expand=YES)



fenetre.mainloop()