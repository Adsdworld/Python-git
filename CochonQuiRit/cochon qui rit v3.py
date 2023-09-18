# @Arthur De Sallier Dupin
# Cochon Qui Rit v3


# bug quand on obtient 2as on à 2 fois les choix--> ok
# bug lors de la boucle--> à tester
# bug 2 as pour la queue--> à tester
# bug as avec le premier 6--> à tester

rejouer = True #permet de rejouer une fois la partie gagnée
play = True #permet d'arrêter la partie si quelqu'un gagne
from random import randint
from time import sleep

def afficher_les_règles():
    choice = input("Voulez vous afficher les règles? laisser vide pour quitter")
    if choice != "":
        print("Bienvenue. Vous allez jouer à \"Cochon qui rit\" !\nSouhaitez-vous voir les règles du jeu ? Tapez \"O\" ou \"o\" pour les voir\nO\n*** Règles : ***\nLe but du jeu est de reconstituer son cochon\nPour cela, vous allez jeter 3 dés à chaque tour\nSuivant votre lancer, vous pourrez récupérer\ndifférentes parties du corps de votre cochon\nLe joueur va devoir récupérer le corps, 4 pattes, 2 oreilles, 2 yeux et 1 queue\nPour commencer, faire un 6 pour récupérer le corps de votre cochon\nFaire un as pour récupérer une patte, une oreille ou un oeil\nFaire deux as pour la queue\nTant qu'un joueur fait des as, il peut relancer\n*** A vous de jouer ***")

def print_joueur_data(data,player): #permet d'afficher les objets possédés par un joueur
    for keys in data:
        if player in keys:
            print("\t{}: {}".format(keys, data[keys]))


while rejouer:
    while True:
        print("Bienvenue. Vous allez jouer à \"Cochon qui rit\" !")
        afficher_les_règles()
        
        while True:
            player_list=[]
            choice = int(input("Combien de joueurs êtes vous? Entrer un nombre entre 2 et 4")) #récupérer le nombre et les noms des joueurs dans une liste
            if 1<choice<5:
                for i in range(choice):
                    i+=1
                    choice = input("Joueur {}, choississez un nom".format(i))
                    player_list.append(choice)
                break
        data = {}
        for i in player_list: #ajouter les objets/informations des joueurs dans un dictionnaire utilisé comme base de données
            print("C'est à {} de jouer".format(i))
            data[i+'corp'] = 0
            data[i+'eyes'] = 0
            data[i+'ears'] = 0
            data[i+'legs'] = 0
            data[i+'queue'] = 0
            data[i+'points'] = 0
            data[i+'tours'] = 0
            #print_joueur_data(data, players)

        while play:
            for players in player_list:
                dé_list = [] #stocke les résultats d'un lancé de 3 dés
                for i in range(3
                               
                               ):
                    dé_list.append(randint(1, 6))
                sleep(2)
                data[players+'tours'] +=1
                print("{} obtient: {}".format(players, dé_list))
                
                if data[players+'corp']==1:
                    for i in dé_list:
                        if i == 1:
                            data[players+'points'] +=1 #compte le nombre de points (=as), à condition que le joueur ait le corp
                else:
                    for i in dé_list:
                        if data[players+'corp']==0:
                            if i == 6:
                                for k in dé_list:
                                    if k == 1:
                                        data[players+'points'] +=1
                                data[players+'corp'] =1

                del dé_list
                while True:
                    if data[players+'points'] > 0: #si le joueurs à des points on récupère les choix disponible et on lui demande de choisir des objets
                        choice_available=''
                        if data[players+'corp']<1:
                            choice_available+='corp '
                        if data[players+'eyes']<2:
                            choice_available+='eyes '
                        if data[players+'ears']<2:
                            choice_available+='ears '
                        if data[players+'legs']<4:
                            choice_available+='legs '
                        if data[players+'queue']==0:
                            if data[players+'points']>1:
                                choice_available+='queue '
                        if choice_available == 'queue ' and data[players+'points']<1:
                            print("{} plus qu'un as pour avoir la queue".format(players))
                            print_joueur_data(data, players) 
                            break
                        print("Vous pouvez choisir parmis: {}".format(choice_available))
                        choice = input("Choix de {}:".format(players))
                        if choice in choice_available:
                            if choice == 'corp':
                                data[players+'corp'] +=1
                                data[players+'points'] -=1
                            if choice == 'eyes':
                                data[players+'eyes'] +=1
                                data[players+'points'] -=1
                            if choice == 'ears':
                                data[players+'ears'] +=1
                                data[players+'points'] -=1
                            if choice == 'legs':
                                data[players+'legs'] +=1
                                data[players+'points'] -=1
                            if choice == 'queue':
                                data[players+'queue'] +=2
                                data[players+'points'] -=2
                    else: #arrivé ici, le joueur à épuisé ses points, on affiche son 'inventaire'
                        print_joueur_data(data, players) 
                        break
                if data[players+'corp'] == 1 and data[players+'eyes'] == 2 and data[players+'ears'] == 2 and data[players+'legs'] == 4 and data[players+'queue'] == 2:
                    play = False
                    print("{} à gagné, Bravo à lui".format(players))

                            
                    
choice = input("Voulez vous rejouer? laisser vide pour quitter")
if choice == "":
    rejouer = False
else:
    play=True
