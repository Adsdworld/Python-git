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
coule_user1=int(3)
coule_user2=int(3)
#coule_user1=int(input("ligne"))
#coule_user2=int(input("colonne"))
if coule_user1==nombre_coule1 and coule_user2==nombre_coule2:
    print("coulé")
elif coule_user1==nombre_coule1:
    print("même ligne")
elif coule_user2==nombre_coule2:
    print("même colonne")
else:
    print("ni sur la ligne, ni sur la colone")

thistuple = ("apple", "banana", "cherry", "cool", "fruit")
print(thistuple[1])
print(thistuple[-2])
print(thistuple[2:4])
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 
for x in thistuple:
    print(x) 
print(len(thistuple)) 

nombre2=int(3)
position1=int(0)
my_tuple=(3, 1, 4, 1, 5, 9, 2)
def position (a, b, c):
    y=list(c)
    y.insert(b, a)
    c=tuple(y)
    return c
print("mon premier truc :", position(nombre2, position1, my_tuple))

def copie_tuple (t):
    
    return t

print("show liste")
liste1=[1,2,3,4,5]
for i in range(5):  #for i in range va de 0 à range-1 ici 4
    print(liste1[i])

prenom = "JeAn"
nom = "DuRaNt"
age = 21
print("Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom.lower(), nom.upper(), age))
print("Je m'appelle {} {} et j'ai {} ans.".format(prenom, nom, age))

prenom = "Jean"
message = "Bonjour"
age = 21
chaine_complete = message + " " + prenom + " tu as " + str(age) # On utilise le symbole '+' pour concaténer deux chaînes
print(chaine_complete)
if 'J' in prenom :
 print("Oui, 'J' est dans le prénom")

chaine = "Salut !"
print(chaine[0]) # Première lettre de la chaîne
print(chaine[2]) # Troisième lettre de la chaîne
print(chaine[-1]) # Dernière lettre de la chaîne 

chaine = "Bonjour !"
for i in chaine:
 print(i)

presentation = "BonjourBonsoir"
print(presentation[0:7]) # On sélectionne les deux premières lettres : 'sa'
print(presentation[7:len(presentation)]) # On sélectionne la chaîne sauf les deux 1ères lettres : 'lut'

def nombre_de_voyelle(chaine):
    i=0
    b=0
    while i<len(chaine):
        if chaine[i] in "aeiouy":
            b=b+1
        i+=1
    return b
def position_de_la_lette_e(chaine):
    i=0
    b=""
    while i<len(chaine):
        if chaine[i] in "e":
            b+=str(i+1)+":"
        i+=1
    return b
chaine = str("ceci est une chaine")
print("Il y a {} dans {} et la lettre e est situé en position {}".format(str(nombre_de_voyelle(str(chaine))), chaine, position_de_la_lette_e(chaine)))

ma_liste_de_mots = [ 'Cosinus', 'Sinus', 'Tangente', 'Cotangente' ]
ma_liste_de_mots.sort()
print(ma_liste_de_mots)
for i in range(len(ma_liste_de_mots)):
    ma_liste_de_mots.insert(i,str(ma_liste_de_mots[i]+" hyperbolique"))
    del ma_liste_de_mots[i+1]
print(ma_liste_de_mots)

ma_liste_de_mots= ["maths", "info", "python", "exposants", "alpha", "fonction", "parabole","equilateral", "orthogonal", "cercle", "isocèle" ]
print(ma_liste_de_mots)
del ma_liste_de_mots[len(ma_liste_de_mots)-1]
print(ma_liste_de_mots)

b=[]
for i in ma_liste_de_mots:
    if i[0] in "aeiouy":
        b.append(i[0])
    if i[len(i)-1] in "s":
        b.append(i)
print(b)
ma_liste_de_6_caractères=[]
ma_liste_de_mots = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
for i in ma_liste_de_mots:
    if len(i)<6:
        ma_liste_de_6_caractères.append(i)
for i in ma_liste_de_mots:
    if i in ma_liste_de_6_caractères:
        ma_liste_de_mots.remove(i)
print(ma_liste_de_6_caractères)
print(ma_liste_de_mots)

voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
ma_liste_de_mots = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
for i in ma_liste_de_mots:
    b=0
    for j in range(len(i)):
        if i[j] in voyelles:
            b+=1
    print("{} ont été trouvées dans {}".format(b, i))

chaine="fêter"
def conjugaison_verbe_er(chaine):
    chaine = chaine.replace("er", "")
    print("Je {}e".format(chaine))
    print("Tu {}es".format(chaine))
    print("Il {}e".format(chaine))
    print("Nous {}ons".format(chaine))
    print("Vous {}ez".format(chaine))
    print("Ils {}ent".format(chaine))
conjugaison_verbe_er(chaine)

matValeurs=[[10,7,4,11,3],[0,-1,4,9,12],[8,-18,2,157,63]]
print(type(matValeurs))
print(matValeurs[0])
print(matValeurs[1])
print(matValeurs[0][0])
print(matValeurs[0][1])

matValeurs=[[10,7,4,11,3],[0,-1,4,9,12],[8,-18,2,157,63]]
col3 = [] #liste vide
for ligne in matValeurs :
 print(ligne)
 col3.append(ligne[2]) # ajouter le 3ème élément
print("col3 : ",col3)

def initMatVal(nb_ligne,nb_colonne,valeur):
 #Création d’une matrice vide
 matrice=[None] * nb_ligne
 for i in range(nb_ligne):
    matrice[i]=[None] * nb_colonne
 #Initialisation de la matrice avec val
 for i in range(nb_ligne):
    for j in range (nb_colonne):
        matrice[i][j]=valeur
 return matrice

print(initMatVal(5,5, 3))

mat=[[10,2,3,12],[4,-5,60,-1],[7,80,9,11]]
for i in mat[0]:
    print(i)
for i in mat[1]:
    print(i)
for i in mat[2]:
    print(i)

T = [[1,9,5],[2,18,4],[-8,0,-2]]
somme=0
for ligne in range(len(T)):
    print(len(T))
    for element in range(len(T[ligne])):
        somme+=T[ligne][element]
print(somme)

T = [[1,9,5],[2,18,4]]
max=0
for ligne in range(len(T)):
    for element in range(len(T[ligne])):
        if max<T[ligne][element]:
            max=T[ligne][element]
print(max)

mon_dictionnaire = {}
mon_dictionnaire["pseudo"] = "Jean"
mon_dictionnaire["date"] = 12
mon_dictionnaire["mot de passe"] = "***"
print(mon_dictionnaire)
mon_dictionnaire["mot de passe"]
print(mon_dictionnaire)
del mon_dictionnaire["date"] 
print(mon_dictionnaire)
print(mon_dictionnaire.pop("pseudo"))

fruits = {"pommes":21, "melons":3, "poires":31}
for cle in fruits:
 print(cle) 
for cle in fruits.keys():
 print(cle) 
for valeur in fruits.values():
 print(valeur)
if 21 in fruits.values():
 print("Un des fruits se trouve dans la quantité 21.") 

 d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}
def ChangeNomByPrenom(dico):
    dico=d
    nom=dico["nom"]
    prenom=dico["prenom"]
    del dico["nom"]
    del dico["prenom"]
    dico["nom"]=nom
    dico["prenom"]=prenom
ChangeNomByPrenom(d)
print(d)
