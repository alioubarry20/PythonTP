import socket

#session UDP
serveur=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# permet de libere le port/serveur apres utilisation
serveur.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serveur.bind(('localhost',3000))
print("SErveur UDP en ecoute sue le port 3000\n")


while True:
    # utilisation de recv pour recup du turple
    request,address=serveur.recv(1024)
    print("Message Client: ",request.decode("utf-8"))
    print("IP du client connecter: ",address)
    serveur.sendto(b"I am the serveur",address)

serveur.close()
