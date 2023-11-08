import os
os.system('cls')

WindowsFile=open("err.data.txt", "r")
lignes=WindowsFile.readline()

lecture_code=False
error_code=""
error_Liste=[]
for caracteres in lignes:    
    if lecture_code==True:
        if caracteres=="*":
            error_Liste.append(error_code)
            error_code=""
            lecture_code=False
        else:
            error_code+=caracteres
    elif caracteres=="*":
        lecture_code=True

for element in error_Liste:
    if element=="":
        error_Liste.remove(element)
        
while True:
    try:
        choice=input("Entrer un code d'erreur")
        break
    except:
        print("Une erreur est survenue")
compteur=0
for a in error_Liste:
    if choice==a:
        compteur+=1
print(compteur)
