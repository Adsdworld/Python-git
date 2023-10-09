from Ask_module import *


while True:
    choice=ask_while_try_exept_oui_non("Êtes vous un Homme ou une Femme? ","Homme", "Femme", "Homme séléctionné", "Femme séléctionné", "Choisisser entre Femme et Homme")
    choice2=ask_while_try_exept_oui_non("Calculer son Poids idéal ou votre IMC? ", "Poids idéal", "IMC", "Poids Idéal séléctionné", "IMC séléctionné", "You must make a choice")
    tailleEnCm=int(ask_while_try_exept("float", "Quel est votre taille en m", "vous devez entrer une taille en m"))
    PoidsEnkg=int(ask_while_try_exept("int", "Quel est votre poids en kg", "vous devez entrer un poids en kg"))

    dico={"dénutrition":16.5, "maigreur":18.4, "poids normal":24.9, "surpoids":25, "obésité modéré":30, "obésité sévère":35, "obésité morbide":40}
    if choice2=="IMC":
        res=PoidsEnkg/(tailleEnCm*tailleEnCm)
        print("IMC calculé: {}".format(res))
        for keys in dico:
            if dico[keys]>res:
                print("Hmm, diagnostic du robotdoctor: {}".format(keys))
                break

    else:
        if choice=="Homme":
            res=tailleEnCm*62.4-44.7
        else:
            res=tailleEnCm*72.7-62.4
        if res<PoidsEnkg:
            print("Vous êtes sous le poids idéal")
        elif res==PoidsEnkg:
            print("Parfaite santé, votre poids est idéal")
        else:
            print("Vous êtes au-dessus de votre poids idéal")
    #choiceQuit=ask_while_try_exept_oui_non("Quitter? 'o' ou 'n' ", 'o', 'n', "fermeture du programme", "On recommence !", "You must choice between oui 'o' or no 'n'")
    #if choiceQuit=='o':
    #    break
    if ask_while_try_exept_quitter()==True:
        break

