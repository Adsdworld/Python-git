import MiniProgramme as MP



def function(a):
    try:
        if a==0:
            raise Exception("a==0")
    except:
        print("Une erreur est survenue dans le try")
    else:
        print("Aucune erreur n'est survenue dans l'éxécution")
    finally:
        print("Fin de l'éxécution du programme")