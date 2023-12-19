#Arthur de Sallier Dupin P2 E2

def ask_int(ctx, ctx_error):
    while True:
        try:
            choice=int(input(ctx))
            return choice
        except ValueError:
            print(ctx_error)

def controlerCarburant(capacite, jauge_en_pourcentage, conssomation):
    print("Distance à parcourir avant la prochaine station : 350km")
    nombre_de_litres = capacite*(jauge_en_pourcentage/100)
    nombre_de_kilomètres_restants = (nombre_de_litres/conssomation)*100
    print("Distance possible dans l'état actuel: ",nombre_de_kilomètres_restants, "kms")

    if nombre_de_kilomètres_restants >= 350:
        print("Bonne route !!!\n")
    else:
        print("Faites de plein !\n")
        return Ajout_de_Carburant(capacite, jauge_en_pourcentage, conssomation)
    return nombre_de_kilomètres_restants


def Ajout_de_Carburant(capacite, jauge_en_pourcentage, conssomation):
    print(" *** Ajout de Carburant *** ")
    while True:
        jauge_en_pourcentage2 = ask_int("Saisir le pourcentage de carburant à ajouter (par exemple 15%): ", "Veuillez saisir un nombre entier au format 'X'%")
        if 0 < jauge_en_pourcentage2 > 100:
            print("Vous avez saisie une valeur supérieur à 100%, ce qui n'est pas concevable, veuillez réessayer")
        else:
            break
    jauge_en_pourcentage +=jauge_en_pourcentage2
    return controlerCarburant(capacite, jauge_en_pourcentage, conssomation)


def controlerPression():
    print("Lancement du programme de controle de la pression des pneus")
    while True:
        while True:
            pneu_avant_droit = ask_int("Saisir la pression du pneu avant droit (par exemple 40 psi): ", "Veuillez saisir un nombre entier au format 'X'psi")
            if 34<pneu_avant_droit<46:
                break 
            else:
                print("Les pressions doivent être dans l'interval 35 à 45 psi conmpris, veuillez réessayer")
        while True:
            pneu_avant_gauche = ask_int("Saisir la pression du pneu avant gauche (par exemple 40 psi): ", "Veuillez saisir un nombre entier au format 'X'psi")
            if 34<pneu_avant_gauche<46:
                break 
            else:
                print("Les pressions doivent être dans l'interval 35 à 45 psi conmpris, veuillez réessayer")
        if -1<abs(pneu_avant_droit-pneu_avant_gauche)<4:
            break
        else:
            print("La différence entre les pneus avant doit être maximum de 3psi, différence calculé: ",abs(pneu_avant_droit-pneu_avant_gauche))
    while True:
        while True:
            pneu_arrière_droit = ask_int("Saisir la pression du pneu arrière droit (par exemple 40 psi): ", "Veuillez saisir un nombre entier au format 'X'psi")
            if 34<pneu_avant_droit<46:
                break 
            else:
                print("Les pressions doivent être dans l'interval 35 à 45 psi conmpris, veuillez réessayer")
        while True:
            pneu_arrière_gauche = ask_int("Saisir la pression du pneu arrière gauche (par exemple 40 psi): ", "Veuillez saisir un nombre entier au format 'X'psi")
            if 34<pneu_avant_gauche<46:
                break 
            else:
                print("Les pressions doivent être dans l'interval 35 à 45 psi conmpris, veuillez réessayer")
        if -1<abs(pneu_avant_droit-pneu_avant_gauche)<5:
            break
        else:
            print("La différence entre les pneus avant doit être maximum de 4psi, différence calculé: ",abs(pneu_avant_droit-pneu_avant_gauche))
    print("Les pressions sont correctes\n")
    return
    

def magasin():
    dico_categories={1:"boissons", 2:"chips", 3:"sucreries"}
    dico_boissons = {1:"coca", 2:"pepsi", 3:"limonade"}
    dico_chips = {1:"chips salées", 2:"chips sucrées", 3:"chips classic"}
    dico_sucreries = {1:"bonbon de noel", 2:"bonbon bleu", 3:"bonbon rouge"}
    for j in range(len(dico_categories)):
        print("'{}' {}".format(j, dico_categories[j+1]))
    while True:
        choix_int = ask_int("Choisissez une catégorie", "veuillez réessayer en entrant un nombre")+1
        if choix_int in dico_categories:
            break
    if choix_int == 1:
        for j in range(len(dico_boissons)):
            print("'{}' {}".format(j, dico_boissons[j+1]))
        while True:
            choix2_int = ask_int("Choisissez une boisson", "veuillez réessayer en entrant un nombre")+1
            if choix2_int in dico_boissons:
                print("achat de", dico_boissons[choix2_int])
                break
    if choix_int == 2:
        for j in range(len(dico_chips)):
            print("'{}' {}".format(j, dico_chips[j+1]))
        while True:
            choix2_int = ask_int("Choisissez une chips", "veuillez réessayer en entrant un nombre")+1
            if choix2_int in dico_chips:
                print("achat de", dico_chips[choix2_int])
                break
    if choix_int == 3:
        for j in range(len(dico_sucreries)):
            print("'{}' {}".format(j, dico_sucreries[j+1]))
        while True:
            choix2_int = ask_int("Choisissez une sucreries", "veuillez réessayer en entrant un nombre")+1
            if choix2_int in dico_sucreries:
                print("achat de", dico_sucreries[choix2_int])
                break
    

