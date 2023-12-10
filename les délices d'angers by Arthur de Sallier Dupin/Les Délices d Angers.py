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
from File import File
import os
import random
import ctypes
import platform
def is_windows():
    return platform.system().lower() == 'windows'
def roll():
    foreground_colors = [0, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    background_colors = [7, 8, 9, 10, 11, 12, 13, 14]
    foreground_color = random.choice(foreground_colors)
    background_color = random.choice(background_colors)
    return foreground_color, background_color

def change_color():
    if is_windows():
        foreground_color, background_color = roll()
        if foreground_color==background_color:
            return change_color()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, foreground_color | (background_color << 4))

def ask_while_try_exept(type, ctx, ctx_err):
    while True:
        change_color()
        try:
            if type=="str":
                choice=input(ctx)
            elif type == "none":
                choice=input(ctx)
                if "none" in choice.lower():
                    return None
            else:
                raise Exception("type unknow, please choose between 'int' or 'str'")
            return choice
        except ValueError:
            print(ctx_err)
        except Exception as err:
            print(err)
            
def RécupérerFichier(name):
    WindowsFile=open(name, "r", encoding='utf-8')
    lignes=WindowsFile.readlines()
    Liste=[]
    for chaines in lignes:
        Liste.append(chaines.strip().split(";"))
    WindowsFile.close()
    return Liste

def AfficherListe(Liste):
    for i in Liste:
        print(i)

def ModifierListe(File_name, Liste, position_int, valeur_str, nouvelle_position,nouvelle_valeur_str):
    for i in range (len(Liste)):
        if Liste[i][position_int] == valeur_str:
            Liste[i][nouvelle_position]=nouvelle_valeur_str.strip() #Modifie la valeur
        else:
            Liste[i][nouvelle_position]=Liste[i][nouvelle_position].strip() #Garde inchangé
    Stringbuilder=""
    for i in range(len(Liste)):
        for j in range (len(Liste[i])):
            if j == (len(Liste[i])-1):
                Stringbuilder+=Liste[i][j]
            else:
                Stringbuilder+=Liste[i][j]+";"
        Stringbuilder+="\n"
    with open (File_name, "w",encoding='utf-8') as WindowsFile:
        WindowsFile.write("{}".format(Stringbuilder))
        WindowsFile.close()

def EcrireListe(File_name, Liste):
    Stringbuilder=""
    for i in Liste:
        for j in i:
            if j == i[-1]:
                Stringbuilder+=j
            else:
                Stringbuilder+=j+";"
        Stringbuilder+="\n"
    with open (File_name, "w",encoding='utf-8') as WindowsFile:
        WindowsFile.write("{}".format(Stringbuilder))
        WindowsFile.close()


os.system('cls')

def acceuil():
    while True:
        change_color()
        os.system('cls')
        print("*** Bienvenue sur le site \"Les délices d'Angers\" ***\nNotre site vous propose des porduits locaux et de qualité,\nBonne visite !\n")
        while True:
            change_color()
            try:
                choice=input("Avez vous un compte Oui 'o' | Non 'n'").strip()
                if choice.lower()=='n':
                    var =createaccount()
                    if var == False:
                        print("Abandon de la création du compte")
                    else:
                        change_color()
                        os.system('cls')
                        print("Compte crée avec succès,\n")
                if choice.lower()=='o':
                    break
            except:
                print("Une erreur est survenue, veuillez réessayer")
        user= login()
        if user != False:
            if "True" in user[8]:
                Personnel(user)
            else:
                FileUserCommandes=File(999)
                Catalogue(user, FileUserCommandes)
        sleep(3)

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
        temp7=""
        for caractères in temp3[0]:
             temp7+=caractères
        if ".." in temp7:
                print("Email format can't be example'..'example@example.exemple ")
                return False
        if "." in temp4:
            if ".." in temp4:
                print("Email format can't be example@example'..'exemple ")
                return False
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
    print("***Connection à votre compte***")
    id=input("\t***Saisissez votre login: ").strip()
    
    for i in range(len(Comptes)-1):
        if Comptes[i+1][6]==id:
            for j in range(0,3):
                print("Tentative {}/3".format(j))
                mdp=input("\t***Saisissez votre mot de passe: ")
                if Comptes[i+1][7]==mdp:
                    os.system('cls')
                    print("Connecté avec succès, bonjour {} {}".format(Comptes[i+1][2],Comptes[i+1][1]))
                    return Comptes[i+1]
                else:
                    print("Mauvais mot de passe :/ ")
            print("Trop de tentatives")
    print("Identifiant introuvable dans la base de données: ou mot de passe incorrect :/ ")
    return False
        
def Catalogue(user, FileUserCommandes: File):
    while True:
        print("Bienvenue dans notre catalogue,\nQuelle catégorie de produit recherchez-vous? ")
        Catégories=[]
        for i in RécupérerFichier("Produits.txt"):
            if not i[5] in Catégories:
                Catégories.append(i[5])
        for j in range(1, len(Catégories)):
            print("'{}' {}".format(j, Catégories[j]))
        catégorie=Getcatégorie(Catégories)
        change_color()
        os.system('cls')
        print("Catégorie séléctionné: {}".format(catégorie))
        MathingProduits=[]
        Produits = RécupérerFichier("Produits.txt")
        for j in range(len(Produits)):
            if Produits[j][5]==catégorie:
                MathingProduits.append(Produits[j])
        for j in range(len(MathingProduits)):
            print("'{}' ({}) {}: {}€ \n{}, {}".format(j, (MathingProduits[j][-1]).strip(), MathingProduits[j][1], MathingProduits[j][4], MathingProduits[j][3], MathingProduits[j][2]))
        #while True:
        stop=True
        while stop:
            choice=ask_while_try_exept("str", "Choisissez à l'aide de l'identifiant: ", "veuillez réessayer")
            for j in range(len(MathingProduits)):
                if str(j).strip()==choice:
                    OrderProduit(MathingProduits[j], user, FileUserCommandes)
                    stop=False
                    break
            if stop == True:
                print("Une erreur est survenue dans la saisie de l'identifiant, veuillez reessayer ")
        while True:
            try:
                choice=input("Souhaitez vous continuer à commander Oui 'o' | Non 'n'")
                if choice.lower()=='n':
                    ListesdeCommandes=[]
                    prixtotal=0
                    poidstotal=0
                    for k in range(FileUserCommandes.recupTaille()):
                        element=FileUserCommandes.enlever()
                        prixtotal+=float(element[1]*float(element[2]))
                        a=GetProduitUsingId(element[0])
                        b=getPoids(a)
                        poidstotal+=b*element[1]
                        ListesdeCommandes.append(element)
                    frais=frais_livraison(prixtotal, poidstotal)
                    stringbuilder=GetLastCommandeid()+";"+user[0]+";"+str(ListesdeCommandes)+";"+str(prixtotal)+";"+frais+";"+"en cours de validation"
                    with open ("Commandes.txt", "a",encoding='utf-8') as WindowsFile:
                            WindowsFile.write("{}\n".format(stringbuilder))
                            print("Commande de {} kg pour {}€ en cours de traitement par nos équipes".format(str(poidstotal), str(prixtotal)))
                            print("Avec seulement {}€ de frais de livraison pour un total de {}€".format(frais, float(frais)+prixtotal))
                    #GetCommandesByUser(user)
                    input("Payer")
                    print("Merci de votre visite et à demain")
                    return
                if choice.lower()=='o':
                    break
            except:
                print("Une erreur est survenue, veuillez réessayer")
    return

def GetProduitUsingId(id):
    Produits = RécupérerFichier("Produits.txt")
    for j in Produits:
        if j[0]==id:
            return j
    return "Le produit n'existe plus"
def Getcatégorie(Catégories):
    choice = ask_while_try_exept("str", "choisir une catégorie en rentrant son numéro: ", "veuillez réessayer")
    for j in range(len(Catégories)):
        if choice==str(j):
            return Catégories[j]
    return Getcatégorie(Catégories)

def OrderProduit(produit, user, FileUserCommandes: File):
    if int(produit[-1]) <= 5:
        print("Stock limité: {}".format(produit[-1]))
    while True:
        try:
            while True:
                quantité=int(input("Quel quantité ? "))
                if quantité==0:
                    print("Abandon de la commande de",produit[1])
                    return
                elif quantité <= int(produit[-1]):
                    tuple=(produit[0], quantité, produit[4])
                    FileUserCommandes.ajouter(tuple)
                    nouvelle_quantite=str(int(produit[-1])-quantité)
                    ModifierListe("Produits.txt", RécupérerFichier("Produits.txt"), 0, produit[0], -1, nouvelle_quantite)
                    """stringbuilder=GetLastCommandeid()+";"+user[0]+";"+str([produit[0], str(quantité)])+";"+str(float(produit[4])*quantité)+";"+produit[4]+";"+frais_livraison(float(produit[4])*quantité, getPoids(produit))+";"+"en cours de validation"
                    with open ("Commandes.txt", "a",encoding='utf-8') as WindowsFile:
                            WindowsFile.write("{}\n".format(stringbuilder))
                            print("Commande de {} {} en cours de traitement par nos équipes".format(str(quantité), produit[1]))
                            return"""
                    return
                
                else:
                    print("Malheuresement nous n'avons pas suffisament de stock")
                    while True:
                        try:
                            choice=input("Souhaitez vous continuer en saisissant une nouvelle quantité Oui 'o' | Non 'n'")
                            if choice.lower()=='n':
                                if createaccount() == False:
                                    print("Abandon de la commande")
                                    return
                            if choice.lower()=='o':
                                break
                        except:
                            print("Une erreur est survenue, veuillez réessayer")
        except:
            print("veuillez reessayer")
    
def getPoids(produit):
    if "g" in produit[3].lower():
        try:
            return float(produit[3].lower().replace("g", ""))/1000
        except:
            None
            #print("Erreur dans la récupération du poids en g")
    if "kg" in produit[3].lower():
        try:
            return float(produit[3].lower().replace("kg", ""))
        except:
            None
            #print("Erreur dans la récupération du poids en kg")

def GetCommandesByUser(user):
    Commandes = GetCommandes()
    UserCommandes = []
    for j in Commandes:
        if j[1]==user[0]:
            UserCommandes.append(j)
    print("Commandes en cours: {} ".format(len(UserCommandes)))
    for j in range(len(UserCommandes)):
        try:
            import ast
            ma_liste = ast.literal_eval(UserCommandes[j][2])
        except:
            print("impossible de convertir la string fournit en list")
        print("{} {} {}".format( ma_liste[1], GetProduitById(ma_liste[0]), UserCommandes[j][-1]))
    input("Presser entrer pour continuer")
    return

def GetCommandes():
    WindowsFile=open("Commandes.txt", "r", encoding='utf-8')
    lignes=WindowsFile.readlines()
    Produits=[]
    for ligne in lignes:
        Produits.append(ligne.split(";"))
    return Produits

def frais_livraison(montant, poids):     
    if montant <= 20 :
        if poids <= 5 :
            frais_livraison = 5
            return str(frais_livraison)
        if poids > 5 :
            frais_livraison = 7
            return str(frais_livraison)
    if montant <= 50 :
        if poids <= 7 :
            frais_livraison = 10
            return str(frais_livraison)
        if poids > 7 :
            frais_livraison = 12
            return str(frais_livraison)
    if montant <= 100 :
        if poids <= 10 :
            frais_livraison = 15
            return str(frais_livraison)
        if poids > 10 :
            frais_livraison = 18
            return str(frais_livraison)
    if montant > 100 :
        if poids <= 20 :
            frais_livraison = 17
            return str(frais_livraison)
        if poids > 20 :
            frais_livraison = 20
        return str(frais_livraison)
    
    

def GetProduitById(id):
    Produits = RécupérerFichier("Produits.txt")
    for j in Produits:
        if j[0]==id:
            return j[1]
    return "Le produit n'existe plus"

def Personnel(user):
    change_color()
    print("bienvenue dans votre espace personnel")
    while True:
        
        choice = ask_while_try_exept("str", "'1' pour ajouter un produit\n'2' pour modifier un produit\n'3' pour supprimer un produit\n'4' pour afficher les commandes en cours\n'5' pour afficher les stocks\n'6' pour se déconnecter\nchoix: ", "veuillez réessayer")
        os.system('cls')
        change_color()
        if choice == "1":
            id = ask_while_try_exept("str", "identifiant du produit: ", "veuillez réessayer")
            nom = ask_while_try_exept("str", "nom du produit: ", "veuillez réessayer")
            caractéristiques = ask_while_try_exept("str", "caractéristiques du produit: ", "veuillez réessayer")
            volume = ask_while_try_exept("str", "(format Xg ou Xkg) poids du produit: ", "veuillez réessayer")
            prix = ask_while_try_exept("str", "(format X ou X.X) prix du produit: ", "veuillez réessayer")
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
            try:
                UpadteProduitsWithID(id, new_id, nom, caractéristiques, volume, prix, categorie, quantite)
            except:
                None
        elif choice == "3":
            id = ask_while_try_exept("str", "identifiant du produit à modifié: ", "veuillez réessayer")
            Produits=RécupérerFichier("Produits.txt")
            try:
                produit_ligne, position = getUpdatedProduitWithId(Produits, id)
                Produits.pop(position)
                EcrireListe("Produits.txt", Produits)
            except:
                None
        elif choice == "4":
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

        elif choice == "5":
            for ligne in RécupérerFichier("Produits.txt"):
                print(ligne)
        elif choice == "6":
            print("A bientôt {}".format(user[2]))
            return
        else:
            print("Veuillez saisir un nombre")

def bad(Produits):
    WindowsFile=open("Produits.txt", "r", encoding='utf-8')
    lignes=WindowsFile.readlines()
    Produits=[]
    for ligne in lignes:
        Produits.append(ligne.split(";"))
    return Produits

def EditCommandStatus():
    Commandes = GetCommandes()
    print('')
    os.system('cls')
    for j in range(len(Commandes)):
        print("'{}' {}".format(j, Commandes[j]))
    stop = True
    while stop:
        choice = ask_while_try_exept("str", "choisir une commande en rentrant son numéro: ", "veuillez réessayer")
        for j in range(len(Commandes)):
            if choice.strip()==str(j).strip():
                stop=False
                edit(choice)
        if stop == True:
            print("Identifiant non-trouvé reessayer avec un identifiant valide")
    
def edit(choice):
    new_status=ask_while_try_exept("str", "Entrer le nouveau status: ", "veuillez réessayer")
    newCommandes = GetCommandes()
    for i in range (len(newCommandes)):
        if newCommandes[i][0] == choice:
            newCommandes[i][-1]=new_status.strip()
        else:
            newCommandes[i][-1]=newCommandes[i][-1].strip()
    for i in newCommandes:
        print(i)
    Stringbuilder=""
    for i in newCommandes:
        for j in i:
            if j == i[-1]:
                Stringbuilder+=j
            else:
                Stringbuilder+=j+";"
        Stringbuilder+="\n"
    with open ("Commandes.txt", "w",encoding='utf-8') as WindowsFile:
            WindowsFile.write("{}".format(Stringbuilder))

def UpadteProduitsWithID(Identifiant, NouvelIdentifiant,nom,caractéristiques,volume,prix,categorie,quantité ):
    newProduits=RécupérerFichier("Produits.txt")
    try:
        produit_ligne, position = getUpdatedProduitWithId(newProduits, Identifiant)
    except:
        return
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
        if newProduits[i][0]==Identifiant:
            return newProduits[i], i
    print("Identifiant non trouvé")
    return "Identifiant non trouvé"
    
def WriteListeInFile(Liste):
     StringBuilder=""
     for i in range(len(Liste)):
          StringBuilder+=Liste[i][0]+";"+Liste[i][1]+";"+Liste[i][2]+";"+Liste[i][3]+";"+Liste[i][4]+";"+Liste[i][5]+";"+Liste[i][6]+"\n"
     return StringBuilder
          



def GetLastCompteid():
    WindowsFile=open("Comptes.txt", "r")
    lignes=WindowsFile.readlines()
    Comptes=[]
    for ligne in lignes:
        Comptes.append(ligne.split(";"))
    return str(int(Comptes[-1][0])+1)
def GetLastCommandeid():
    WindowsFile=open("Commandes.txt", "r")
    lignes=WindowsFile.readlines()
    Comptes=[]
    for ligne in lignes:
        Comptes.append(ligne.split(";"))
    if Comptes[-1][0] == "Identifiant de commande":
        return "1"
    else:
        return str(int(Comptes[-1][0])+1)


acceuil()