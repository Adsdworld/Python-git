# essai Piles
from File import File

fileGalettes = File(5)
fileCrepes = File(5)

dicCrepes = {1:"crêpe sucre",2:"crêpe confiture",3:"crêpe nutella", 4:"crêpe chantilly"}
dicGalettes = {1:"galette jambon",2:"galette andouillette",3:"galette complète",4:"galette raclette"}  

while True :
    print("Bonjour, que souhaitez-vous commander ?")
    print("Du salé ou du sucré")
    choix =0
    # ajouter les controles de saisie/exception
    while choix < 1 or choix > 3 :
        try:
            choix = int(input("1 pour salé, 2 pour sucré, 3 pour l'addition : "))
        except ValueError :
                print("Erreur de saisie, ce n'est pas un nombre")
                
    if choix == 1:
        i=1
        for cle, galette in dicGalettes.items():
            print(cle, " ", galette)
        '''for galette in dicGalettes:
            print(i," ",dicGalettes[galette])
            i+=1'''
        choix=0
        while choix < 1 or choix > len(dicGalettes) :
            try:
                choix = int(input("quel est votre choix ?"))
                fileGalettes.ajouter(choix)
            except ValueError :
                    print("Erreur de saisie, ce n'est pas un nombre")

    elif choix == 2 :
        i=1
        for crepe in dicCrepes:
            print(i," ",dicCrepes[crepe])
            i+=1
        choix=0
        while choix < 1 or choix > len(dicCrepes) :
            try:
                choix = int(input("quel est votre choix ?"))
                fileCrepes.ajouter(choix)
            except ValueError :
                print("Erreur de saisie, ce n'est pas un nombre")

    else :
        print("\nC'est cadeau !!")
        break
    
    if fileCrepes.estPleine() == True :
        print(fileCrepes)
        print("\nIl est temps de servir les crêpes")
        while fileCrepes.estVide() == False:
            print("\tLa", dicCrepes[fileCrepes.recupererPremier()],"est servie")
            fileCrepes.enlever()
            print(fileCrepes)
        print("")

    if fileGalettes.estPleine() == True :
        print("\nIl est temps de servir les galettes")
        while fileGalettes.estVide() == False:
            print("\tLa", dicGalettes[fileGalettes.recupererPremier()],"est servie")
            fileGalettes.enlever()
            print(fileGalettes)

print("\nAu revoir et à bientôt !")
