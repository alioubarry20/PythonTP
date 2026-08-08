import threading

class Mythread(threading.Thread):

    def __init__(self,nom,val_init,val_finale):
        threading.Thread.__init__(self,nom,val_init)

        self.nom = nom 
        self.val_init = val_init 
        self.val_finale = val_finale 


    def run(self):
        print("Thread lancer!")
        for i in range(self.val_init,self.val_finale):
            print(self.nom+""+str(i))

t1 =Mythread("thread1",0,10)
t1.start()

t1 =Mythread("thread2",0,20)
t1.start("thread2")
