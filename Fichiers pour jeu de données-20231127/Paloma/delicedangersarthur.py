
import os
os.system('cls')
import fonctions as f

print("""***bienvenue sur le site Les Délices d'angers***
        notre sie vous propose des produits locaux de qualité 
        bonne visite""" )

while True:
    try:
        compte=int(input("avez vous un compte ? 1 pour oui et 2 pour non: "))
        break
    except ValueError:
        print("Mettre un nombre")
    

def SeConnecter ():
    Comptes=f.RécupérerFichier("Comptes.txt")
    login = input("saisir login: ")
    motdepasse = input("saisir mot de passe: ")
    for ligne in Comptes:
        if ligne[6]==login:
            #print("login correct")
            if ligne[7] == motdepasse:
                #rint("mot de passe ok")
                nom = ligne[1]
                prenom = ligne[2]
                print("bonjour", prenom, "", nom)
                return 
            else:
                return"mot de passe incorrect"

            """nom = ligne[1]
            prenom = ligne[2]
            adresse = ligne[5]
            naissance = ligne[4]
            mail = ligne[3]
            motdepasse=ligne[7]
            """

    return "Login incorrect"

if compte ==1 :
    print(SeConnecter())

if compte == 2:
    print("création d'un compte ")
    nom = input("saisir votre nom")
    prenom = input("saisir votre prénom")
    adresse = input("saisir votre adresse")
    naissance = input("saisir votre date de naissance")
    email = input("saisir votre adresse mail")
    login = input("saisir votre login")
    try:
        motdepasse = input("saisir votre mot de passe")
    except ValueError:
        print("mettre un mot de passe avec des chiffre")

    print("bonjour",prenom,"",nom)
    def GetLastCompteid():
        WindowsFile=open("Comptes.txt", "r")
        lignes=WindowsFile.readlines()
        Comptes=[]
        for ligne in lignes:
            Comptes.append(ligne.split(";"))
        return str(int(Comptes[-1][0])+1)

    with open("Comptes.txt", 'a', encoding='utf8', ) as fichier:
        fichier.write(str(GetLastCompteid()+";"+nom+";"+prenom+";"+adresse+";"+naissance+";"+email+";"+login+";"+motdepasse+";False\n"))
        fichier.close()


def recupererCategorie():

    listeProduits=[]
    dicoCategorie={}

    with open ("Produits.txt", "r", encoding='utf8') as listeProd :
        listeProd.readline()
        i= 1
        for produit in listeProd :
            tab = produit.split(";")

            if len(tab)>6:
                try :
                    tab[6]=int(tab[6])
                except ValueError:
                    print(f"Erreur de conversion en entier")
                    break

            else:
                print("l'indice n'est pas dans la ligne")
                break
            #tab[6] = int(tab[6])
            listeProduits.append(tab)

            if tab[5] not in dicoCategorie.values() :
                dicoCategorie[i] = tab[5]
                i+=1

    return listeProduits, dicoCategorie
#print(recupererCategories())

listeProduits, dicoCategorie = recupererCategorie()
print(dicoCategorie)

while True:
    try:
        categorie=int(input("quelle catégorie de produits recherchez-vous ?"))
    except ValueError:
        print("Mettre un chiffre")
    else:
        print("Votre choix est de",dicoCategorie[categorie])
        break

listeProdCat=[]
for prod in listeProduits :
    if prod[5]==dicoCategorie[categorie]:
        listeProdCat.append(prod)
for prod in range(len(listeProdCat)):
    print(prod,"Nom :", listeProdCat[prod][1], "Produit :", listeProdCat[prod][2], "Volume :", listeProdCat[prod][3], "Prix :", listeProdCat[prod][4] )
def autrecodepourlechoix():
    reponse = f.ask_while_try_exept("choisir en saisissant le nombre devant le produit: ", "veuillez reessayer")
    for prod in range(len(listeProdCat)):
        if reponse.strip() == str(prod): #strip retire les espaces
            return listeProdCat[prod]
    print("produit non trouvé, retour à la saisie des catégories")
    return recupererCategorie()
prod = autrecodepourlechoix()
while True:
    try:
        quantité = int(input("quelle quantité souhaitez-vous ?"))
        nouvelle_quantite=str(int(prod[-2])-quantité)
        break
    except:
        print("Mettre un nombre, attention à ce que la quantité dans le fichier produit soit un nombre")
f.ModifierListe("Produits.txt", f.RécupérerFichier("Produits.txt"), 0, prod[0], -2, nouvelle_quantite)







#aides pour la suite, tu as certainement d'autres fonctionnalités à implémente avant de t'y intérresser
"""
def Personnel(user):
    print("bienvenue dans votre espace personnel")
    while True:
        choice = ask_while_try_exept("str", "'1' pour ajouter un produit\n'2' pour modifier un produit\n'3' pour afficher les commandes en cours\n'4' pour afficher les stocks\n'5' pour se déconnecter\nchoix: ", "veuillez réessayer")
        if choice == "1":
            id = ask_while_try_exept("str", "identifiant du produit: ", "veuillez réessayer")
            nom = ask_while_try_exept("str", "nom du produit: ", "veuillez réessayer")
            caractéristiques = ask_while_try_exept("str", "caractéristiques du produit: ", "veuillez réessayer")
            volume = ask_while_try_exept("str", "poids du produit: ", "veuillez réessayer")
            prix = ask_while_try_exept("str", "prix du produit: ", "veuillez réessayer")
            categorie = ask_while_try_exept("str", "categorie du produit: ", "veuillez réessayer")
            quantite = ask_while_try_exept("str", "quantité du produit: ", "veuillez réessayer")
            AddProduits(id, nom, caractéristiques, volume, prix, categorie, quantite)
        elif choice == "2":
            id = ask_while_try_exept("str", "identifiant du produit à modifié: ", "veuillez réessayer")
            new_id = ask_while_try_exept("none", "(Enter 'None' to keep current value) Nouvel identifiant du produit: ", "veuillez réessayer")
            nom = ask_while_try_exept("none", "(Enter 'None' to keep current value) nom du produit: ", "veuillez réessayer")
            caractéristiques = ask_while_try_exept("none", "(Enter 'None' to keep current value) caractéristiques du produit: ", "veuillez réessayer")
            volume = ask_while_try_exept("none", "(Enter 'None' to keep current value) poids du produit: ", "veuillez réessayer")
            prix = ask_while_try_exept("none", "(Enter 'None' to keep current value) prix du produit: ", "veuillez réessayer")
            categorie = ask_while_try_exept("none", "(Enter 'None' to keep current value) categorie du produit: ", "veuillez réessayer")
            quantite = ask_while_try_exept("none", "(Enter 'None' to keep current value) quantité du produit: ", "veuillez réessayer")
            UpadteProduitsWithID(id, new_id, nom, caractéristiques, volume, prix, categorie, quantite)
        elif choice == "3":
            Commandes=GetCommandes()
            for j in range (len(Commandes)):
                print(Commandes[j])
            while True:
                try:
                    choice=input("Souhaitez vous modifier le status d'une commande? Oui 'o' | Non 'n'")
                    if choice.lower()=='n':
                        break
                    if choice.lower()=='o':
                        EditCommandStatus()
                except:
                    print("Une erreur est survenue, veuillez réessayer")

        elif choice == "4":
            for ligne in getProduits():
                print(ligne)
        elif choice == "5":
            print("Aurevoir {}".format(user[2]))
            return

"""