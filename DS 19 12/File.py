#Arthur de Sallier Dupin P2 E2

class File:
    def __init__(self, capacite) :
        self.valeurs = []
        self.capacite = capacite

    # Retourne le nombre d'éléments de la file
    def recupTaille(self) :
        taille = 0;
        for i in range(len(self.valeurs)) :
            if self.valeurs[i] != None :
                taille += 1
        return taille

    # Renvoie True si la pile et vide et False sinon
    def estVide(self) :
        if self.recupTaille() == 0:
            return True
        else :
            return False#self.valeurs == []

    def estPleine(self) :
        if (self.recupTaille() == self.capacite) :
            return True
        else :
            return False

    # Ajoute un élément à la file
    def ajouter(self, valeur) :
        if self.estPleine() == False :
            self.valeurs.append(valeur)
        else :
            print("Ajout impossible. Pile pleine")

    # Supprime le premier élément de la file
    def enlever(self) :
        element = 0
        if self.estVide() == False :
            element = self.valeurs.pop(0)
        else :
            print("Suppression impossible. Pile vide")
            element = None
        return element
    '''def enlever(self) :
        element = 0
        if self.estVide() == False :
            element = self.valeurs[0]
            for i in range(self.recupTaille()-1) :
                self.valeurs[i] = self.valeurs[i+1]
            self.valeurs[self.recupTaille()-1]=None
        else :
            print("Suppression impossible. Pile vide")
            element = None
        return element'''
        
    # Récupère le premier élément ajouté
    def recupererPremier(self) :
        element = 0
        if self.estVide() == False :
            element = self.valeurs[0]
        return element

    # Affichage de la file
    def __str__(self) :
        ch = ''
        for x in self.valeurs :
            ch = ch + "-" + str(x) + "-"
        ch = "\nEtat de la file:\n" + ch
        return ch
