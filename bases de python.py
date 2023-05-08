#// partie entière de a//b (enlève ce qui est après la virgule)
#** (puissance)
 
stop=True
age = ""
while stop: #Tant que True == stop(True) c'est VRAI, Tant que True == stop(False) c'est FAUX 
    age = input("Entré vôtre âge")
    try : #cette structure permet d'essayer de faire une action, si il y a échec, ça ne stop pas le programme
        age=int(age)
        stop=False
    except ValueError:
        print("Vous n'avez pas rentré un nombre")

prénom = input("entrez votre prénom")
print("Vous vous appellez {} et vous avez {} ans".format(prénom, age))

print()
print("***")
liste=['Jean', 'alexandre',3,4]
print("création d'une liste : {}".format(liste))
print("     for i in range(4)")
print("         print(liste[i])")
for i in range(4):  #i va de 0 à range-1 ici 3
    print(liste[i])

print("on prends chaque terme de la liste {} dans i et on vérifie si int(i)==3 ou int(i) == 4".format(liste))
print("     for i in liste")
print("         if str(i) == str(3) or str(i) == str(4):")
print("         i est un nombre, i à pour valeur {}\".format(i)")
for i in liste:  #i va de 0 à la longueur de la liste-1 soit 3
    if str(i) == str(3) or str(i) == str(4):
        print("i est un nombre, i à pour valeur {}".format(i))

print()
print("***")
liste2 = [ 'Cosinus', 'Sinus', 'Tangente', 'Cotangente' ]
print("création d'une liste : {}".format(liste2))
liste2.sort()
print("rangement de la liste avec liste2.sort() : {}".format(liste2))

print("on prends chaque terme de la liste {} dans i et on insert au i ème terme i+\" hyperbolique\"".format(liste2))
print("une fois l'insertion éffectué on à on supprime le terme de position i")
print("     for i in liste")
print("         liste2.insert(i,str(liste2[i]+\" hyperbolique\"))")
print("         del liste2[i+1]")
for i in range(len(liste2)):
    print(liste2)
    liste2.insert(i,str(liste2[i]+" hyperbolique"))
    print(liste2)
    del liste2[i+1]
print(liste2)

print()
print("***")
print("on importe la librairie random et on demande un nombre entier randomisé entre 0 inclu et 4 inclu")
print("     import random ")
print("     print(random.randint(0,4))")
import random 
print(random.randint(0,4))
    
