WindowsFile=open("FicLaser.txt", "r")
lignes=WindowsFile.readlines()

dico={}
total=0
from datetime import datetime
print(datetime.now())
for i in lignes:
    mots=i.split(",")
    if not mots[0] in dico:
        try:
            dico[mots[0]]=int(mots[-1])
            total+=int(mots[-1])
        except:
            dico[mots[0]]=mots[-1]
        
    else:
        try:
            dico[mots[0]]+=int(mots[-1])
            total+=int(mots[-1])
        except:
            dico[mots[0]]+=mots[-1]

for keys in dico:
    print(keys+": "+str(dico[keys]))
print("TOTAL {}".format(total))
    
