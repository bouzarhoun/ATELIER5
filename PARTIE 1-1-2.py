class Vecteur2D:  #declaration de class
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def affichage(self):
            print("(%.2f,%.2f)" %(self.x, self.y))

    def addition(self,v):
        s = Vecteur2D(self.x + v.x, self.y + v.y)
        return s
print("1-vecteur sans parametre: ")
V = Vecteur2D()
print(V.x)
print(V.y)
print("vecteur avec deux parametre:")
V1 = Vecteur2D(2,3)
print(V1.x)
print(V1.y)
print("2-l'affichage:")
V2 = Vecteur2D(1,7)
V3 = Vecteur2D(2,9)
V2.affichage()
V3.affichage()
print(" l'addition:")
V3.addition(V2).affichage()
