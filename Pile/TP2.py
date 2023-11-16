import os
os.system('cls')
maliste=[]
def menu():
    while True:
        choice=input("choose X + D C 'q' to quit()")
        if choice.lower()=="x":
            f_x()
        elif choice.lower()=="+":
            f_()
        elif choice.lower()=="d":
            f_d()
        elif choice.lower()=="c":
            f_c()
        elif choice.lower()=="q":
            print("final score: {}".format(maliste[-1]))
        print(maliste)

def f_x():
    play=True
    while play:
        try:
            entier=int(input("nouveau score"))
            #if entier.isdigit():
            maliste.append(entier)
            return
        except :
            print("Une erreur est survenue")

def f_():
    try:
        if (len(maliste)>=2):
            maliste.append(maliste[-1]+maliste[-2])
        else:
            raise Exception("Pas assez de scores 2 requis")
    except Exception:
        print(Exception)

def f_d():
    try:
        if (len(maliste)>=1):
            maliste.append(maliste[-1]*2)
        else:
            raise Exception("Pas assez de scores 1 requis")
    except Exception:
        print(Exception)
def f_c():
        if (len(maliste)>=1):
            maliste.pop()
        else:
            print("Pas assez de scores 1 requis")

menu()