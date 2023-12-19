#Arthur de Sallier Dupin P2 E2
from time import sleep
import os
import random
os.system('cls')

def RécupérerFichier(name):
    WindowsFile=open(name, "r", encoding='utf-8')
    lignes=WindowsFile.readlines()
    Liste=[]
    for chaines in lignes:
        Liste.append(chaines.strip().split(";"))
    WindowsFile.close()
    return Liste

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



def ask_str(ctx):
    while True:
        try:
            choice=input(ctx)
            return choice
        except ValueError:
            print("Veuillez rentrer une chaine de caractère")

def ask_int(ctx):
    while True:
        try:
            choice=int(input(ctx))
            return choice
        except ValueError:
            print("Veuillez rentrer un nombre (int)")

def ask_float(ctx):
    while True:
        try:
            choice=float(input(ctx))
            return choice
        except ValueError:
            print(print("Veuillez rentrer un nombre (float)"))





str = ask_str("entrer une str")
print(str,type(str))
int = ask_int("entrer un int")
print(int,type(int))
float = ask_float("entrer un float")
print(float,type(float))