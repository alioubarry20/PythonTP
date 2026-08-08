import socket

socketServeur = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socketServeur.bind(("127.0.0.1", 5000))


socketServeur.listen(10)
print("Serveur en attente de connexion\n")


conn,adr= socketServeur.accept()
print(f"client connecter ")

message = conn.recv(1024).decode()
print(f"message recu:{message}")
reponse = message.upper()

conn.send(reponse.encode())

conn.close()
socketServeur.close()