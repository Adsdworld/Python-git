
import os
os.system('color 5')
os.system('cls')
os.system('cd ..')
from Ask_module import *


from Pile import Pile
import random as rdm

pile=Pile(34)
availablechoice=[]
def roll():
    return rdm.choice(["7", "8", "9", "10", "valet", "dame", "roi", "as"])
for i in range(32):
    while True:
        b=0
        r=roll()
        for a in availablechoice:
            if a==r:
                b+=1
        if b<4:
            availablechoice.append(r)
            pile.empiler(r)
            break
print(pile)
print(pile.nombreDelements())

pilej1=Pile(17)
pilej2=Pile(17)
def power(carte):
    for o in range(len(["7", "8", "9", "10", "valet", "dame", "roi", "as"])):
        if ["7", "8", "9", "10", "valet", "dame", "roi", "as"][o]==carte:
            return o
while pile.estVide!=True:
    cartej1=pile.depiler()
    pilej1.empiler(cartej1)
    cartej2=pile.depiler()
    pilej2.empiler(cartej2)
    if power(cartej1)==power(cartej2):
        print("egalité")
    
    if power(cartej1)<power(cartej2):
        print("J1 perds")
    else:
        print("J1 gagne")
