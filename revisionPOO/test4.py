class CompteBank:
    def __init__(self,num_compte,nom,solde):
        self.num_compte=num_compte
        self.nom=nom
        self.solde=solde

    def versement(self,somme):
        self.solde+=somme
    def retrait(self,somme):
        if somme>self.solde:
            print("solde insufissant")
        else:
            self.solde-=somme
    
    def agios(self):
        self.solde=self.solde*95/100

newcompt=CompteBank(12345,"ndiaye",2500)
newcompt.agios()
print("le numero est :",newcompt.num_compte)
print("le nom est :",newcompt.nom)
print("le sole est :",newcompt.solde)

# cercle
from math import*
class Cercle:
    def __init__(self,a,b,r):
        self.a=a
        self.b=b
        self.r=r
    
    def permetre(self):
        return 2*pi*self.r
    
    def surface(self):
        return pi*self.r**2
    def testappartenance(self,x,y):
        return (x-self.a)**2 +(y-self.y)**2 == self.r**2
    
c=Cercle(0,0,1)
print("le perimetre est:",c.permetre())
print("la surface est:",c.surface())
print("test appartenance du pointA(0,1):",c.testappartenance(0,1))