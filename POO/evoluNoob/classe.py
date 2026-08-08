class Personne:

    def __init__(self,nom,age):
        self.nom = nom
        self.age = age

    def parler(self,message):
        self.message =message
        print(f"{self.nom} a dit {self.message}")

    #property (getter,setter,deleter,helper)
    """"
    age = property(_getage,_setage)
    def _getage(self):
        return self._age
    """

class Chien(Personne):
    def __init__(self, nom, age,race):
        super().__init__(nom, age)
        self.race =race
    

class Chiot(Chien):
    def __init__(self, nom, age, race,poidNaissance):
        Chien.__init__(nom, age, race)
        self.poidNaissance=poidNaissance




h1= Personne("Melo",22)
h1.parler("hi melo fans")

H2= Chien("REX",4,'Berger')
Chien.parler("je sais aboyer")
print(H2.race)