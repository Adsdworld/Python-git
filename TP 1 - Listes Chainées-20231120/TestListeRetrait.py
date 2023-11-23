from ListeChainee import ListeChainee
import unittest

class TestListeAjoutAvant(unittest.TestCase) :

    def test1Retrait(self) :
        liste = ListeChainee(3, ListeChainee(3, ListeChainee(2, ListeChainee(1, ListeChainee(0, None)))))
        print("liste avant ",liste)
        liste = liste.retire(2)
        print("liste après ",liste)
        self.assertEqual(liste.getTete(), 3, "Le premier élément de la liste est 3")
        self.assertEqual(liste.getReste().getTete(), 3, "Le second élément de la liste est 3")
        self.assertEqual(liste.getReste().getReste().getTete(), 1, "Le troisième élément de la liste est 1")
        
    def test2Retraits(self) :
        liste = ListeChainee(3, ListeChainee(3, ListeChainee(2, ListeChainee(1, ListeChainee(0, None)))))
        print("liste avant ",liste)
        liste = liste.retire(2)
        liste = liste.retire(3)
        print("liste après ",liste)
        self.assertEqual(liste.getTete(), 3, "Le premier élément de la liste est 3")
        self.assertEqual(liste.getReste().getTete(), 1, "Le second élément de la liste est 1")
        
    def test3Retraits(self) :
        liste = ListeChainee(3, ListeChainee(3, ListeChainee(2, ListeChainee(1, ListeChainee(0, None)))))
        print("liste avant ",liste)
        liste = liste.retire(2)
        liste = liste.retire(3)
        liste = liste.retire(1)
        print("liste après ",liste)
        self.assertEqual(liste.getTete(), 3, "Le premier élément de la liste est 3")

    def testRetraitTous(self) :
        liste = ListeChainee(3, ListeChainee(3, ListeChainee(2, ListeChainee(1, ListeChainee(0, None)))))
        print("liste avant ",liste)
        liste = liste.retire(2)
        liste = liste.retire(3)
        liste = liste.retire(1)
        liste = liste.retire(3)
        print("liste après ",liste)
        self.assertTrue(liste.estVide(), "La liste est vide")
              
if __name__ == '__main__':
    unittest.main()
