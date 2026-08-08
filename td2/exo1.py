nom = input("Entrez un Nom: ")
age =int(input("Entrez un age :"))
moy =float(input("Entrez la moyenne : "))

# print("Bonjour",nom, "tu as ",age,"ans","et ta moyenne est",moy)    affichage obsolette
# affichage personaliser 
print(f"Bonjour {nom}, tu as {age}ans et ta moyenne est {moy}.")

if moy >= 10:
    print("Tu es admis Felicitation\n")
else:
    print("Tu es ajourné\n")