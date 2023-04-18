import random
print("Voici", "un", "exemple", "d'appel", sep=" % ", end=" -\n")
Random_Number=random.randint(0, 9)
Random_Number=Random_Number**2
print("Voici", "un", Random_Number, "d'appel", sep=" % ", end=" -\n")

Time=5600
#Time=int(input("enté le nombre de secondes pour un conversion en heure:minutes::secondes"))
Time_J=0
Time_H=0
Time_M=0
Time_S=0
Time_J=Time//(24*3600)
Time=(Time-(Time_J*(24*3600)))
Time_H=Time//(3600)
Time=(Time-(Time_H*3600))
Time_M=Time//(60)
Time=(Time-(Time_M*60))
Time_S=Time
print("Votre temps en secondes corresponds à ",Time_J,Time_H, Time_M, Time_S, sep=":", end=" -\n")

Nombre_de_Candidats=1
#Nombre_de_Candidats=int(input("Nombre de Candidats"))
for i in range(Nombre_de_Candidats):
    Suffrage=float(51)
    #Suffrage=float(input("suffrage en % du candidat"))
    if Suffrage>50:
        print("élu au premier tour")
    else:
        if Suffrage>12.5:
            print("ticket pour le 2eme tour")
        else:
            print("Battu")

nombre=int(7)
#nombre=int(input("entrer un nombre"))
for i in range(10):
    i=i+1
    print(nombre*i)

nombre2=int(5)
#nombre2=int(input("entrer un nombre"))
nombre3=0
for i in range(nombre2):
    i=i+1
    nombre3=i+nombre3
    print(nombre3)

nombre2=5
#nombre2=int(input("entrer un nombre"))
nombre3='*'
nombre5=int(0)
for i in range(nombre2):
    print(nombre3)
    nombre3=nombre3+nombre3

nombre2=19
nombre4=' '
nombre3='*'
nombre5=1
affichage=''
for i in range(nombre2//2):
    for j in range((nombre2//2)+1-i):
        affichage=affichage+nombre4
    for k in range(nombre5):
        affichage=affichage+nombre3
    if nombre5<(nombre2-1):
        nombre5=nombre5+(2)
    for j in range((nombre2//2)+1-i):
        affichage=affichage+nombre4
    print(affichage)
    affichage=''

"""from turtle import *
width(5)
color('red')
down()
for i in range (20):
 left(i*5)
 forward(i*5)"""



a=float(2)
b=float(3)
c=float(4)
d=float(5)
nombre_floatant=0
#a=float(input("entré un nombre"))
#b=float(input("entré un nombre"))
#c=float(input("entré un nombre"))
#d=float(input("entré un nombre"))
#nombre_floatant=0

def f_Sum(nb1,nb2,nb3,nb4):
    nombre_floatant=nb1+nb2+nb3+nb4
    print(nombre_floatant)

f_Sum(a, b, c, d)

note = []
somme, moyenne = 0,0
for i in range (0,4):
    print("saisir la note n°",i+1)
    i+=1
    #saisie = int(input())
    note.append(10)
for i in range (0,4):
    somme = somme + note[i]
    moyenne = somme / 4
print("la moyenne des notes est",moyenne)

Nb = []
for i in range(0,6):
    Nb.append(i * i)
    print(Nb[i])
print("")

liste = [1]
for k in range(1,7):
    liste.append(liste[k-1] + 2)
print(liste)
print("")

suite = [1,1]
for i in range(2,8):
    suite.append(suite[i-1] + suite[i-2])
    print(suite)
print("")

tri = [12 ,4 ,10 ,5 ,6 ,7 ,8 ,9 ,10 ,1]
for i in range(0, len(tri)):
    i+=1
    for j in range(0, len(tri)-1):
        if (tri[j]>tri[j+1]):
            tri[j], tri[j+1]=tri[j+1],tri[j]
print(tri)

import math
#help(math)

from monmodule import mafonction
print(mafonction(4))

from monmodule import age
age(18)




from random import *

nombre_coule1=randint(1, 5)
nombre_coule2=randint(1, 5)
#print(nombre_coule1, nombre_coule2)
coule_user1=int(input("ligne"))
coule_user2=int(input("colonne"))
if coule_user1==nombre_coule1 and coule_user2==nombre_coule2:
    print("coulé")
elif coule_user1==nombre_coule1:
    print("même ligne")
elif coule_user2==nombre_coule2:
    print("même colonne")
else:
    print("ni sur la ligne, ni sur la colone")