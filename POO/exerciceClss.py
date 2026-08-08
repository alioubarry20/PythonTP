class Voiture:


    # __init__ une methode appelée automatiquement qd on cree une instance
    def __init__(self,p_couleur,p_marque,v=0):
        self.couleur = p_couleur # attribut
        self.marque = p_marque # attribut*
        self.vitesse = v # attribut

     #methode
    def accelerer(self,p_vitesse):
        self.vitesse += p_vitesse
     
     #methode
    def freiner(self,p_vitesse):
        self.vitesse -= p_vitesse
        if self.vitesse <0:
            self.vitesse =  0

    #__str__ defini comment l'object s'affiche quand on fait une print()
    def __str__(self):
        return f"La voiture de {self.couleur}et de marque {self.marque}"
    

    """""
    exemple surchage d'operateur
    ==  __eq__
    <  __lt___
    >  __gt__ 
    != __ne__
    exple : def __lt__(self,other):
                return self.score < other.score


     NB:
     isinstance permet de verififier si un object est d'une classe
     exple: isinstance(p1,Personne) # true
    """

Voiture_bleu =Voiture("red","Audi",15) #instance lorsque le cree python execute __init__
Voiture_bleu.couleur= "yellow"
Voiture_rouge =Voiture("black","Bentley",55)



print(Voiture_bleu.couleur)
print(Voiture_bleu.marque)
print(Voiture_bleu.vitesse)
print("-----------------------------------------------------------------------------")

print(Voiture_rouge.couleur)
print(Voiture_rouge.marque)
print(Voiture_rouge.vitesse)
print("-----------------------------------------------------------------------------")

print(Voiture_bleu.vitesse)
Voiture_bleu.accelerer(20)
print(Voiture_bleu.vitesse)
print("-----------------------------------------------------------------------------")
print(Voiture_bleu.vitesse)
Voiture_bleu.freiner(10)
print(Voiture_bleu.vitesse)
