# @Arthur De Sallier Dupin
# Cochon Qui Rit



restart = True
from random import randint

show = input("Souhaitez vous lire les règles de la partie ? laisser vide pour passer")
if show != "":
    print("Voici les règles :\n\tFaites un 6 pour récupérer le corp du cochon,\n\tAprès 2 as vous récupérer les yeux,\n\tA 4 les oreilles,\n\tA 8 les pattes,\n\tEnfin à 10 la queue !")

name = input("Quel est ton nom ?")

while restart:

    print("Bienvenue dans Cochon Qui Rit !")
    
    nombre_de_tours = 0 #compte le nombre de lancés
    play = True # control de la boucle principale
    dé_Liste = [] # permet de stocker les valeurs des dés
    corp = False
    eyes = False
    ears = False
    legs = False
    queue = False
    nombre_de_1=0
    
    

    while play:    
        for j in range(0,2): # on effectue 1 lancé de 3 dés
            dé_Liste.append(randint(1, 6))
        nombre_de_tours+=1
        if corp == False:
            for i in dé_Liste:
                if i == 6:
                    corp=True
                    dé_Liste.remove(6)
                if corp == True:
                    if i == 1:
                        nombre_de_1+=1
                        dé_Liste.remove(1)
        else:
            for i in dé_Liste:
                if i == 1:
                    nombre_de_1+=1
                    dé_Liste.remove(1)
            choice_available = ''
            if nombre_de_1 >=4:
                if (eyes==False or ears==False or queue == False) and nombre_de_1>=2:
                    if eyes == False:
                        choice_available+='eyes '
                    if ears == False:
                        choice_available+='ears '
                    if queue == False:
                        choice_available+='queue '
                if (legs==False) and nombre_de_1>=4:
                    choice_available+='legs '
                if (corp == True and eyes==True and ears == True and queue==True and legs==True):
                    break
                choice = input("choisissez parmis : {}".format(choice_available))
                
                while True:
                    if choice in choice_available:
                        if choice == 'eyes':
                            eyes = True
                            nombre_de_1-=2
                        if choice == 'ears':
                                ears = True
                                nombre_de_1-=2
                        if choice == 'queue':
                                queue = True
                                nombre_de_1-=2
                        if choice == 'legs':
                                legs = True
                                nombre_de_1-=4
                        print ("corp :", corp,"\n""eyes :", eyes,"\n""ears :", ears,"\n""queue :", queue,"\n""legs :", legs,"\n")
                        break
                    else:
                        choice = input("choisissez parmis : {}".format(choice_available))

    print("Bravo {}, nombre d'essais totaux : {}".format(name, nombre_de_tours))

    input = input("Voulez vous rejouer ? laisser vide pour quitter")
    if input != '':
        print("Rejouons !")
    else:
        print("exit")
        restart=False
        



def Select_part(nb_6, nb_1):
    used_6 = 0
    as_used = 0
    if corp == True:
        used_6+=1
    if eyes == True:
        as_used+=2
    if ears == True:
        as_used+=2
    if queue == True:
        as_used+=4
    if queue == True:
        as_used+=2
    





        





#while corp==False:
#    for i in range(0,2):
#    dé_aléatoire = randint(1, 6)
#    nombre_de_tours=nombre_de_tours+1
#    if dé_aléatoire == 6:
#        print("Bravo, vous récupérer le corp du cochon !")
#        corp = True
#        while as_compteur<10:
#            dé_aléatoire = randint(1, 6)
#            nombre_de_tours=nombre_de_tours+1
#            if dé_aléatoire == 1:
#                as_compteur= as_compteur+1
#                print("{}/10".format(as_compteur))
#print("Fin de la partie, nombre d'essais totaux : {}".format(nombre_de_tours))