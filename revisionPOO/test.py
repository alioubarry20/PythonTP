class Animmal:
    pass
Lion =Animmal()
Lion.couleur= "blanc"
Lion.fourure= "lisse"
chat =Animmal()
chat.nb_patte=4

# init

class Personne:
    def __init__(self,nom,prenom,age):
        self.nom =nom
        self.nom =prenom
        self.nom =age

    def __str__(self):
        return f"Bonjour{self.nom}"

p =Personne("messi","leo",38)
print(p.nom)
print(p.prenom)


class Rectangle:
    def __init__(self,long,larg):
        self.long = long
        self.larg = larg
        self.surface = long * larg

r=Rectangle(4,6)
print(r.surface) #24

class Chien:
    def __init__(self,nom):
        self.nom=nom

    def aboyer(self):
        return f"{self.nom} aboie!"
    
c=Chien("sity")
c.aboyer()


class Compte:
    def __init__(self,solde,):
        self.solde =solde

    def deposer(self,montant):
        self.montant=montant
        self.solde += self.montant
    def __str__(self):
        return f"{self.solde}et le monztnt est{self.montant}"
c = Compte(100)
c.deposer(200)
print(c.solde)




# str
class Musique:
    def __init__(self,titre,auteur,disq):
        self.titre=titre
        self.auteur=auteur
        self.disq=disq
    
    def __str__(self):
        return f"{self.titre}chanter par{self.auteur}est certifer disq{self.disq}"
    

song =Musique("melo","Tiakola","Platine")
song.disq="Diamant"
print(song)


class Mamifere:
    def __init__(self,parole,age):
        self.cri= parole
        self.age=age
        self.apti=[]
    

    def new_apt(self,x):
        self.apti.append(x)
    
    def afficher_apti(self):
        for i in self.apti:
            print("je sais",i)

a= Mamifere("hahha",15)
a.new_apt("bz")
a.new_apt("lover")
print(a.apti)
a.afficher_apti()




class CompteBancaire:
    def __init__(self,nom,solde):
        self.nom=nom
        self.solde=float(solde)

    def deposer(self,montant):
        
        if montant>0:
            self.solde+=montant
        else:
            print("Le montant doit etre positif")
        
    def retirer(self,montant):
        if montant<self.solde:
            self.solde-=montant
        else:
            f"Solde insuffisant"

    def __str__(self):
        return f"Compte de {self.nom} | Solde: {self.montant} FCFA "

    def __add__(self,other):
        return CompteBancaire("Fusion",self.solde + other.solde)


 
# CompteBancaire 
compte1 = CompteBancaire("Mamadou", 50000) 
compte2 = CompteBancaire("Awa", 30000) 
 
compte1.deposer(10000) 
compte2.retirer(5000) 
 
print(compte1)  # Compte de Mamadou | Solde: 60000 FCFA 
print(compte2)  # Compte de Awa | Solde: 25000 FCFA 
 
compteFusion = compte1 + compte2 
print(compteFusion)  # Fusion de Mamadou et Awa | Solde: 85000 FCFA 
        
    
    