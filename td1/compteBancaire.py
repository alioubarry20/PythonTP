class CompteBancaire:
    def __init__(self,proprietaire,solde):
        self.proprietaire = proprietaire
        self.solde = float(solde)

#les methodes deposer & retirer
    def deposer(self,montant):
        if montant>0:
            self.solde =self.solde + montant
        else:
            print("Impossible,veuillez deposer un montant!")
        
    def retirer(self,montant):
        if montant<=self.solde:
            self.solde -= montant
        else:
            print("le solde est insuffisant!")

# Redéfinir la méthode __str__ pour afficher : 
    def __str__(self):
        return f"Compte de {self.proprietaire} | Solde: {self.solde} FCFA"
            
    # def __add__(self,autre):
    #     return CompteBancaire("Fusion", self.solde + autre.solde)
   
    def __add__(self, autre):
        return CompteBancaire("Fusion", self.solde + autre.solde)




compte1 = CompteBancaire("aliou", 60000)
compte2 = CompteBancaire("fama", 40000)

compte1.deposer(10000)
compte2.retirer(5000)

print(compte1) 
print(compte2)  

compteFusion = compte1 + compte2
print(compteFusion)  # Fusion de aliou et fama | Solde: 105000 FCFA