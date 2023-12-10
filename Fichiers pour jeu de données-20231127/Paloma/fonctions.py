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
    for i in Liste:
        for j in i:
            if j == i[-1]:
                Stringbuilder+=j
            else:
                Stringbuilder+=j+";"
        Stringbuilder+="\n"
    with open (File_name, "w",encoding='utf-8') as WindowsFile:
        WindowsFile.write("{}".format(Stringbuilder))

def ask_while_try_exept(question, message_erreur):
    while True:
        try:
            choice=input(question)
            return choice
        except :
            print(message_erreur)

            