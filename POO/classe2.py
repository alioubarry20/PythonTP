class personne:
    def __init__(self,nom,prenom,age):# object avec ses attributs 
        self.nom = nom
        self.prenom= prenom
        self.age = age
    def __str__(self):# methode 
        return "je suis un animal"
    def afficher(self):# methode 
        print("nom: ",self.nom)
        print("prenom: ",self.prenom)
        print("age",self.age)
p1 =personne("Dop","messi",45) # instanciation de la classe 
p1.afficher()
print(p1)

    
        