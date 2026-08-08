class Mamifere:
    compteur = 0
    def __init__(self,nom):
        self.nom = nom
        #Mamifere.compteur+=1
        Mamifere.incremente()
        # print(self.nom)
    def afficher(self):
        print(self.nom)

    # methode static propre a py il ne faut pas utiliser les variable d'instance uniquement proprieter du class 
    @staticmethod
    def incremente():
        Mamifere.compteur+=1
# super permet d'afficher les fonction de la classe mere

# le polimorphisme le fait de surcharger 
class chien(Mamifere):
    def __init__(self, nom,race):
        super().__init__(nom)
        self.race=race
    def afficher(self):
        super().afficher()
        print(self.race)
    

m1 = Mamifere("Mamifere")
print(Mamifere.compteur)
m2 = chien("chien","berger allemand")
print(Mamifere.compteur)
m1.afficher()
m2.afficher()