# de Sallier Dupin Arthur
# Examen du 12/10/2023
# Module Fonctions

# Fonction qui renvoie le résultat d'une division
# Contrôler la saisie de l'utilisateur et gérer les exceptions pouvant survenir
# lorsque cette fonction est appelée
def fonction1() :
    while True:# saisir un premier entier entre 2 et 12
        try:
            nb1=int(input("Saisir un entier entre 2 et 12"))
            if not(1<nb1<13):
                raise Exception("Erreur de saisie recommencer")
            break
        except Exception as err:
            print(err)
    while True:# saisir un second entier
        try:
            nb2=int(input("Saisir un entier"))
            break
        except ValueError as err:
            print(err)
    print(nb1/nb2) # effectuer la division et afficher le résultat de la division
    
    
    
    
    
    

# Fonction qui fait saisir 10 mots à l'utilisateur, qui les stocke dans une liste
# puis qui retourne cette liste
def fonction2() : # créer une liste qui contient des mots (au moins 10) et retourner la liste
    Liste=[]
    for i in range(10):
        while True:
            try:
                choice=input("Veuillez saisir un mot: ")
                if len(choice)<1:
                    raise Exception
                break
            except:
                print("Une erreur est survenue")
        Liste.append(choice)
    return Liste
            
        
    


# Fonction qui retourne un mot pris au hasard dans une liste
# La liste est récupérée en paramètre
from random import randint
def fonction3(Liste) :
    return Liste[randint(0,len(Liste)-1)]
    # récupérer un mot de la liste au hasard
   
    # retourner la liste


# Fonction qui recherche un caractère dans une chaine de caractères
# Cette fonction prend en paramètre une liste déjà remplie de mots
# et va utiliser la fonction3 pour récupérer un mot de la liste au hasard
# L'utilisateur va saisir une lettre
# La fonction va retourner vrai si le caractère est présent dans le mot et faux sinon
def fonction4(Liste) :
    mot=fonction3(Liste)
    while True:
        try:
            choice=input("Veuillez saisir un caractère à rechercher: ")
            if len(choice)!=1:
                raise Exception("Erreur de saisie recommencer")
            if choice=="0" or choice=="1" or choice=="2" or choice=="3" or choice=="4" or choice=="5" or choice=="6" or choice=="7" or choice=="8" or choice=="9":
                raise Exception("Erreur de saisie recommencer")
            break
        except Exception as err:
            print(err)
    print("mot choisit dans la liste au hasard: {}".format(mot.upper()))
    if choice.lower() in mot.lower():
        return True
    else:
        return False
    # faire saisir un caractère - avec les contrôles nécessaires

    # récupérer au hasard d'un mot de la liste


    # retourner le résultat de la recherche



