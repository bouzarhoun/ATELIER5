class etudiant:
    def __init__(self,nom,prenom,age,cne,moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne

list = []
l1 = []
l2 = []
list.append( etudiant('ismail','bouzarhoun',20,'P123434634',12.22) )
list.append( etudiant('anass','mroubae',21,'P132234354',3.19) )
list.append( etudiant('zayd','filali',12,'Q123253456',18.23) )

for obj in list:
    l1.append(obj.age)
    l2.append(obj.moyenne)
i=1
l1.sort()
print("L'age tries:")
for obj in l1:
    for obj1 in list:
        if obj1.age == obj:
            print(str(i)+": "+obj1.nom+" "+obj1.prenom+" "+str(obj1.age)+" "+obj1.cne+" "+str(obj1.moyenne))
            i+=1

print("------------------------------------------------------")
i=1
l2.sort()
print("Le moyenne tries:")
for obj in l2:
    for obj1 in list:
        if obj1.moyenne == obj:
            print(str(i)+": "+obj1.nom+" "+obj1.prenom+" "+str(obj1.age)+" "+obj1.cne+" "+str(obj1.moyenne))
            i+=1