import sys 
try:
    File =open("Myfile.txt")
except IOError as e:
    print("Erreur lors de l'ouverture du fichier \r\n" + 
          "Numero de l'erreur : {0}\r\n".format(e.errno)+
          "Texte de l'erreur: {0}".format(e.strerror))
    
else:
    print("le fichier a bien ete ouvert.\n")
    File.close()


# Exemple 2


try:
    File= open("File.txt")
except IOError as e :
    for agr in e.args:
        print(agr)

else:
    print("le fichier a ete ouvert")
    File.close()
#agrs propriete qui contient tjrs des arguments d'exception en STR


# Exemple 3 appeler nom et valeur des arguments
"""""
try:
    File = open("File2.txt")
except IOError as e :
    for Entry in dir(e):
        if (not Entry.startswith("_")):
        try:
            print(Entry,"=",.e__getattribute__(Entry))
        except AttributeError:
            print("Attribut",Entry,"Non accessible.")

else:
    print("Le fichier a bien été ouvert.")
    File.close()

    
"""