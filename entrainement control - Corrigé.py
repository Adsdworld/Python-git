"""
Chaine de caractères: Séquences de caractères, manipulables et concaténables, définit entre des "" ou ''
Dictionnaire: Paires clé-valeur, accès rapide et rangé par clé définit par {}
Matrice: liste de liste 
Tuple: Liste non-modifable définit par ()
Module: Fichier contenant des fonctions.
Liste : valeurs rangé par position de 0 à longueur de la liste moins 1 définit par []
Tri : utilisation de .sort() si disponible ou comparaison > ou < ou = des termes 1 par 1
Inversion : utilisation de .reverse() si disponible
Fonction: Bloc réutilisable de code qui effectue une tâche spécifique définit par def nom_de_la_fonction (paramètre1, paramètre2): 
Concaténation: Fusion de deux chaînes ou listes en une seule.
"""



# Control Rédiger par ChatGPT
# Bienvenue à ce deuxième contrôle de Python ! Cette fois-ci, nous allons aborder de nouvelles notions telles que les chaînes de caractères, 
# les dictionnaires, les matrices, les tuples et les modules. Voici des énoncés d'exercices pour tester vos compétences :


#####################################################################################################
# IL FAUT FAIRE LES EXERCICE DANS L'ORDRE POUR NE PAS AVOIR DE PROBLEME D'INDENTATION (=espacement) #
#####################################################################################################
# Exercice 1: 
# Écrivez une fonction appelée "longueur_chaine" qui prend en entrée une chaîne de caractères et retourne sa longueur.
ma_chaine="Je veux avoir 20/20 en python donc je m'entraine"
def longueur_chaine(ma_chaine):
    longueur = len(ma_chaine)
    print(longueur)
longueur_chaine(ma_chaine)
    


# Exercice 2: 
# Créez un dictionnaire vide appelé "mon_dictionnaire" et ajoutez-y trois clés "nom", "âge" et "ville". Demandez ensuite à l'utilisateur de saisir 
# les valeurs correspondantes et affichez le dictionnaire final.
mon_dictionnaire = {"nom":"Arthur", "âge":"18", "ville": "Angers"}
print(mon_dictionnaire)



# Exercice 3 :
# Écrivez une fonction appelée "somme_matrice" qui prend en entrée une matrice (une liste de listes) et renvoie la somme de tous les éléments.
# Essayer aussi avec ma_matrice2
ma_matrice=[[0, 2, 3],[10, 5],[30]]
ma_matrice2=[[0, 2, 3],[10, 5, 5], [10, 2, 8]]
def somme_matrice(ma_matrice):
    nombre=0
    for i in ma_matrice: 
        print(i)
        for j in i:
            nombre=nombre+j
    print(nombre)
somme_matrice(ma_matrice2)


# Exercice 4 : 
# Créez un tuple contenant les jours de la semaine. Affichez le jour correspondant à l'indice 3.
# Info, un tuple est une liste qui ne peut être modifié une fois cré, il s'initialise comme ceci :
mon_tuple=("lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche")
print(mon_tuple[2])


# Exercice 5 : 
# Écrivez une fonction appelée "concatener_listes" qui prend deux listes en entrée et renvoie une nouvelle liste contenant les éléments des deux listes 
# concaténés.
# affichage :
# ma_liste_final = ["rose", "age", 28, "orange", 20, 28, "couleur"]
ma_liste1 = ["rose", "age", 28]
ma_liste2 = ["orange", 20, 28, "couleur"]
nouvelle_liste=ma_liste1+ma_liste2
print(nouvelle_liste)



# Exercice 6 : Créez une fonction appelée "inverser_chaine" qui prend une chaîne de caractères en entrée et renvoie une nouvelle chaîne inversée 
# (par exemple, "Bonjour" devrait devenir "ruojnoB").
# Par exemple "Je m'appel Tom et j'ai 28 ans" deviendrais "sna 82 ia'j..."
ma_chaine1 = "Bonjour"
ma_chaine2 = "Je m'appel Tom et j'ai 28 ans"
longueur = len(ma_chaine2)
nouvelle_chaine=""
for i in range(longueur):
    nouvelle_chaine=nouvelle_chaine + ma_chaine2[longueur-i-1]
print(nouvelle_chaine)



# Exercice 7: 
# Écrivez une fonction appelée "compter_elements" qui prend une liste en entrée et renvoie un dictionnaire contenant chaque élément de la liste et 
# son nombre d'occurrences.
# dictionnaire attendu : {"8": 2, "15": 1, "13": 3}
ma_liste=[8, 15, 8, 13, 13, 13]
nouveau_dictionnaire={}
for i in ma_liste:
    print(i)
    if i in nouveau_dictionnaire:
        a=nouveau_dictionnaire[i]
        nouveau_dictionnaire[i]=a+1
    else:
        nouveau_dictionnaire[i]=1
print(nouveau_dictionnaire)



# Exercice 8 : 
# Créez une matrice de 3 liste contenant 3 nombre et y placer correctement les nombres pour obtenir le résultat ci-dessous. Affichez la matrice 
# sur 3 lignes, 1 ligne par liste.
# affichage : 
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
ma_matrice=[[9, 4, 7], [2, 5, 8], [3, 6, 9]]
for i in ma_matrice:
    print(i)



# Exercice 9:
# Écrivez une fonction appelée "somme_tuples" qui prend deux tuples contenant des nombres en entrée et renvoie un nouveau tuple contenant la somme 
# des éléments correspondants.
# affichage :
# mon_tuple_final=(66)
mon_tuple1 = (10, 8, 6, 4, 2, 0) # 30
mon_tuple2 = (1, 3, 5, 7, 9, 11) # 36
nombre=0
nouveau_tuple=mon_tuple1+mon_tuple2
for i in nouveau_tuple:
    nombre=nombre+i
print(nombre)



# Exercice 10: 
#Importez le module "random" et générez un nombre aléatoire entre 1 et 10.
import random
print(random.randint(10, 20))


# Exercice 11 :
# Créez une liste contenant les noms de cinq pays et triez-la par ordre alphabétique.
ma_liste=["France", "Angleterre", "Chine", "Etat-unies", "Espagne"]
ma_liste.sort()
print(ma_liste)


# Exercice 12 : 
# Écrivez une fonction appelée "concatener_dictionnaires" qui prend deux dictionnaires en entrée et renvoie un nouveau dictionnaire contenant toutes 
# les clés et valeurs des deux dictionnaires combinés.
# affichage :
# mon_dictionnaire_final={"rose":"couleur", "nombre": 26, "nom":"de Sallier Dupin", "âge": 18, "prénom": "arthur"}
mon_dictionnaire1 = {"rose":"couleur", "nombre": 26}
mon_dictionnaire2 = {"nom":"de Sallier Dupin", "âge": 18, "prénom": "arthur"}
nouveau_dictionnaire={}
nouveau_dictionnaire=mon_dictionnaire1
for i in mon_dictionnaire2:
    print(i)
    if str(i) in nouveau_dictionnaire:
        print("La clé existe déjà, impossible d'ajouter la nouvelle clé sans détruire la précédante")
    else:
        nouveau_dictionnaire[i]=mon_dictionnaire2[i]
print(nouveau_dictionnaire)



# Exercice 13 :
# Demandez à l'utilisateur de saisir une phrase et comptez le nombre de mots dans cette phrase.
la_phrase = "Ceci est une phrase qui contient des lettres qui séparées par des espaces forment des mots"
nombre=la_phrase.count(" ") # pas sur que l'on l'ai vu
print(nombre)



# Exercice 14 :
# Écrivez une fonction appelée "moyenne_liste" qui prend une liste de nombres en entrée et renvoie la moyenne de ces nombres.
ma_liste=[8, 15, 8, 13, 13, 13]
nombre=0
for i in ma_liste:
    nombre=nombre+i
moyenne= nombre/len(ma_liste)
print(moyenne)



# Exercice 15 : 
# Importez le module mathématique et utilisez la fonction "sqrt" pour calculer la racine carrée d'un nombre saisi par l'utilisateur.
from math import *
nombre_au_carré = sqrt(int(input("entrer un nombre")))
print(nombre_au_carré)


# Exercice 16: 
# Demandez à l'utilisateur de saisir deux nombres et effectuez toutes les opérations mathématiques de base (+, -, *, /) entre ces deux nombres.
nombre1 = int(input("entrer un nombre"))
nombre2 = int(input("entrer un nombre"))
print(nombre1+nombre2)
print(nombre1-nombre2)
print(nombre1/nombre2)
print(nombre1*nombre2)


# Exercice 17 : 
# Demander un nombre entier à l'utilisateur
# Créez une fonction appelée "est_premier" qui prend un nombre en entrée et renvoie True s'il est premier, sinon False.
# un nombre est premier si ses seuls diviseurs sont 1 et lui-même
def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True

nombre = int(input("Entrer un nombre : "))

if est_premier(nombre):
    print(nombre, "est un nombre premier.")
else:
    print(nombre, "n'est pas un nombre premier.")



# En bonus un devine nombre, qui pourrait tomber à l'exament:
import random

def devine_nombre():
    nombre_choisi = random.randint(1, 100)
    essais = 0
    devine = False

    print("=== Devine le nombre ===")
    print("J'ai choisi un nombre entre 1 et 100. À toi de deviner !")

    while not devine:
        essais += 1
        proposition = int(input("Entre ta proposition : "))

        if proposition < nombre_choisi:
            print("C'est plus grand !")
        elif proposition > nombre_choisi:
            print("C'est plus petit !")
        else:
            devine = True

    print("Bravo ! Tu as deviné le nombre en", essais, "essais.")

devine_nombre()


# Comment ordonner les liste d'une matrice :
ma_matrice=[[99, 14, 7], [23, 5, 8], [3, 86, 9]]
ma_matrice.sort() # permet d'ordonner les liste par ordres de grandeur

ma_matrice=[[99, 14, 7], [23, 5, 8], [3, 86, 9]]
nouvelle_matrice=[[], [], []]
for i in range(len(ma_matrice)):
    ma_matrice[i-1].sort()
    nouvelle_matrice[i-1]=ma_matrice[i-1]
print(nouvelle_matrice)