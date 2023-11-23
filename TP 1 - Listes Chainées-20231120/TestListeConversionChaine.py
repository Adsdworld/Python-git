from ListeChainee import ListeChainee
import unittest

class TestListeConversionChaine(unittest.TestCase) :

    def testListeVide(self) :
        liste = ListeChainee(0, None)
        self.assertEqual(str(liste), "{}", "La représentation de la liste est {}")

    def testListe1Element(self) :
        liste = ListeChainee(1, ListeChainee(0, None))
        print(liste)
        self.assertEqual(str(liste), "1->{}", "La représentation de la liste est 1->{}")
 
    def testListe2Elements(self) :
        liste = ListeChainee(1, ListeChainee(2, (ListeChainee(0, None))))
        print(liste)
        self.assertEqual(str(liste), "1->2->{}", "La représentation de la liste est 1->2->{}")
 
    def testElement3Elements(self) :
        liste = ListeChainee(1, ListeChainee(2, ListeChainee(3, ListeChainee(0, None))))
        print(liste)
        self.assertEqual(str(liste), "1->2->3->{}", "La représentation de la liste est 1->2->3->{}")

if __name__ == '__main__':
    unittest.main()
