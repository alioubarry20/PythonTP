# reponse=""
# while reponse!="oui":
#     reponse = input("dite'oui'pour arreter:")
# print('Merci!')    
#les listee

#  insert(i, x) : Insère l'élément x à l'indice i. 

#fruit =["banane","orange","cerice"]
# print(fruit.insert(0,"keychup"))
# print(fruit.remove("banane"))
# print(fruit.append("banane"))
# print(fruit.pop(0))
# print(fruit.index("cerice"))
#print(fruit.reverse)
# print(fruit)
carre =[x**2 for x in range(5)]
#print(carre)

nombre = [1,2,3,4,5,6]
impaire=[i for i in nombre if i%2!=0]
print(impaire)

coordonner=(10,50,10,10,50,10)
print(coordonner.count(10))
voiture = {
    "marque":"AUDI","nbRoue":4,"color":"fullBlack"
}
voiture["color"]="red"
print(voiture)