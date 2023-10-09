from Ask_module import *
from time import sleep
from Menu import *
from ServicesCartes import *


SwiftErrorMsg="Le system Swift vous regarde avec dédain"


def AuthSucess():
    AfficherMenuPrincipal()
def guichet():
    while True:
        UserCard=ask_while_try_exept("int", "***INSERER CARTE\nEntrer votre identifiant de carte: ", "Veuillez entrer l'identifiant de votre carte")
        print("Asking Swift system")
        for i in range(3):
            sleep(0.3)
            print(".")
        if UserCard==DatabaseCard:
            for i in range(3):
                try:
                    UserCode=ask_while_try_exept("int", "***TAPER CODE\nEntrer votre code de carte: ", "Veuillez entrer le code de votre carte")
                    if UserCode==DatabaseCode:
                        print("Vous avez correctement été authentifié par le system Swift")
                        AfficherMenuPrincipal()
                    else:
                        print("tentatives: {}/3".format(i+1))
                        raise Exception("Code Faux")
                except Exception as err:
                    print(err)
                    i+=1
                    if i==3:
                        print("Je mange votre carte parceque j'ai faim")
                        continue
                
        else:
            print(SwiftErrorMsg)
            continue
        
