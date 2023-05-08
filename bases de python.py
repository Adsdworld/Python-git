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

input("Appuyer sur Entrer pour continuer")

print("\n***")
liste=['Jean', 'alexandre',3,4]
print("création d'une liste : {}".format(liste)+"\n     for i in range(4)\n         print(liste[i])")
for i in range(4):  #i va de 0 à range-1 ici 3
    print(liste[i])

input("Appuyer sur Entrer pour continuer")

print("on prends chaque terme de la liste {} dans i et on vérifie si str(i)==str(3) ou str(i) == str(4)".format(liste)+"\n     for i in liste\n         if str(i) == str(3) or str(i) == str(4):\n         print(\"i est un nombre, i à pour valeur {}\".format(i)\")\n     else:\n         print(\"i n'est pas égal à str(3) ou str(4), i à pour valeur {}\".format(i))")
for i in liste:  #i va de 0 à la longueur de la liste-1 soit 3
    if str(i) == str(3) or str(i) == str(4):
        print("i est égal à str(3) ou str(4), i à pour valeur {}".format(i))
    else:
        print("i n'est pas égal à str(3) ou str(4), i à pour valeur {}".format(i))

input("Appuyer sur Entrer pour continuer")

print("\n***")
liste2 = [ 'Cosinus', 'Sinus', 'Tangente', 'Cotangente' ]
print("création d'une liste : {}".format(liste2))
liste2.sort()
print("rangement de la liste avec liste2.sort() : {}".format(liste2))

input("Appuyer sur Entrer pour continuer")

print("on prends chaque terme de la liste {} dans i et on insert au i ème terme liste2[i]+\" hyperbolique\"".format(liste2)+"\nune fois l'insertion éffectué on à on supprime le terme de position i\n     for i in liste\n         liste2.insert(i,str(liste2[i]+\" hyperbolique\"))\n         del liste2[i+1]")
for i in range(len(liste2)):
    print(liste2)
    liste2.insert(i,str(liste2[i]+" hyperbolique"))
    print(liste2)
    del liste2[i+1]
print(liste2)

input("Appuyer sur Entrer pour continuer")

print("\n***\non importe la librairie random et on demande un nombre entier randomisé entre 0 inclu et 4 inclu\n     import random\n     print(random.randint(0,4))")
import random 
print(random.randint(0,4))
    
