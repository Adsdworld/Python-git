def afficher_morpion(morpion):
    """
    Affiche un morpion sous forme de grille avec des caractères spéciaux.
    Le morpion doit être une matrice contenant 3 listes.
    """
    print("   0   1   2")
    print("0  " + morpion[0][0] + " | " + morpion[0][1] + " | " + morpion[0][2])
    print("  ---+---+---")
    print("1  " + morpion[1][0] + " | " + morpion[1][1] + " | " + morpion[1][2])
    print("  ---+---+---")
    print("2  " + morpion[2][0] + " | " + morpion[2][1] + " | " + morpion[2][2])
    print(" ")

def ajouter_X(morpion):
    """
    Demande à l'utilisateur de saisir une ligne et une colonne pour ajouter une X dans un morpion.
    La fonction vérifie que la case est vide avant d'ajouter la X.
    """
    while True:
        ligne = input("Entrez le numéro de ligne (0 à 2) : ")
        colonne = input("Entrez le numéro de colonne (0 à 2) : ")
        try:
            ligne = int(ligne)
            colonne = int(colonne)
            if morpion[ligne][colonne] == " ":
                morpion[ligne][colonne] = "X"
                break
            else:
                print("Cette case n'est pas vide. Veuillez choisir une autre position.")
        except (ValueError, IndexError):
            print("Entrée invalide. Veuillez entrer un numéro de ligne et de colonne entre 1 et 3.")
    return ligne, colonne

def tourner_morpion(morpion, coefficient, ligne, colonne):
    """
    Retourne le morpion dans le sens horaire en fonction d'un coefficient de retournement.
    Le coefficient doit être un entier compris entre 1 et 4 inclus.
    La fonction retourne également les coordonnées de la ligne et de la colonne tournées.
    """
    if coefficient == 0 or coefficient == 4:
        return morpion, ligne, colonne
    elif coefficient == 1:
        nouveau_morpion = [[morpion[2-i][j] for i in range(3)] for j in range(3)]
        nouvelle_ligne = colonne
        nouvelle_colonne = 2 - ligne
    elif coefficient == 2:
        nouveau_morpion = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
        nouveau_morpion[0][0] = morpion[2][2]
        nouveau_morpion[0][1] = morpion[2][1]
        nouveau_morpion[0][2] = morpion[2][0]
        nouveau_morpion[1][0] = morpion[1][2]
        nouveau_morpion[1][1] = morpion[1][1]
        nouveau_morpion[1][2] = morpion[1][0]
        nouveau_morpion[2][0] = morpion[0][2]
        nouveau_morpion[2][1] = morpion[0][1]
        nouveau_morpion[2][2] = morpion[0][0]
        nouvelle_ligne = 2 - ligne
        nouvelle_colonne = 2 - colonne
    elif coefficient == 3:
        nouveau_morpion = [[morpion[i][2-j] for i in range(3)] for j in range(3)]
        nouvelle_ligne = 2 - colonne
        nouvelle_colonne = ligne
    else:
        raise ValueError("Le coefficient de retournement doit être un entier entre 1 et 4 inclus.")
    return nouveau_morpion, nouvelle_ligne, nouvelle_colonne



# 2 ème coup:
# si O au centre, 2 possibilités pour X (côtés, coins)
    # 2 rotations possibles (côté ou coin)
# si O sur le côté, 3 possibilités pour X (centre, côtés, coins)
# si O dans le coin, 2 possibilités pour X (centre, côtés)
    # 2 rotations possibles (centre ou 8 rotation côtés ou coins)

import os
# clear the console screen
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
import random
msg_place="A toi, j'ai placé mon O :"
msg_implication="Par implication :"
msg_implication_null="Par implication, match null :"
msg_implication_defaite="Par implication, je perds"
msg_implication_victoire="A la fin je gagne par implication, voici le morpion final :"
msg_implication_victoire_double="Ou :"
msg_morpion_original="Morpion original :"
msg_morpion_retourne="Morpion tourné pour la machine"


# Morpion : 
pos=random.randint(1,3)
if (pos==1): # O au centre, 2 possibilités pour X (côtés, coins) #Tested
    print("positions fonctionnels : Toutes\n\n")
    morpion = [
    [" ", " ", " "],
    [" ", "O", " "],
    [" ", " ", " "]]
    print(msg_place)
    afficher_morpion(morpion)
    ligne, colonne = ajouter_X(morpion)
    if morpion[1][2] == "X" or morpion[0][2] == "X": # on définit le coefficient de retournement, 0 : pas de retournement, 1 : 90°, 2 : 180°, 3 : 270°
        retournement = 4
    elif morpion[2][1] == "X" or morpion[2][2] == "X":
        retournement = 1
    elif morpion[1][0] == "X" or morpion[2][0] == "X":
        retournement = 2
    else:
        retournement = 3
    #print("Valeur du retournement (sens horaire, avec un pas de 90°) {}".format(retournement)+"\n"+msg_morpion_original+"\n"+"ligne : {} \ncolonne : {}".format(ligne, colonne)) # à commenter
    afficher_morpion(morpion)
    morpion, ligne, colonne = tourner_morpion(morpion, (4-retournement), ligne, colonne) # ajusté pour la machine
    #print(msg_morpion_retourne+"\n"+"ligne : {} \ncolonne : {}".format(ligne, colonne)) # à commenter
    #afficher_morpion(morpion) # à commenter
    if (ligne==1 and colonne==2): # O au centre X sur un côté
        morpion[0][0] = "O"
        print(msg_place) 
        morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
        afficher_morpion(morpion)
        # ["O", " ", " "]
        # [" ", "O", "X"]
        # [" ", " ", " "]
        print(msg_implication_victoire)
        morpion = [ #ajusté_ pour la machine
        ["O", "X", "O"],
        [" ", "O", "X"],
        ["O", " ", "X"]]
        morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
        afficher_morpion(morpion)
        print(msg_implication_victoire_double)
        morpion = [ #ajusté_ pour la machine
        ["O", "O", "O"],
        [" ", "X", "X"],
        ["O", " ", "X"]]
        morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
        afficher_morpion(morpion)
    else: # O au centre X sur un coin
        morpion[2][0] = "O"
        print(msg_place)
        # [" ", " ", "X"]
        # [" ", "O", " "]
        # ["O", " ", " "]
        morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
        afficher_morpion(morpion)
        ligne, colonne = ajouter_X(morpion)
        afficher_morpion(morpion)
        morpion, ligne, colonne = tourner_morpion(morpion, (4-retournement), ligne, colonne) # ajusté pour la machine
        if(ligne == 0 and colonne==0):
                morpion = [
                ["X", "O", "X"],
                [" ", "O", " "],
                ["O", " ", " "]]
                print(msg_implication_null)
                morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
                afficher_morpion(morpion)
        elif(ligne == 0 and colonne==1): # 
            morpion[2][2] = "O"
            print(msg_place)
            # [" ", "X", "X"]
            # [" ", "O", " "]
            # ["O", " ", "O"]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion = [
            ["X", " ", "X"],
            [" ", "O", " "],
            ["O", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            ["O", "X", "X"],
            [" ", "O", " "],
            ["O", "X", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif (ligne==1 and colonne==2): #  
            morpion[2][2] = "O"
            print(msg_place)
            # [" ", " ", "X"]
            # [" ", "O", "X"]
            # ["O", " ", "O"]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire) 
            morpion = [
            ["X", " ", "X"],
            [" ", "O", "X"],
            ["O", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            ["O", " ", "X"],
            [" ", "O", "X"],
            ["O", "X", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne == 1 and colonne==0): # 
                    morpion[2][2] = "O"
                    print(msg_place)
                    # [" ", " ", "X"]
                    # ["X", "O", " "]
                    # ["O", " ", "O"]
                    morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
                    afficher_morpion(morpion)
                    print(msg_implication_victoire)
                    morpion = [
                    ["X", " ", "X"],
                    ["X", "O", " "],
                    ["O", "O", "O"]]
                    morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
                    afficher_morpion(morpion)
                    print(msg_implication_victoire_double)
                    morpion = [
                    ["O", " ", "X"],
                    ["X", "O", " "],
                    ["O", "X", "O"]]
                    morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
                    afficher_morpion(morpion)
        elif(ligne==2 and colonne==1): # 
            morpion[0][0] = "O"
            print(msg_place)
            # ["O", " ", "X"]
            # [" ", "O", " "]
            # ["O", "X", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire) 
            morpion = [
            ["O", " ", "X"],
            ["X", "O", " "],
            ["O", "X", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            ["O", " ", "X"],
            ["O", "O", " "],
            ["O", "X", "X"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)     
        elif(ligne == 2 and colonne==2):
            morpion = [
            [" ", " ", "X"],
            [" ", "O", "O"],
            ["O", " ", "X"]]
            print(msg_implication_null)
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        
elif (pos==2): # O sur le côté, 3 possibilités pour X (centre, côtés, coins) peut être pas côtés
    print("positions fonctionnels : 0 1 | 0 2| 1 1\n\n")
    morpion = [
    [" ", " ", " "],
    [" ", " ", "O"],
    [" ", " ", " "]]
    print(msg_place)
    afficher_morpion(morpion)
    ligne, colonne = ajouter_X(morpion)
    if morpion[0][1] == "X" or morpion[0][2] == "X" or morpion[1][1] == "X": # 
        retournement = 4
    #print("Valeur du retournement (sens horaire, avec un pas de 90°) {}".format(retournement)+"\n"+msg_morpion_original+"\n"+"ligne : {} \ncolonne : {}".format(ligne, colonne)) # à commenter
    afficher_morpion(morpion)
    morpion, ligne, colonne = tourner_morpion(morpion, (4-retournement), ligne, colonne) # ajusté pour la machine
    #print(msg_morpion_retourne+"\n"+"ligne : {} \ncolonne : {}".format(ligne, colonne)) # à commenter
    #afficher_morpion(morpion) # à commenter
    if (ligne==0 and colonne==1): # O sur le côté X sur un côté
        morpion[2][0] = "O"
        print(msg_place) 
        morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
        afficher_morpion(morpion)
        # [" ", "X", " "]
        # [" ", " ", "O"]
        # ["O", " ", " "]
        ligne, colonne = ajouter_X(morpion)
        afficher_morpion(morpion)
        morpion, ligne, colonne = tourner_morpion(morpion, (4-retournement), ligne, colonne) # ajusté pour la machine
        if (ligne==0 and colonne==0): # Tested - 
            morpion[0][2] = "O"
            print(msg_place)
            # ["X", "X", "O"]
            # [" ", " ", "O"]
            # ["O", " ", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire) 
            morpion = [
            ["X", "X", "O"],
            [" ", "X", "O"],
            ["O", " ", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            ["X", "X", "O"],
            [" ", "O", "O"],
            ["O", " ", "X"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==1 and colonne==0): # Tested
            morpion[0][2] = "O"
            print(msg_place)
            # [" ", "X", " "]
            # ["X", " ", "O"]
            # ["O", " ", "O"]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire) 
            morpion = [
            [" ", "X", "X"],
            ["X", " ", "O"],
            ["O", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            [" ", "X", "O"],
            ["X", " ", "O"],
            ["O", "X", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            [" ", "X", "O"],
            ["X", "O", " "],
            ["O", "X", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne == 2 and colonne==1): # Tested
            morpion[1][1] = "O"
            print(msg_place)
            # [" ", "X", " "]
            # [" ", "O", "O"]
            # ["O", "X", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion = [
            [" ", "X", "O"],
            ["X", "O", "O"],
            ["O", "X", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            [" ", "X", "X"],
            ["O", "O", "O"],
            ["O", "X", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==2 and colonne==2): # Tested
            morpion[1][1] = "O"
            print(msg_place)
            # [" ", "X", " "]
            # [" ", "O", "O"]
            # ["O", " ", "X"]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion = [
            [" ", "X", "O"],
            ["X", "O", "O"],
            ["O", " ", "X"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            [" ", "X", "X"],
            ["O", "O", "O"],
            ["O", " ", "X"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne == 1 and colonne==1): # Tested
            morpion = [
            ["O", "X", "O"],
            ["X", "X", "O"],
            ["O", "O", "X"]]
            print(msg_implication_null)
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne == 0 and colonne==2): # Tested
            morpion = [
            ["O", "X", "X"],
            [" ", " ", "O"],
            ["O", " ", " "]]
            print(msg_implication_null)
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
    elif(ligne==0 and colonne==2): # O sur le côté X sur un coin
        morpion[2][0] = "O"
        print(msg_place) 
        morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
        afficher_morpion(morpion)
        # [" ", " ", "X"]
        # [" ", " ", "O"]
        # ["O", " ", " "]
        ligne, colonne = ajouter_X(morpion)
        afficher_morpion(morpion)
        morpion, ligne, colonne = tourner_morpion(morpion, (4-retournement), ligne, colonne) # ajusté pour la machine
        if(ligne==0 and colonne==0): # Done
            morpion[0][1] = "O"
            print(msg_place)
            # ["X", "O", "X"]
            # [" ", " ", "O"]
            # ["O", " ", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion=[
            ["X", "O", "X"],
            [" ", " ", "O"],
            ["O", " ", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==1 and colonne==0): # Done
            morpion[0][0] = "O"
            print(msg_place)
            # ["O", " ", "X"]
            # ["X", " ", "O"]
            # ["O", " ", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion=[
            ["O", " ", "X"],
            ["X", " ", "O"],
            ["O", " ", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==0 and colonne==1): # Done
            morpion[0][0] = "O"
            print(msg_place)
            # ["O", "X", "X"]
            # [" ", " ", "O"]
            # ["O", " ", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion=[
            ["O", "X", "X"],
            ["X", "X", "O"],
            ["O", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion=[
            ["O", "X", "X"],
            ["X", "O", "O"],
            ["O", "X", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==1 and colonne==1): # Done
            morpion[0][0] = "O"
            print(msg_place)
            # ["O", " ", "X"]
            # [" ", "X", "O"]
            # ["O", " ", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion=[
            ["O", " ", "X"],
            ["X", "X", "O"],
            ["O", " ", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==2 and colonne==1): # Done
            morpion[1][0] = "O"
            print(msg_place)
            # [" ", " ", "X"]
            # ["O", " ", "O"]
            # ["O", "X", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion=[
            ["X", " ", "X"],
            ["O", "O", "O"],
            ["O", "X", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion=[
            ["O", " ", "X"],
            ["O", "X", "O"],
            ["O", "X", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==2 and colonne==2): # Done
            morpion[1][0] = "O"
            print(msg_place)
            # [" ", " ", "X"]
            # ["O", " ", "O"]
            # ["O", " ", "X"]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion=[
            ["X", " ", "X"],
            ["O", "O", "O"],
            ["O", " ", "X"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion=[
            ["O", " ", "X"],
            ["O", "X", "O"],
            ["O", " ", "X"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
    elif(ligne==1 and colonne==1): # O sur le côté X au centre
        morpion[2][0] = "O"
        print(msg_place) 
        morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
        afficher_morpion(morpion)
        # [" ", " ", " "]
        # [" ", "X", "O"]
        # ["O", " ", " "]
        ligne, colonne = ajouter_X(morpion)
        afficher_morpion(morpion)
        morpion, ligne, colonne = tourner_morpion(morpion, (4-retournement), ligne, colonne) # ajusté pour la machine
        if(ligne==1 and colonne==0): # Tested
            morpion[2][2] = "O"
            print(msg_place)
            # [" ", " ", " "]
            # ["X", "X", "O"]
            # ["O", " ", "O"]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion=[
            [" ", " ", "O"],
            ["X", "X", "O"],
            ["O", "X", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion=[
            [" ", " ", "X"],
            ["X", "X", "O"],
            ["O", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==0 and colonne==0): # Tested
            morpion[2][2] = "O"
            print(msg_place)
            # ["X", " ", " "]
            # [" ", "X", "O"]
            # ["O", " ", "O"]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion=[
            ["X", " ", "O"],
            [" ", "X", "O"],
            ["O", "X", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion=[
            ["X", " ", "X"],
            [" ", "X", "O"],
            ["O", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==0 and colonne==1): # Tested
            morpion[2][1] = "O"
            print(msg_place)
            # [" ", "X", " "]
            # [" ", "X", "O"]
            # ["O", "O", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion=[
            ["O", "X", "O"],
            ["X", "X", "O"],
            ["O", "O", "X"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==0 and colonne==2): # Tested
            morpion[0][0] = "O"
            print(msg_place)
            # ["O", " ", "X"]
            # [" ", "X", "O"]
            # ["O", " ", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion=[
            ["O", " ", "X"],
            [" ", "X", "O"],
            ["O", " ", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==2 and colonne==1): # Tested
            morpion[0][1] = "O"
            print(msg_place)
            # [" ", "O", " "]
            # [" ", "X", "O"]
            # ["O", "X", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion=[
            [" ", "O", " "],
            [" ", "X", "O"],
            ["O", "X", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==2 and colonne==2): # Tested
            morpion[0][0] = "O"
            print(msg_place)
            # ["O", " ", " "]
            # [" ", "X", "O"]
            # ["O", " ", "x"]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion=[
            ["O", " ", " "],
            ["X", "X", "O"],
            ["O", " ", "X"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        else: print("Je suis encore en phase d'apprentissage il me manque 7 possibilités à maîtriser")
elif (pos==3): # O sur le coin, 2 possibilités pour X (centre, côtés)
    print("positions fonctionnels : 0 1 | 1 1\n\n")
    morpion = [
    [" ", " ", "O"],
    [" ", " ", " "],
    [" ", " ", " "]]
    print(msg_place)
    afficher_morpion(morpion)
    ligne, colonne = ajouter_X(morpion)
    if morpion[0][1] == "X" or morpion[1][1] == "X": # 
        retournement = 4
    #print("Valeur du retournement (sens horaire, avec un pas de 90°) {}".format(retournement)+"\n"+msg_morpion_original+"\n"+"ligne : {} \ncolonne : {}".format(ligne, colonne)) # à commenter
    afficher_morpion(morpion)
    morpion, ligne, colonne = tourner_morpion(morpion, (4-retournement), ligne, colonne) # ajusté pour la machine
    #print(msg_morpion_retourne+"\n"+"ligne : {} \ncolonne : {}".format(ligne, colonne)) # à commenter
    #afficher_morpion(morpion) # à commenter
    if (ligne==0 and colonne==1): # O sur le coin X sur le côté
        morpion[2][1] = "O"
        print(msg_place) 
        morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
        afficher_morpion(morpion)
        # [" ", "X", "O"]
        # [" ", " ", " "]
        # [" ", "O", " "]
        ligne, colonne = ajouter_X(morpion)
        afficher_morpion(morpion)
        morpion, ligne, colonne = tourner_morpion(morpion, (4-retournement), ligne, colonne) # ajusté pour la machine
        if(ligne==0 and colonne==0): # Tested
            morpion[2][2] = "O"
            print(msg_place)
            # ["X", "X", "O"]
            # [" ", " ", " "]
            # [" ", "O", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion = [
            ["X", "X", "O"],
            [" ", " ", "O"],
            ["X", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            ["X", "X", "O"],
            [" ", " ", "X"],
            ["O", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==1 and colonne==0): # Tested
            morpion[2][2] = "O"
            print(msg_place)
            # [" ", "X", "O"]
            # ["X", " ", " "]
            # [" ", "O", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion = [
            [" ", "X", "O"],
            ["X", " ", "O"],
            ["X", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            [" ", "X", "O"],
            ["X", " ", "X"],
            ["O", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==1 and colonne==1): # Tested
            morpion[2][2] = "O"
            print(msg_place)
            # [" ", "X", "O"]
            # [" ", "X", " "]
            # [" ", "O", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion = [
            [" ", "X", "O"],
            [" ", "X", "O"],
            ["X", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            [" ", "X", "O"],
            [" ", "X", "X"],
            ["O", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==1 and colonne==2): # Tested
            morpion[1][1] = "O"
            print(msg_place)
            # [" ", "X", "O"]
            # [" ", "O", "X"]
            # [" ", "O", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion = [
            [" ", "X", "O"],
            [" ", "O", "X"],
            ["X", "O", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==2 and colonne==0): # Tested
            morpion[2][2] = "O"
            print(msg_place)
            # [" ", "X", "O"]
            # [" ", " ", " "]
            # ["X", "O", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion = [
            [" ", "X", "O"],
            [" ", " ", "X"],
            ["X", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==2 and colonne==2): # Tested
                morpion[1][1] = "O"
                print(msg_place)
                # [" ", "X", "O"]
                # [" ", "O", " "]
                # [" ", "O", "X"]
                morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
                afficher_morpion(morpion)
                print(msg_implication_null)
                morpion = [
                [" ", "X", "O"],
                [" ", "O", " "],
                [" ", "O", "X"]]
                morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
                afficher_morpion(morpion)
        else: print("Je suis encore en phase d'apprentissage il me manque 7 possibilités à maîtriser")
    elif(ligne==1 and colonne==1): # O sur le coin X sur le centre
        morpion[2][1] = "O"
        print(msg_place) 
        morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
        afficher_morpion(morpion)
        # [" ", " ", "O"]
        # [" ", "X", " "]
        # [" ", "O", " "]
        ligne, colonne = ajouter_X(morpion)
        afficher_morpion(morpion)
        morpion, ligne, colonne = tourner_morpion(morpion, (4-retournement), ligne, colonne) # ajusté pour la machine
        if(ligne==0 and colonne==0): # Tested
            morpion[2][2] = "O"
            print(msg_place)
            # ["X", " ", "O"]
            # [" ", "X", " "]
            # [" ", "O", "O"]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire)
            morpion = [
            ["X", " ", "O"],
            [" ", "X", "O"],
            ["X", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_victoire_double)
            morpion = [
            ["X", "X", "O"],
            [" ", "X", "X"],
            ["O", "O", "O"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==0 and colonne==1): # tested
                morpion[2][2] = "O"
                print(msg_place)
                # [" ", "X", "O"]
                # [" ", "X", " "]
                # [" ", "O", "O"]
                morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
                afficher_morpion(morpion)
                print(msg_implication_victoire)
                morpion = [
                [" ", "X", "O"],
                [" ", "X", "X"],
                ["O", "O", "O"]]
                morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
                afficher_morpion(morpion)
                print(msg_implication_victoire_double)
                morpion = [
                [" ", "X", "O"],
                [" ", "X", "O"],
                ["X", "O", "O"]]
                morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
                afficher_morpion(morpion)
        elif(ligne==1 and colonne==0): # Tested
            morpion[1][2] = "O"
            print(msg_place)
            # [" ", " ", "O"]
            # ["X", "X", "O"]
            # [" ", "O", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion = [
            ["O", "X", "O"],
            ["X", "X", "O"],
            ["O", "O", "X"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==1 and colonne==2): # Tested
            morpion[1][0] = "O"
            print(msg_place)
            # [" ", " ", "O"]
            # ["O", "X", "X"]
            # [" ", "O", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion = [
            [" ", " ", "O"],
            ["O", "X", "X"],
            [" ", "O", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==2 and colonne==0): # Tested
            morpion[0][0] = "O"
            print(msg_place)
            # [" ", " ", "O"]
            # [" ", "X", " "]
            # ["X", "O", " "]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion = [
            ["O", " ", "O"],
            [" ", "X", " "],
            ["X", "O", " "]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        elif(ligne==2 and colonne==2): # Tested
            morpion[0][0] = "O"
            print(msg_place)
            # ["O", " ", "O"]
            # [" ", "X", " "]
            # [" ", "O", "X"]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
            print(msg_implication_null)
            morpion = [
            ["O", "X", "O"],
            [" ", "X", " "],
            [" ", "O", "X"]]
            morpion, ligne, colonne = tourner_morpion(morpion, retournement, ligne, colonne) # désajusté pour la machine
            afficher_morpion(morpion)
        else: print("Erreur position 3 centre")

