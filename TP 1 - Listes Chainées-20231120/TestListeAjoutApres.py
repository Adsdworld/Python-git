from ListeChainee import ListeChainee
import unittest

class TestListeAjoutApres(unittest.TestCase) :

    def testListe1Element(self) :
        vide = ListeChainee(0, None)
        liste = ListeChainee(1, vide)
        liste = liste.ajouteApres(2, 1)
        print(liste)
        self.assertEqual(liste.getTaille(), 2, "La taille de la liste est 2")
        self.assertEqual(liste.getTete(), 1, "Le premier élément de la liste est 1")
        self.assertEqual(liste.getReste().getTete(), 2, "Le second élément de la liste est 2")

    def testListe2Elements(self) :
        liste = ListeChainee(1, ListeChainee(2, ListeChainee(0, None)))
        liste = liste.ajouteApres(3, 1)
        print(liste)
        self.assertEqual(liste.getTaille(), 3, "La taille de la liste est 3")
        self.assertEqual(liste.getTete(), 1, "Le premier élément de la liste est 1")
        self.assertEqual(liste.getReste().getTete(), 3, "Le second élément de la liste est 3")
        self.assertEqual(liste.getReste().getReste().getTete(), 2, "Le troisième élément de la liste est 2")


    def testElementNonTrouve(self) :
        liste = ListeChainee(1, ListeChainee(2, ListeChainee(0, None)))
        liste = liste.ajouteApres(3, 0)
        print(liste)
        self.assertEqual(liste.getTaille(), 2, "La taille de la liste est 2")
        self.assertEqual(liste.getTete(), 1, "Le premier élément de la liste est 1")
        self.assertEqual(liste.getReste().getTete(), 2, "Le second élément de la liste est 2")

if __name__ == '__main__':
    unittest.main()

