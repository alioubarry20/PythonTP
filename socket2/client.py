import socket
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientSocket.connect(('10.0.2.15',8000))
CA= True
while CA:

    message=input('saisiez les donner ')
    if message !='':
        clientSocket.send(message.encode())
        donnes=clientSocket.recv(2048)
        print('Le serveur a envoyer',donnes)
    else:
        CA= False


clientSocket.close()