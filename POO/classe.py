class Mamifere:
    def __init__(self,type):
        self.cri ="bonjour"
        # self.age = "ans"
        self.type =type
        

    def parle(self):
        print("je sais dire",self.cri)
        # print("jai 10",self.age)
        print("je suis de type",self.type)
    def ajoutAptitude(self,y):
        self.ajoutAptitude.appeend(y)
    def ajoutAptitude(self,):
        for a in self.ajoutAptitude:
            print(a)
    

animal = Mamifere(type="lion",)
tigre = Mamifere(type="tigre",)
print(animal)
print(tigre)

#appel fr lz methode parle
animal.parle()
animal.cri = "coucouuuu"
animal.cri = "rugissement"
tigre.cri="hhhhh"
animal.parle()
animal.ajoutAptitude("manger")
animal.ajoutAptitude("boire")
animal.ajoutAptitude()
tigre.parle()


