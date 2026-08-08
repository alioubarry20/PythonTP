def max(liste):
    max_val =liste[0]
    for i in liste:
        if x > max_val:
            x= max_val
    return max_val
print(max([5,1,85,3,4]))

# afficher les produit >10

produit =[
    {"nom":"pain","prix":150},
    {"nom":"mayo","prix":50},
    {"nom":"lait","prix":200}
]
for p in produit:
    if p["prix"]>100:
        print(p["nom"],p["prix"])

class Voiture:
    def __init__(self,marque,v):
        self.marque=marque
        self.v=v

    def __str__(self):
        return f"la voiture de {self.marque}roule a une vitesse de {self.v}"

class Animal:
    def __init__(self,nom):
        self.nom= nom

    def __str__(self):
        f"Animal: {self.nom}"

class Chien(Animal):
    def __init__(self, nom,race):
        super().__init__(nom)
        self.race=race
    def __str__(self):
        return f"Chien:{self.nom},race{self.race}"
A1 = Animal("giraf")
print(A1)
rex =Chien("boby","bull-dog")
print(rex)
    