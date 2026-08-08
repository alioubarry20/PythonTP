class voiture:
    def __init__(self,marque,prix):
        self.marque = marque
        self.prix = prix
    def afficher(self):
        print(f"la voiture de {self.marque} coute {self.prix}")

class mercedes(voiture):
    def __init__(self, marque, prix,couleur):
        super().__init__(marque, prix)
        self.couleur = couleur

    def afficher(self):
        super().afficher()
        print(self.couleur)
#v=voiture("voiture","1520","couleur")
c=mercedes("BMW","15000000","ful-black")
#v.afficher()
c.afficher()
    
    
    
    