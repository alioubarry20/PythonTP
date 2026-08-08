etudiants = [
    {"nom": "Awa", "moyenne": 15},
    {"nom": "Moussa", "moyenne": 9},
    {"nom": "fatou", "moyenne": 12}
]


# fonction qui permet d'afficher chq etudiant avec sa moyenne
def afficher_etudiants(liste):
    for etu in liste:
        print(f"{etu["nom"]} voici ta moyenne:{etu['moyenne']}")


# fonction qui retourne la moy generale de la classe 
def moyenne_classe(liste):
    total = 0
    for etu in liste:
        total += etu["moyenne"]
        return total/len(liste)

# affoche le best etdudiant

def meilleur_etudiant(liste):
    best = liste[0]
    for i in liste:
        if i["moyenne"]> best["moyenne"]:
            best= i
            return best["nom"]
        
print("la liste des etudiants\n")
afficher_etudiants(etudiants)

print("la moyenne de la classe est de:",moyenne_classe(etudiants))
print("le meilleur etudiant de la classe est:",meilleur_etudiant(etudiants))