def afficher_tableau(tableau):
    """
    Fonction pour afficher le tableau de jeu.
    """
    print("   0  1  2")
    for i in range(3):
        row = str(i) + "  "
        for j in range(3):
            if tableau[i][j] == "":
                row += "  "
            else:
                row += tableau[i][j] + " "
        print(row)

# Initialiser le tableau de jeu avec des chaînes vides pour chaque case.
tableau = [["", "", ""], ["", "", ""], ["", "", ""]]

# Boucle pour jouer jusqu'à ce qu'un joueur gagne ou que le jeu soit nul.
gagne = False
joueur = 'X'
while not gagne:
    # Afficher le tableau de jeu actuel.
    afficher_tableau(tableau)

    # Demander au joueur courant de choisir une case.
    ligne = int(input("Joueur " + joueur + ", choisissez une ligne (0-2): "))
    colonne = int(input("Joueur " + joueur + ", choisissez une colonne (0-2): "))

    # Vérifier que la case choisie est vide.
    if tableau[ligne][colonne] != "":
        print("Cette case est déjà occupée. Choisissez une autre case.")
        continue

    # Placer le symbole du joueur sur la case choisie.
    tableau[ligne][colonne] = joueur

    # Vérifier si le joueur a gagné.
    for i in range(3):
        if tableau[i][0] == joueur and tableau[i][1] == joueur and tableau[i][2] == joueur:
            gagne = True
        if tableau[0][i] == joueur and tableau[1][i] == joueur and tableau[2][i] == joueur:
            gagne = True
    if tableau[0][0] == joueur and tableau[1][1] == joueur and tableau[2][2] == joueur:
        gagne = True
    if tableau[0][2] == joueur and tableau[1][1] == joueur and tableau[2][0] == joueur:
        gagne = True

    # Passer au joueur suivant.
    if joueur == 'X':
        joueur = 'O'
    else:
        joueur = 'X'

# Afficher le tableau de jeu final.
afficher_tableau(tableau)
print("Joueur " + joueur + " a gagné !")
