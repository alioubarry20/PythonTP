# definition de la procedure
# def calcule():
#     a=int(input("entrez a: "))
#     b=int(input("entrez b: "))
#     c = a * b
#     return c
#     # calcule()
# resultat = calcule()
# print("le resulta de a * b est: ",resultat)
#     # print(c)
a = int(input("entrez a: "))
b = int(input("entrez b: "))
def produit(n1,n2):
    p =n1 * n2
    return p
val = produit(a,b)
produit("le produit est egal a: ",val)