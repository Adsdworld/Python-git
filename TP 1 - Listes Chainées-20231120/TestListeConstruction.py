from ListeChainee import ListeChainee
import unittest

class TestListeConstruction(unittest.TestCase) :

    def testListe1Element(self) :
        liste = ListeChainee(1, ListeChainee(0, None))
        print("testListe1Element ", liste)
        self.assertTrue(not liste.estVide(), "La liste n'est pas vide")
        self.assertEqual(liste.getTete(), 1, "Le premier élément de la liste est 1")

    def testListe2Elements(self) :
        liste = ListeChainee(1, ListeChainee(2, ListeChainee(0, None)))
        print("testListe2Elements ", liste)
        self.assertTrue(liste.getTaille(), 2)
        self.assertEqual(liste.getTete(), 1, "Le premier élément de la liste est 1")
        self.assertEqual(liste.getReste().getTete(), 2, "Le second élément de la liste est 2")
 
    def testElementNonTrouve(self) :
        liste = ListeChainee(1, ListeChainee(2, ListeChainee(3, ListeChainee(0, None))))
        print("testElementNonTrouve ", liste)
        self.assertEqual(liste.getTete(), 1, "Le premier élément de la liste est 1")
        self.assertEqual(liste.getReste().getTete(), 2, "Le second élément de la liste est 2")
        self.assertEqual(liste.getReste().getReste().getTete(), 3, "Le second élément de la liste est 3")

if __name__ == '__main__':
    unittest.main()
