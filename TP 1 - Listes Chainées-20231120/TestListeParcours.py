from ListeChainee import ListeChainee
import unittest

class TestListeParcours(unittest.TestCase) :

    def testListeVide(self) :
        liste = ListeChainee(0, None)
        self.assertEqual(liste.getTaille(), 0, "La taille de la liste est 0")
        self.assertTrue(not liste.contient(1), "La liste ne contient pas de 1")

    def testListe1Element(self) :
        liste = ListeChainee(1, ListeChainee(0, None))
        self.assertEqual(liste.getTaille(), 1, "La taille de la liste est 1")
        self.assertTrue(liste.contient(1), "La liste contient 1")
        self.assertTrue(not liste.contient(2), "La liste ne contient pas de 2")

    def testListe2Elements(self) :
        liste = ListeChainee(1, ListeChainee(2, ListeChainee(0, None)))
        self.assertEqual(liste.getTaille(), 2, "La taille de la liste est 1")
        self.assertTrue(liste.contient(2), "La liste contient 2")

    def testElementNonTrouve(self) :
        liste = ListeChainee(1, ListeChainee(2, ListeChainee(0, None)))
        self.assertEqual(liste.getTaille(), 3, "La taille de la liste est 3")
        self.assertTrue(liste.contient(3), "La liste contient 3")

if __name__ == '__main__':
    unittest.main()
