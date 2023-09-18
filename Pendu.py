#non fonctionnel

dictionnaire={1:"bonjour"}

print(dictionnaire)

def pendu(mot):
    mot=mot.upper()
    début_du_mot=mot[0]
    fin_du_mot=mot[len(mot)-1]

    mot_à_deviner=début_du_mot+"-"*(len(mot)-2)+fin_du_mot
    print(mot_à_deviner)
    
    stop1=True
    while stop1:
        stop2=True
        lettre = input("Entrez une lettre")
        while stop2:
            if (lettre[0] != 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
                lettre=lettre[0].upper()
                stop2=False
            else:
                lettre = input("Votre premier caractère ne correspondait pas à une lettre, vous devez entrez une lettre")
            
        positions = []
        for index, caractere in enumerate(mot):
            if caractere == lettre:
                positions.append(index)
        
        mot_à_deviner = début_du_mot
        for i in range(len(mot)):
            if (i+1) in positions:
                mot_à_deviner=mot_à_deviner+lettre
            elif (i==0):
                mot_à_deviner=mot_à_deviner+"-"
        mot_à_deviner = mot_à_deviner+fin_du_mot
        print(mot_à_deviner)
        if not "-" in mot_à_deviner:
            print("Le mot à été deviné")
            stop1=False
    



pendu(dictionnaire[1])    