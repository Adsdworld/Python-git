# chanmps d'enregistrements

#Menu personnel

# menu client 
# recevoir les diff catégories
# afficher les produits de la catégories séléctionné


#Les Délices d’Angers
# by Arthur de Sallier Dupin   

"""Présentation
La société Les Délices d’Angers a pour activité principale la vente de produits de consommation.
Elle emploie à ce jour 10 personnes en plus du directeur : une secrétaire-comptable-gestionnaire, six vendeurs et
deux commerciaux. Sa région d'implantation se situe en Anjou avec 3 boutiques.
        Mission
Travaillant pour une société de services informatiques en tant que développeur d’applications, vous intervenez chez
ce client, la société Les Délices d’Angers. Vous avez un entretien avec le directeur.
Dans le cadre de cet entretien, il vous charge de développer une application pour la vente « en ligne » de ses
produits.
    """
from time import sleep
def ask_while_try_exept(type, ctx, ctx_err):
    while True:
        try:
            if type=="str":
                choice=input(ctx)
            else:
                raise Exception("type unknow, please choose between 'int' or 'str'")
            return choice
        except ValueError:
            print(ctx_err)
        except Exception as err:
            print(err)


import os
os.system('cls')

def acceuil():
    #while True:
        os.system('cls')
        print("Bienvenue dans notre magasin")
        while True:
            try:
                choice=input("Avez vous un compte Oui 'o' | Non 'n'")
                if choice.lower()=='n':
                    if createaccount() == False:
                        print("Abandon de la création du compte")
                if choice.lower()=='o':
                    break
            except:
                print("Une erreur est survenue, veuillez réessayer")
        if login()==True:
            catalogue()

def createaccount():
    stringbuilder=GetLastCompteid()+";"
    stringbuilder+=ask_while_try_exept("str", "Votre nom: ", "veuillez réessayer")+";"
    stringbuilder+=ask_while_try_exept("str", "Votre prénom: ", "veuillez réessayer")+";"
    stringbuilder+=ask_while_try_exept("str", "Votre adresse: ", "veuillez réessayer")+";"
    temp1=ask_while_try_exept("str", "Votre date de naissance au format JJ/MM/YYYY: ", "veuillez réessayer")
    if "/" in temp1:
        ma_liste=temp1.split("/")
        if 1900<int(ma_liste[2])<2023:
            stringbuilder+=temp1+";"
        else:
         print("Veuillez entrer une date de naissance valide")
         return False
    else:
         print("Veuillez respecter le format JJ/MM/YYYY")
         return False
    temp2=ask_while_try_exept("str", "Votre email: ", "veuillez réessayer")+";"
    if temp2.count("@") == 1:
        temp3 = temp2.split("@")
        temp4=[]
        for caractères in temp3[1]:
             temp4.append(caractères)
        if "." in temp4:
            if temp4[0] == ".":
                print("Email format can't be '@.' email must contain at least on caracter between '@' and '.'")
                return False
            try:
                temp5 = temp4.split(".")
                temp6 = []
                for caractères in temp5[1]:
                    temp6.append(caractères)
                if temp6[0] == ".":
                    print("Email format can't be '@chaine..' email must contain at least on caracter between '.' and '.'")
                    return False
            except: 
                None
        else:
            print("Email must contain a '.' after '@'")
            return False
        stringbuilder+=temp2
    else:
         print("Email must contain one '@' ")
         return False
    stringbuilder+=ask_while_try_exept("str", "Définisser un identifiant pour vous connecté: ", "veuillez réessayer")+";"
    stringbuilder+=ask_while_try_exept("str", "Protéger cet identifiant par un mot de passe robuste: ", "veuillez réessayer")+";False"
    with open ("Comptes.txt", "a",encoding='utf-8') as WindowsFile:
            WindowsFile.write("\n{}".format(stringbuilder))
            return True

def login ():
    WindowsFile=open("Comptes.txt", "r")
    lignes=WindowsFile.readlines()
    Comptes=[]
    for ligne in lignes:
        Comptes.append(ligne.split(";"))
    print("***Veuillez vous connecter***")
    id=input("\t***Entrer votre adresse login: ")
    mdp=input("\t***Entrer votre mot de passe: ")
    for i in range(len(Comptes)-1):
        if Comptes[i+1][6]==id:
            if Comptes[i+1][7]==mdp:
                print("Connecté avec succès, bonjour {}".format(Comptes[i+1][1]))
                if Comptes[i+1][8]==True:
                    Personnel()
                else:
                    Catalogue()

                return True
            else:
                print("Mauvais mot de passe :/ ")
                
        else:
            print("Identifiant introuvable dans la base de données: :/ ")
    return False
        
def Catalogue():
    print("bienvenue dans notre catalogue")
    None
def Personnel():
    while True:
        choice = ask_while_try_exept("str", "'1' pour ajouter un produit\n '2' pour modifier un produit\n'3' pour afficher les commandes en cours\n4 pour se déconnecter\n'5' pour afficher les stocks")
        if choice == "1":
            None
        if choice == "2":
            None
        if choice == "3":
            None
        if choice == "4":
            None
        if choice == "5":
            getProduits()
        
        
        AddProduits("12", "pizza", "chorizo", "500g", "2", "repas", "10")
        sleep(10)
        UpadteProduitsWithID("1000", "1001", None, None, None, None, None, None)
        sleep(10)
        AddProduits("13", "pizza", "chorizo", "500g", "2", "repas", "10")
        sleep(10)
        UpadteProduitsWithID("12", "1001", None, None, None, None, None, None)
        sleep(10)
        AddProduits("20", "pizza", "chorizo", "500g", "2", "repas", "10")

def getProduits():
    WindowsFile=open("Produits.txt", "r", encoding='utf-8')
    lignes=WindowsFile.readlines()
    Produits=[]
    for ligne in lignes:
        Produits.append(ligne.split(";"))
    #print(Produits)
    return Produits

def UpadteProduitsWithID(Identifiant, NouvelIdentifiant,nom,caractéristiques,volume,prix,categorie,quantité ):
    newProduits=getProduits()
    produit_ligne, position = getUpdatedProduitWithId(newProduits, Identifiant)
    newProduits.pop(position)
    print("Ligne mise à jour: ",produit_ligne)
    updateField = []
    if NouvelIdentifiant == None:
         updateField.append(produit_ligne[0])
    else:
         updateField.append(NouvelIdentifiant)
    if nom == None:
         updateField.append(produit_ligne[1])
    else:
         updateField.append(nom)
    if caractéristiques == None:
         updateField.append(produit_ligne[2])
    else:
         updateField.append(caractéristiques)
    if volume == None:
         updateField.append(produit_ligne[3])
    else:
         updateField.append(volume)
    if prix == None:
         updateField.append(produit_ligne[4])
    else:
         updateField.append(prix)
    if categorie == None:
         updateField.append(produit_ligne[5])
    else:
         updateField.append(categorie)
    if quantité == None:
         updateField.append(produit_ligne[6])
    else:
         updateField.append(quantité)
    
    newProduits.append(updateField)
    with open ("Produits.txt", "w",encoding='utf-8') as WindowsFile:
            WindowsFile.write("{}".format(WriteListeInFile(newProduits)))

def AddProduits(Identifiant,nom,caractéristiques,volume,prix,categorie,quantité ):
    stringbuilder=Identifiant+";"+nom+";"+caractéristiques+";"+volume+";"+prix+";"+categorie+";"+quantité
    with open ("Produits.txt", "a",encoding='utf-8') as WindowsFile:
            WindowsFile.write("{}\n".format(stringbuilder))


def getUpdatedProduitWithId(newProduits, Identifiant):
    for i in range(len(newProduits)):
        #print(newProduits[i][0])
        if newProduits[i][0]==Identifiant:
            #print(newProduits[i])
            return newProduits[i], i
    return None
    
def WriteListeInFile(Liste):
     StringBuilder=""
     for i in range(len(Liste)):
          StringBuilder+=Liste[i][0]+";"+Liste[i][1]+";"+Liste[i][2]+";"+Liste[i][3]+";"+Liste[i][4]+";"+Liste[i][5]+";"+Liste[i][6]
     return StringBuilder
          



def GetLastCompteid():
    WindowsFile=open("Comptes.txt", "r")
    lignes=WindowsFile.readlines()
    Comptes=[]
    for ligne in lignes:
        Comptes.append(ligne.split(";"))
    #print(Comptes[-1])
    return str(int(Comptes[-1][0])+1)


acceuil()