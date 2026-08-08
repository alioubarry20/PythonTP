import socket

# Création du socket (IPv4 + TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à une adresse et un port
server.bind(("localhost", 9000))  # 127.0.0.1:5000

# Serveur en écoute
server.listen(10)
i =0
mots_secret='lion'

while i < 10 :
    
    print("Serveur en attente de connexion...")
    

    # Accepter une connexion
    client_socket, client_address = server.accept()
    print(f"Client connecté {i} : {client_address}")




    # Recevoir un message
    message = client_socket.recv(1024).decode("utf-8")
    print("Message reçu :", message)

    # Répondre au client
    client_socket.send("Message bien reçu !".encode("utf-8"))
    i+=1
    if message.lower == mots_secret.lower:
        print(f"bravo vous avez trouver le mots ")
    else:
        print('cest pas le bon mots')

# Fermer les sockets
client_socket.close()
server.close()