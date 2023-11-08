# de Sallier Dupin Arthur
# Programme Principal qui va appeler les fonctions du module ModuleFonctions
# et le programme du module MiniProgramme
import os
import ModuleFonctionsDS1 as MF
# clear the console screen
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Appel du programme de consommation automobile


# Appel de la fonction1
MF.fonction1()

# Appel de la fonction2
Liste=MF.fonction2()
# Appel de la fonction3

print("mot choisit 1: {}".format(MF.fonction3(Liste)))
print("mot choisit 2: {}".format(MF.fonction3(Liste)))
print("mot choisit 3: {}".format(MF.fonction3(Liste)))
print("mot choisit 4: {}".format(MF.fonction3(Liste)))
print("mot choisit 5: {}".format(MF.fonction3(Liste)))

# Appel de la fonction4 et affichage du résultat
print("Résultat de la recherche: {}".format(MF.fonction4(Liste)))

##on peut saisier des carcatères vides dans fonction 2




