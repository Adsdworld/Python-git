from Ask_module import *
import ServicesCartes as svc
from datetime import datetime

def AfficherMenuPrincipal():
    print("***Menu***\n1-Consulter le solde\n2-Faire un retrait\n3-Faire un dépôt\n")
    choice=ask_while_try_exept("int", "Veuillez choisir entre 1, 2 ou 3 et 0 pour quitter", "Veulliez rentrer un nombre")
    while choice!=0 and choice!=1 and choice!=2 and choice!=3:
        choice=ask_while_try_exept("int", "***Veuillez choisir entre 1, 2 ou 3 et 0 pour quitter: ", "Veulliez rentrer un nombre entre 0 et 3")
    if choice==0:
        print("Le system Swift vous rends votre carte jalousement")
        quit()
    elif choice==1:
        AfficherSolde()
    elif choice==2:
        AfficherRetrait()
    elif choice==3:
        AfficherDépôt()



def AfficherSolde():
    print("***Solde***")
    print("Solde: {}".format(svc.RécupérerSolde()))
    svc.TicketMsg="Consultation de votre solde le {}\nSolde: {}".format(datetime, svc.DatabaseSolde)
    DemanderTicket()
    AfficherMenuPrincipal()
def AfficherRetrait():
    print("***Retrait***")
    while True:
        try:
            choice=int(input("Entrer le montant à retirer: 10, 20, 30, 40, 50, 100, 500, 10000, vous entrer un montant personnalisé"))
            if svc.DatabaseSolde>=choice:
                print("Le retrait à été authorisé")
                svc.DatabaseSolde=svc.DatabaseSolde-choice
                svc.TicketMsg="Retrait le {}\nMontant: {}\nNouveau Solde: {}".format(datetime, choice, svc.DatabaseSolde)
                DemanderTicket()
            else:
                print("Le system swift vous regarde avec dédain")
                raise Exception("err")
        except Exception:
            print("Montant trop important")
            if ask_while_try_exept_revenir_en_arrière()==True:
                break
        else:
            print("L'opération à réussit")
            break
    AfficherMenuPrincipal()
def AfficherDépôt():
    print("***Dépôt***")
    while True:
        try:
            choice=int(input("Entrer le montant à déposer: 10, 20, 30, 40, 50, 100, 500, 1000, vous entrer un montant personnalisé *Limité à 1000 par opération"))
            if choice<=1000:
                print("Le dépôt à été authorisé")
                svc.DatabaseSolde=svc.DatabaseSolde+choice
                svc.TicketMsg="Dépôt le {}\nMontant: {}\nNouveau Solde: {}".format(datetime, choice, svc.DatabaseSolde)
                DemanderTicket()
            else:
                print("Le system swift vous regarde avec envie")
                raise Exception("err")
        except Exception:
            print("Trop d'argent à été déposer, le distributeur n'accepte dorénavant plus que les diamants")
            if ask_while_try_exept_revenir_en_arrière()==True:
                break
        else:
            print("L'opération à réussit")
            break
    AfficherMenuPrincipal()

def DemanderTicket():
    choice=ask_while_try_exept_oui_non("Voulez vous un ticket 'o' ou 'n': ", "n", "o", "merci pour la planète", "impression du ticket", "Veuillez répondre par 'o' ou 'n'")
    if choice=='o':
        AfficherTicket()
    AfficherMenuPrincipal()

def AfficherTicket():
    print("***Ticket***")
    print(svc.TicketMsg)
    svc.TicketMsg=""
    print("Ticket edited by beautiful Swift system")