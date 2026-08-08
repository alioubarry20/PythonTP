import socket

# Création socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion
client_socket.connect(("127.0.0.1", 8080))

# Saisie du nombre
nombre = input("Entrer un nombre : ")

# Envoi
client_socket.send(nombre.encode())

# Réception du résultat
resultat = client_socket.recv(1024).decode()
print(f"Le carré est : {resultat}")

# Fermeture
client_socket.close()
