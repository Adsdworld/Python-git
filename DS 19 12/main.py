#Arthur de Sallier Dupin P2 E2
from time import sleep
import os
import random
from modules import *
os.system('cls')
import ctypes
import platform
def is_windows():
    return platform.system().lower() == 'windows'
def change_color():
    if is_windows():
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 8 | (8 << 4))
change_color()


"""#"Last Chance Gas" de Al, qui est la dernière de la route 190 menant à la vallée de la mort. 
La station services "Last Chance Gas" de Al est donc la dernière de la route 190 menant à la vallée de la mort et il n'y
a plus d'autres stations à moins de 350 kilomètres. """






def lancertestdecarburant():
    print("Lancement du programme de controle du niveau de carburant")
    capacite = ask_int("Saisir la capacité du réservoir (par exemple 60L): ", "Veuillez saisir un nombre entier au format 'X'L")
    while True:
        jauge_en_pourcentage = ask_int("Saisir le pourcentage de la jauge (par exemple 30%): ", "Veuillez saisir un nombre entier au format 'X'%")
        if 0 < jauge_en_pourcentage > 100:
            print("Vous avez saisie une valeur supérieur à 100%, ce qui n'est pas concevable, veuillez réessayer")
        else:
            break
    conssomation = ask_int("Saisir la conssomation pour 100km (par exemple 5L/100km): ", "Veuillez saisir un nombre entier au format 'X'L/100")
    return controlerCarburant(capacite, jauge_en_pourcentage, conssomation)

def PreLaunchforPression():
    controlerPression()



def menu():
    print("Bonjour et bienvenue dans la station service d'AI ***Last Chance GAS ***")
    while True:
        choix_int = ask_int("Quelle opération souhaitez vous faire?\n\tTaper 1 pour controller votre niveau de carburant\n\tTaper 2 pour controller la pression des pneus\n\tTaper 3 pour ouvrir le magasin\n\tTaper 4 pour quitter le programme\nVotre choix: ", "Veuillez taper 1 ou 2 ou 3")
        if choix_int == 1 or 2 or 3:
            if choix_int == 1:
                lancertestdecarburant()
            if choix_int == 2:
                PreLaunchforPression()
            if choix_int == 3:
                magasin()
            if choix_int == 4:
                print("Par mesure de précaution, avant de quitter le programme, faisons une vérification de votre niveau de carburant")
                if lancertestdecarburant()>=350:
                    break
                else:
                    print("Oups, on dirait que vous n'avez pas suffisament de carburant pour faire la route, faites le plein")
    print("Bonne route et à bientôt ... peut-être")
menu()