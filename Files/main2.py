WindowsFile=open("FicLaser.txt", "r")
lignes=WindowsFile.readlines()

dico={}
for i in lignes:
    mots=i.split(",")
    print(mots[-1])
    if not mots[0] in dico:
        dico[mots[0]]=int(mots[-1])
    else:
        dico[mots[0]]+=int(mots[-1])

for keys in dico:
    print(keys+": "+dico[keys])