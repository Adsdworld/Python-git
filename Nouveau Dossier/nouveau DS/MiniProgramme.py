# de Sallier Dupin Arthur
# Examen du 06/11/2023

def calculerPuissance():
    while True:# saisir un entier entre 6 et 14
            try:
                CV=int(input("Quelle est la puissance de votre véhicule (entre 6 et 14 CV)?\n"))
                if not(5<CV<15):
                    raise Exception("Erreur de saisie recommencer")
                break
            except Exception as err:
                print(err)
    return CV

def calculerVitesse():
    while True:# saisir un entier entre 0 et 150
            try:
                vitesse=int(input("Quelle est votre vitesse (inférieur à 150km)?\n"))
                if not(-1<vitesse<150):
                    raise Exception("Erreur de saisie recommencer")
                break
            except Exception as err:
                print(err)
    return vitesse

def calculerConsommation(CV, vitesse):
    if CV<7:
        if vitesse<50:
            conssomation=6.5
        elif 49<vitesse<90:
            conssomation=4.5
        else:
            conssomation=8
    else:
        if vitesse<50:
            conssomation=7.2
        elif 49<vitesse<90:
            conssomation=8
        else:
            conssomation=8.5
    print("Votre conssomation est de: {} litres/100km".format(conssomation))

def demarrerProg():
    print("Bienvenue dans notre programme de calcul de conssomation de véhicule")
    while True:    
        CV=calculerPuissance()
        vitesse=calculerVitesse()
        calculerConsommation(CV, vitesse)
        stop=True
        while stop:
            try:
                choice=input("Souhaiter vous faire un autre calcul\nTaper '1' pour Oui:\n")
                if choice!='1':
                    print("Fermeture du programme")
                    quit()
                else:
                    stop=False
            except:
                print("Erreur de saisie recommencer")

demarrerProg()
