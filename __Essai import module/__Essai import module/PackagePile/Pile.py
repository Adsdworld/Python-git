class Pile:
    def __init__(self, capacite) :
        self.valeurs = []
        self.capacite = capacite

    # Retourne le nombre d'éléments de la pile
    def nombreDelements(self) :
        return len(self.valeurs)

    # Renvoie True si la pile et vide et False sinon
    def estVide(self) :
        return self.valeurs == []

    def estPleine(self) :
        if (self.nombreDelements() == self.capacite) :
            return True
        else :
            return False

    # Ajoute un élément à la pile
    def empiler(self, valeur) :
        if self.estPleine() == False :
            self.valeurs.append(valeur)
        else :
            print("Ajout impossible. Pile pleine")

    # Supprime le dernier élément ajouté
    def depiler(self) :
        if self.estVide() == False :
            if self.valeurs :
                return self.valeurs.pop()
        else :
            print("Suppression impossible. Pile vide")
            return "aucune"

    # Récupère la dernière valeur ajoutée à la pile
    def lireSommet(self) :
        if self.estVide() == False :
            if self.nombreDelements() == 1 :
                return self.valeurs[0]
            else :
                return self.valeurs[-1]

    # Affichage de la pile
    def __str__(self) :
        ch = ''
        for x in self.valeurs :
            #print(x)
            # \t : tabulation
            # \n : saut de ligne
            ch = "|\t" + str(x) + "\t|" + "\n" + ch
        ch = "\nEtat de la pile:\n" + ch
        return ch
