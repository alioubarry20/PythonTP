import socket

# creer un socket client
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# se connecter au serveur (local)
client_socket.connect(("127.0.0.1",5000))

# envoyer un messs
client_socket.send("client 1".encode())


#recevoir la rep du serv
reponse=client_socket.recv(1024).decode()
print(f"Reponse serveur: {reponse}")
client_socket.close()
