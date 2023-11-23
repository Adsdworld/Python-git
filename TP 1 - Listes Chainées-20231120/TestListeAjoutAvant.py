from ListeChainee import ListeChainee
import unittest

class TestListeAjoutAvant(unittest.TestCase) :

    def testListe1Element(self) :
        liste = ListeChainee(1, ListeChainee(0, None))
        print("test taille 0 : ",liste.getTaille())
        print("test liste 0 ",liste)
        liste = liste.ajouteAvant(2, 1)
        print("test liste 1 ",liste)
        print("test taille 1 : ",liste.getTaille())
        self.assertEqual(liste.getTaille(), 2, "La taille de la liste est 2")
        self.assertEqual(liste.getTete(), 2, "Le premier élément de la liste est 2")
        self.assertEqual(liste.getReste().getTete(), 1, "Le second élément de la liste est 1")

    def testListe2Elements(self) :
        liste = ListeChainee(1, ListeChainee(2, ListeChainee(0, None)))
        liste = liste.ajouteAvant(3, 2)
        print(liste)
        self.assertEqual(liste.getTaille(), 3, "La taille de la liste est 3")
        self.assertEqual(liste.getTete(), 1, "Le premier élément de la liste est 1")
        self.assertEqual(liste.getReste().getTete(), 3, "Le second élément de la liste est 3")
        self.assertEqual(liste.getReste().getReste().getTete(), 2, "Le troisième élément de la liste est 2")


    def testElementNonTrouve(self) :
        liste = ListeChainee(1, ListeChainee(2, ListeChainee(0, None)))
        liste = liste.ajouteAvant(3, 0)
        print("non trouve", liste)
        self.assertEqual(liste.getTaille(), 2, "La taille de la liste est 2")
        self.assertEqual(liste.getTete(), 1, "Le premier élément de la liste est 1")
        self.assertEqual(liste.getReste().getTete(), 2, "Le second élément de la liste est 2")

if __name__ == '__main__':
    unittest.main()
