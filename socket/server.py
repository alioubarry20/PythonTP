import socket

#creer un socket serveur
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# associer le socket au port 5000 en local
server_socket.bind(("127.0.0.1",5000))

#ecouter les connexions entrant
server_socket.listen(10)
print("serveur en attente")

#accepter une connexion

conn,addr=server_socket.accept()
print(f"client connecter:{addr}")

#recevoir un mess
message = conn.recv(1024).decode()
print(f"Message recu du client:{message}")

# envoyer une reponse
conn.send("serveur sup de ".encode())

#fermer la connexion
conn.close()
server_socket.close()
