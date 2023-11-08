import os
os.system('cls')

WindowsFile=open("nation.txt", "r")
lignes=WindowsFile.readlines()


Liste=[]
for caractères in lignes:
    Liste.append(caractères.split(";"))

def a():
    for ligne in range(len(Liste)):
        for element in Liste[ligne]:
            if Liste[ligne][0]=="1":
                Liste[ligne][0]="Afrique"
            if Liste[ligne][0]=="2":
                Liste[ligne][0]="Amérique"
            if Liste[ligne][0]=="3":
                Liste[ligne][0]="Asie"
            if Liste[ligne][0]=="4":
                Liste[ligne][0]="Oceanie"
            if Liste[ligne][0]=="5":
                Liste[ligne][0]="Europe"
        print("Continent: {}\n Pays: {}\nCapital: {}\nSuperficie: {}\nPopulation: {}".format(Liste[ligne][0], Liste[ligne][1], Liste[ligne][2], Liste[ligne][3], Liste[ligne][4]))

a()
dico={}
for ligne in range(len(Liste)):
    if Liste[ligne][0] in dico:
        print("Element trouvé dans dico: {}".format(Liste[ligne][0]))
        dico[Liste[ligne][0]]+=int(Liste[ligne][4])
    else:
        dico[Liste[ligne][0]]=int(Liste[ligne][4])

print(dico)

WindowsFile.close()
with open ("nation.txt", "r",encoding='utf-8') as WindowsFile, open("nationV1.txt", "w",encoding='utf-8') as WindowsFile2 :
    for lignes in WindowsFile :
        WindowsFile2.write(""+lignes) 


WindowsFile.close()
WindowsFile2.close()
#update with 2021
with open ("nation.txt", "r",encoding='utf-8') as WindowsFile, open ("majpop2021.txt", "r",encoding='utf-8') as WindowsFile2:
    lignes2=WindowsFile2.readlines()
    Liste2=[]
    for caractères in lignes2:
        Liste2.append(caractères.split(";"))
    lignes=WindowsFile.readlines()
    Liste=[]
    for caractères in lignes:
        Liste.append(caractères.split(";"))

WindowsFile.close()
WindowsFile2.close()
    #print(Liste2)
    #print(Liste)
for elements in Liste2:
    for e in range(len(Liste)):
        if elements[0].upper()==Liste[e][1]:
            print("maj")
            Liste[e][4]=elements[1]

for ligne in range(len(Liste)):
    print("Continent: {}\n Pays: {}\nCapital: {}\nSuperficie: {}\nPopulation: {}".format(Liste[ligne][0], Liste[ligne][1], Liste[ligne][2], Liste[ligne][3], Liste[ligne][4]))

import sys
sys.path
import Ask_module as ask


if 'n'==ask.ask_while_try_exept_oui_non("ajouter des données 'o' 'n' ", "o", "n", "ajoutons des données", "pas d'ajout", "saisir 'o' ou 'n'"):
    print("pas d'ajout")
else:
    while True:
        continent=ask.ask_while_try_exept("str", "saisir un continent", "str requeired").upper()
        pays=ask.ask_while_try_exept("str", "saisir un pays", "str requeired").upper()
        capital=ask.ask_while_try_exept("str", "saisir une capital", "str requeired").upper()
        superficie=ask.ask_while_try_exept("int", "saisir une superficie", "int requeired")
        population=ask.ask_while_try_exept("int", "saisir une population", "int requeired")
        stop=False
        for e in Liste:
            if e[1]==pays.upper():
                stop=True
        if stop==True:
            continue
        with open ("nation.txt", "a",encoding='utf-8') as WindowsFile:
            WindowsFile.write("\n{};{};{};{};{}".format(continent, pays, capital, superficie, population))
        with open ("nation.txt", "r",encoding='utf-8') as WindowsFile:
            lignes=WindowsFile.readlines()
            Liste=[]
            for caractères in lignes:
                Liste.append(caractères.split(";"))
        if 'n'==ask.ask_while_try_exept_oui_non("ajouter des données 'o' 'n' ", "o", "n", "ajoutons des données", "pas d'ajout", "saisir 'o' ou 'n'"):
            break
    



