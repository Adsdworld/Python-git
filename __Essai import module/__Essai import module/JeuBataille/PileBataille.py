import sys
sys.path.append("..")
from PackagePile.Pile import Pile

listeCartes = []
with open ("ListeCartes.txt", "r",encoding='utf8') as cartes :
    for ligne in cartes:
        tab = ligne.split(",")
        tab[1] = int(tab[1])
        listeCartes.append(tab)

pileJ1 = Pile(32)
pileJ2 = Pile(32)

nb=0
while nb < len(listeCartes) :
    pileJ1.empiler(listeCartes[nb])
    pileJ2.empiler(listeCartes[nb+1])
    nb+=2
    print(nb)

print("Main du joueur 1", pileJ1)
print("Main du joueur 2", pileJ2)
