# Liste chainée d'entiers.
class ListeChainee :

    # Construit une nouvelle liste ayant la tête et le reste donné.
    # Le reste est la liste vide pour une nouvelle liste de type singleton
    # (un seul élément).
    # @param tete la tête de la nouvelle liste
    # @param reste le reste de la nouvelle liste
    def __init__(self, tete, reste=None):
        self.tete = tete
        self.reste = reste

    # Retourne la tête de la liste.
    # @return la tête de la liste
    def getTete(self) :
        return self.tete

    # Retourne le reste de la liste.
    # Si la liste est un singleton, son reste est la liste vide.
    # @return le reste de la liste
    def getReste(self) :
        return self.reste
        

    # Indique si la liste est vide ou non.
    # @return True si la liste est vide, False sinon
    def estVide(self) :
        if self.reste==None:
            return True
        else:
            return False
    
    # Indique si un élément est présent ou non dans la liste.
    # @param element l'élément à rechercher
    # @return True si l'élément est présent, False sinon
    def contient(self,element) :
        if self.getTete()==element:
            return True
        elif self.estVide():
            return False
        else:
            return self.getReste().contient(element)
    """        
    # Renvoie une nouvelle liste constituée des éléments de la liste en
    # excluant un élément donné.
    # Si l'élément donné n'est pas présent, une copie de la liste est renvoyée.
    # @param element l'élément à retirer
    # @return la nouvelle liste ne contenant pas l'élément
    def retire(self, element) :


    # Renvoie le nombre d'éléments de la liste.
    # @return le nombre d'éléments de la liste
    def getTaille(self) :
        while !self.estVide():
            #compter les têtes?
"""
        
    # Crée une représentation textuelle de la liste. La liste vide est
    # représentée par la chaîne "{}". Une liste contenant les entiers 1, 2 et 3
    # est représentée par la chaîne "1->2->3->{}".
    # @return une représentation textuelle de la liste
    def __str__(self) :      
        if self.estVide():
            return "{}"
        else:
            return str(self.getTete())+"->"+str(self.getReste())


"""     

    # Renvoie une nouvelle liste constituée des éléments de la liste contenant
    # en plus un élément situé juste après la première occurrence d'un élément
    # donné.
    # Si l'élément donné n'est pas présent, une copie de la liste est renvoyée.
    # @param element l'élément à ajouter
    # @param apresElement l'élément de la liste après lequel l'ajout est fait
    # @return la liste contenant l'élément ajouté après l'élément donné
    def ajouteApres(self, element, apresElement) :

        
    

    		
    # Renvoie une nouvelle liste constituée des éléments de la liste contenant
    # en plus un élément situé juste avant la première occurrence d'un élément
    # donné.
    # Si l'élément donné n'est pas présent, une copie de la liste est renvoyée.
    # @param element l'élément à ajouter
    # @param avantElement l'élément de la liste avant lequel l'ajout est fait
    # @return la nouvelle liste contenant l'élément ajouté avant l'élément
    # donné
    def ajouteAvant(self, element, avantElement) :
"""
        


ma_classe=ListeChainee(1, ListeChainee(2, ListeChainee(0, None)))

print("Tete: {}".format(ma_classe.getTete()))
print("reste: {}".format(ma_classe.getReste()))
print("estVide: {}".format(ma_classe.estVide()))
print("contient 1: {}".format(ma_classe.contient(1)))
print(ma_classe)