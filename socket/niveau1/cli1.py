import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost",5059))

message = input("Entrez un nombre")
s.send(message.encode())


resultat= s.recv(1024).decode()
print(f"le carre est :{resultat}")

s.close()