
""""
try:
    NBR= int (input("Entrez un nombre entre 1 et 10:"))
except(ValueError,KeyboardInterrupt):
    print("Tapez un nombre entre 1 & 10")
else:
    if (NBR > 0) and (NBR<=10):
        print("Vous avez tapé:",NBR)
    else:
        print("LA valeur tapee est incorret")
        """

try:
    NBR= int (input("Entrez un nombre entre 1 et 10:"))
except ValueError:
    print("Tapez un nombre entre 1 & 10")
except KeyboardInterrupt:
    print("Clt + c ")
else:
    if (NBR > 0) and (NBR<=10):
        print("Vous avez tapé:",NBR)
    else:
        print("LA valeur tapee est incorret")