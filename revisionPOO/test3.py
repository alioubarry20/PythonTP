class Rectangle:

    def __init__(self,long,larg):
        self.long=long
        self.larg=larg  

    def perimetre(self):
        
        return (self.long*self.larg)*2
    def surface(self):
        
        return self.long*self.larg
    
    
class Parallepipede(Rectangle):
    def __init__(self, long, larg,hauteur):
        super().__init__(long, larg)
        self.hauteur=hauteur

    def volume(self):
        return self.long*self.larg
monRectangle=Rectangle(7,5)
print("l perimetre du rectangle est:",monRectangle.perimetre)
print("l surface du rectangle est:",monRectangle.surface)

monpara=Parallepipede(7,5,2)
print("le volume du parallepipede est:",monpara.volume)




    

