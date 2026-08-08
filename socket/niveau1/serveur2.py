import socket

# Création du socket serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Association adresse + port
server_socket.bind(("127.0.0.1", 8080))

# Mise en attente
server_socket.listen(1)
print("Serveur en attente de connexion...")

# Acceptation connexion
conn, addr = server_socket.accept()
print(f"Connecté à : {addr}")

# Réception du nombre
message = conn.recv(1024).decode()
print(f"Nombre reçu : {message}")

# Conversion en entier
nombre = int(message)

# Calcul du carré
carre = nombre ** 2

# Envoi du résultat
conn.send(str(carre).encode())

# Fermeture
conn.close()
server_socket.close()
