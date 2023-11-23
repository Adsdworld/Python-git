from ListeChainee import ListeChainee
import unittest

class TestListeVide(unittest.TestCase) :

    def testListeVide(self) :
        liste = ListeChainee(0, None)
        self.assertTrue(liste.estVide(), "La  liste est vide")

if __name__ == '__main__':
    unittest.main()
