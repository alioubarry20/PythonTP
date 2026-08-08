class Personne:
    def __init__(self,nom,age):
        self.nom = nom
        self.nom = age
        # self.moyenne = moyenne
    
    def __str__(self):
        return f"{self.nom},{self.age}ans"

class Etudiant(Personne):
    def __init__(self, nom, age,moyenne):
        super().__init__(nom, age)
        self.moyenne = moyenne
    
    def __str__(self):
        #super().__str__(self)
        return f"Etudiant: {self.nom},{self.age}ans, Votre moyenne={self.moyenne}"

class Enseignant(Personne):
    def __init__(self, nom, age,matiere):
        super().__init__(nom, age)
        self.matiere = matiere

    def __str__(self):
        #super().__str__(self)
        return f"Enseignant: {self.nom},{self.age}ans, Votre matiere={self.matiere}"
    


etudiant = Etudiant("Aliou",21,15)
# print(Etudiant)

enseignant = Enseignant("Aliou",21,"informatiQUE")
print(enseignant)
# print(Personne) JAMAIS

    

