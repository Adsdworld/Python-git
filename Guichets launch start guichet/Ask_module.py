def ask_while_try_exept(type, ctx, ctx_err):
    while True:
        try:
            if type=="int":
                choice=int(input(ctx))
            elif type=="str":
                choice=input(ctx)
            elif type=="float":
                choice=float(input(ctx))
            else:
                raise Exception("type unknow, please choose between 'int' or 'str'")
            return choice
        except ValueError:
            print(ctx_err)
        except Exception as err:
            print(err)
    

    


def ask_while_try_exept_oui_non(ctx, choice1, choice2, choice1msg, choice2msg, choice_err):
    while True:
        try:
            choice=input(ctx)
            if choice==choice1:
                print(choice1msg)
                return choice
            elif(choice==choice2):
                print(choice2msg)
                return choice
            else:
                raise Exception(choice_err)
        except Exception as err:
            print(err)

def ask_while_try_exept_quitter():
    while True:
        try:
            choice=input("Souhaiter vous quitter le programme 'o' ou 'n': ")
            if choice=='o':
                print("Fermeture du programme")
                return True
            elif(choice=='n'):
                return False
            else:
                raise Exception("Vous devez choisir entre 'o' ou 'n'")
        except Exception as err:
            print(err)


def ask_while_try_exept_revenir_en_arrière():
    while True:
        try:
            choice=input("Souhaiter vous revenir en arrière? 'o' ou 'n': ")
            if choice=='o':
                print("Retour en arrière")
                return True
            elif(choice=='n'):
                return False
            else:
                raise Exception("Vous devez choisir entre 'o' ou 'n'")
        except Exception as err:
            print(err)

print("".join(reversed("Boujour")))
