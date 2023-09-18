def tourner_morpion(morpion, coefficient, ligne, colonne):
    """
    Retourne le morpion dans le sens horaire en fonction d'un coefficient de retournement.
    Le coefficient doit être un entier compris entre 1 et 4 inclus.
    La fonction retourne également les coordonnées de la ligne et de la colonne tournées.
    """
    if coefficient == 0 or coefficient == 4:
        return morpion, ligne, colonne
    elif coefficient == 1:
        nouveau_morpion = [[morpion[2-i][j] for i in range(3)] for j in range(3)]
        nouvelle_ligne = colonne
        nouvelle_colonne = 2 - ligne
    elif coefficient == 2:
        nouveau_morpion = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
        nouveau_morpion[0][0] = morpion[2][2]
        nouveau_morpion[0][1] = morpion[2][1]
        nouveau_morpion[0][2] = morpion[2][0]
        nouveau_morpion[1][0] = morpion[1][2]
        nouveau_morpion[1][1] = morpion[1][1]
        nouveau_morpion[1][2] = morpion[1][0]
        nouveau_morpion[2][0] = morpion[0][2]
        nouveau_morpion[2][1] = morpion[0][1]
        nouveau_morpion[2][2] = morpion[0][0]
        nouvelle_ligne = 2 - ligne
        nouvelle_colonne = 2 - colonne
    elif coefficient == 3:
        nouveau_morpion = [[morpion[i][2-j] for i in range(3)] for j in range(3)]
        nouvelle_ligne = 2 - colonne
        nouvelle_colonne = ligne
    else:
        raise ValueError("Le coefficient de retournement doit être un entier entre 1 et 4 inclus.")
    return nouveau_morpion, nouvelle_ligne, nouvelle_colonne

def afficher_morpion(morpion):
    """
    Affiche un morpion sous forme de grille avec des caractères spéciaux.
    Le morpion doit être une matrice contenant 3 listes.
    """
    print("   0   1   2")
    print("0  " + morpion[0][0] + " | " + morpion[0][1] + " | " + morpion[0][2])
    print("  ---+---+---")
    print("1  " + morpion[1][0] + " | " + morpion[1][1] + " | " + morpion[1][2])
    print("  ---+---+---")
    print("2  " + morpion[2][0] + " | " + morpion[2][1] + " | " + morpion[2][2])



morpion = [
    [" ", "X", "O"],
    [" ", " ", " "],
    [" ", " ", " "]]

morpion,x, y = tourner_morpion(morpion, 0, 1, 1)
afficher_morpion(morpion)
morpion = [
    [" ", "X", "O"],
    [" ", " ", " "],
    [" ", " ", " "]]
morpion,x, y = tourner_morpion(morpion, 1, 1, 1)
afficher_morpion(morpion)
morpion = [
    [" ", "X", "O"],
    [" ", " ", " "],
    [" ", " ", " "]]
morpion,x, y = tourner_morpion(morpion, 2, 1, 1)
afficher_morpion(morpion)
morpion = [
    [" ", "X", "O"],
    [" ", " ", " "],
    [" ", " ", " "]]
morpion,x, y = tourner_morpion(morpion, 3, 1, 1)
afficher_morpion(morpion)