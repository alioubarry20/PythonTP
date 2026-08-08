import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("localhost",5059))
s.listen(10)
print("Serveur en attente de connexion!")

conn ,addr = s.accept()
print(f"connecter a {addr}")

reponse = conn.recv().decode()
print(f"le nombre recu{reponse}")


nombre = int(reponse)

carre = reponse**2
conn.send(str(carre).encode())

conn.close()
s.close()


