import socket
#1ere etape
serveurSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serveurSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADR,)
#socket.AF_INET cest pour ipv4 la famille
#SOCK_STREAM pour le TCP le type
#SOCK_datagram pour le UDP le type

#2eme etape lier le socket a une add ip et port
#bind une fonction qui permet de lier le socket aune adresse ip et un numero de port

serveurSocket.bind(('0.0.0.0',8000))
#'0.0.0.0' pour recup de linterface active et cava fonctionner 

#3eme etape mettre lz socket serveur en ecoute
serveurSocket.listen(5)
#4eme etape attendre les connections
(socketClient,adIPClient)+ serveurSocket.accept()
print("Information du client connecter ",socketClient,adIPClient)
CA = True
while CA:

    message=input("saisiez les donner")
    if message != "":
        socketClient.send(message.encode())
        donner=SocketClient.recv(2048)
        print("Le client a envoyer",donner)
    else:
        CA = False
serveurSocket.close()
SocketClient.close()

