"""      class Mammifere:
    def __init__(self):
        self.cri="hello"

    def parle(self):
        print("je sais dire",self.cri)
animal =Mammifere()
print(animal)
animal.cri="haha"
animal.parle()         """

class Mammifere:
    def __init__(self,parole,ans):
        self.cri=parole
        self.age=ans
        self.sexe="H"
        self.aptitude =[]
    def nouvelle_aptitude(self,x):
        self.aptitude.append(x)
        # self.jj="j"
    def afficher_aptitude(self):
        for i in self.afficher_aptitude:
            print("je sais",i)
    # def parle(self):
    #     print("je sais dire",self.cri)
        # print("je suis de sexe ",self.sexe)
    # def pro(self,felling):
        
        # print("je suis de type",self.sexe)
AN=Mammifere("bz",9.3)
AN.nouvelle_aptitude("chier")
AN.nouvelle_aptitude("coccccccccccc")
# AN1=Mammifere("bb",3)
# AN2=Mammifere("bz",9)
# # AN.parle()
# print(AN.age)
# print(AN1.sexe)
print(AN.aptitude)
AN.afficher_aptitude()
