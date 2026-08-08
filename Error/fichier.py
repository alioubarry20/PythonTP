import json

# Liste de produits
produits = [
    {"nom": "Coca", "prix": 600, "quantite": 20},
    {"nom": "Lait", "prix": 700, "quantite": 15}
]

# Sauvegarde
try:
    with open("produits.json", "w", encoding="utf-8") as f:
        json.dump(produits, f, indent=4, ensure_ascii=False)
    print("Produits sauvegardés\n")
except Exception as e:
    print(f"Erreur sauvegarde: {e}")

# Rechargement
try:
    with open("produits.json", "r", encoding="utf-8") as f:
        produits_charges = json.load(f)
    
    print("Produits chargés:")
    for p in produits_charges:
        print(f"- {p['nom']}: {p['prix']} FCFA (stock: {p['quantite']})")
        
except FileNotFoundError:
    print("Fichier introuvable")
except json.JSONDecodeError:
    print("Format JSON invalide")


    """
    
    
    
 try:
    # Écriture
    with open("notes.txt", "w", encoding="utf-8") as f:
        f.write("Mamadou - 15\n")
        f.write("Awa - 17\n")
        f.write("Fatou - 12\n")
    
    print("Fichier créé avec succès\n")
    
    # Lecture
    with open("notes.txt", "r", encoding="utf-8") as f:
        print("Contenu du fichier:")
        contenu = f.read()
        print(contenu)
        
except IOError as e:
    print(f"Erreur fichier: {e}")
    
    
    """