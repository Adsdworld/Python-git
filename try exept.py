def division():
    try:
        x=int(input("entrer le numérateur"))
        y=int(input("entrer le dénominateur"))
        résultat=x/y
        if y==0:
            raise Exception("Division par 0 impossible...")   
    except ValueError:
        print("Vous devez enter des chiffres")
    except Exception as e:
        print(e)
        print(type(e))
    else:
        print("Le résultat de la division est: {}".format(résultat))
    finally:
        print("Fin de l'éxécution de la fonction division")
#division()



import random
def placerMines():
    # remplissage aléatoire du champs de mines
    # True, une case avec une bombe, False, une case vide
    mines=[[str(random.choice(['X', 'O'])) for j in range(10)] for i in range(10)]
    return mines

# fonction qui permet de savoir si on a choisi une case occupée ou pas
def boumOuPasBoum(champ,ligne,colonne) :
    if champ[ligne][colonne] =="X": #sous-entendu champ[ligne][colonne]== True
        print("BOUM !! Perdu !")
        return True
    else :
        return False
    
# fonction qui permet de savoir combien de bombes entoure la case choisie
# 8 cases à tester maxi
def rechercherMines(champ,ligne,colonne) :
    res=0
    # double boucle qui parcourt les 8 voisins de la case choisie
    # et additionne les boums trouvées (maxi 8) if champ[ligne][colonne] : res=res+1
    #print("TODO code à réaliser")
    try:
        for i in range(2):
            if champ[ligne-1+i][colonne-1]=='X':
                #print("champ[ligne-1+{}][colonne-1]: {}".format(i, champ[ligne-1+i][colonne-1]))
                res+=1
    except IndexError:
        print()
    try:
        for i in range(2):
            if champ[ligne-1+i][colonne+1]=='X':
                #print("champ[ligne-1+{}][colonne+1]: {}".format(i, champ[ligne-1+i][colonne+1]))
                res+=1
    except IndexError:
        print()
    try:
        for i in range(2):
            if champ[ligne-1][colonne-1+i]=='X':
                #print("champ[ligne-1][colonne-1+{}]: {}".format(i, champ[ligne-1][colonne-1+i]))
                res+=1
    except IndexError:
        print()
    try:
        for i in range(2):
            if champ[ligne+1][colonne-1+i]=='X':
                #print("champ[ligne+1][colonne-1+{}]: {}".format(i, champ[ligne+1][colonne-1+i]))
                res+=1
    except IndexError:
        print()
    

    return res

# fonction qui permet de savoir combien on a de bombes dans le champ
def compterMines(champ) :
    res=0
    for i in range(10) :
        for j in range(10) :
            if champ[i][j]:
                res = res+1
    print(res)
    return res
# fonction qui permet d’afficher le champ – UNIQUEMENT EN PHASE DE TEST
def afficherMines(champ) :
    for k in range(10):
        print("{}|{}|{}|{}|{}|{}|{}|{}|{}".format(champ[k][0],champ[k][1],champ[k][2],champ[k][3],champ[k][4],champ[k][5],champ[k][6],champ[k][7],champ[k][8],champ[k][9]))
    print()

# fonction qui contient le déroulement du jeu
def jouer() :
    ligne=0
    colonne=0
    nbmines=0
    # on rempli le "tableau" avec les mines
    champ= placerMines()
    # on affiche les mines pour tester le jeu
    afficherMines(champ)
    # Pour savoir combien on a de mines dans le jeu
    # compterMines(champ)
    while True:
        # gérer les exceptions liées à la saisie de l'utilisateur
        print("Entrez le numéro de la ligne choisie : ")
        ligne = int(input())
        print("{}|{}|{}|{}|{}|{}|{}|{}|{}".format(champ[ligne][0],champ[ligne][1],champ[ligne][2],champ[ligne][3],champ[ligne][4],champ[ligne][5],champ[ligne][6],champ[ligne][7],champ[ligne][8],champ[ligne][9]))
        print("Entrez le numéro de la colonne choisie : ")
        colonne = int(input())
        # Créer une exception spécifique si le joueur tombe sur une bombe
        # partie de code à modifier en conséquence
        try:
            if boumOuPasBoum(champ,ligne,colonne) :
                raise Exception("EXPLOZZION !!!!")
        except Exception as err:
            #print(err)
            #print(type(err))
            print("Partie finie !")
            break

        nbmines = rechercherMines (champ,ligne ,colonne ) ;
        print("Nombre de mines : ", nbmines )
        # en fin de "tour", afficher les cases déjà choisies
        #gérer la fin de partie (quand la partie s'arrête-t-elle si le joueur ne fait pas BOUM)
jouer()
