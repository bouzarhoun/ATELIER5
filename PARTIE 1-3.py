class Rectangle: #declaration de la calss rectangle 

        def __init__(self, longueur=30, largeur=15):
                self.longueur = longueur
                self.largeur = largeur
                self.nom = "rectangle"

        def surface(self):
                return self.longueur*self.largeur

        def affichage(self):
                print("Le Surface de %s est: %.2f"% (self.nom, self.surface()))

class Carre(Rectangle): #declaration de la sous class carre 

        def __init__(self, cote):
                Rectangle.__init__(self, cote, cote)
                self.nom = "carre"

r = Rectangle(10, 5)
c = Carre(6)
r.affichage() #afichage de la surface de rectangle 
c.affichage() #affichage de la surface de la carre