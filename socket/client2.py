import socket

# Créer un socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se connecter au server
client_socket.connect(("127.0.0.1",9000))

# Envoyer un message
client_socket.send(input("Entrez votre message : ").encode())

# Recevoir la réponse du serveur
reponse = client_socket.recv(1024).decode()
print(f"Réponse du Serveur : {reponse}")

# Fermer la connexion
client_socket.close()