import socket

# Création du socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect(('127.0.0.1', 8080))

# Saisie du message
message = input("Entrer un message : ")

# Envoi du message
client_socket.send(message.encode())

# Réception de la réponse
reponse = client_socket.recv(1024).decode()
print(f"Réponse du serveur : {reponse}")

# Fermeture
client_socket.close()
