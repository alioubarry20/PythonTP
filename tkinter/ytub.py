from tkinter import *
fenetre =Tk()
fenetre.geometry('400x400')
fenetre.title('melo')
fenetre['bg']='red'
fenetre.resizable(height=False,width=False)
def bnjr():
    print("Venez manger")
label=Label(fenetre,text='Abonnez vous',font=('verdana',20),fg="white",bg="red")
label.pack()
label=Label(fenetre,text='Laissez un like!',font=('verdana',20),fg="white",bg="red")
label.pack()
bt=Button(fenetre,text='click me',font=('arial',20),bg='pink',fg='red',command=bnjr).pack()


def function():
    label['text']= maVar.get()
maVar =StringVar()

label =Label(fenetre,text='Texte modifier')
label.pack()

entree =Entry(fenetre,textvariable=maVar)
entree.pack()

Button=Button(fenetre,text='Arigato',padx=5,command=function)
Button.pack()
fenetre.mainloop()