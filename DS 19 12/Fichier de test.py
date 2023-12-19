#Arthur de Sallier Dupin P2 E2

from modules import controlerCarburant

import unittest

class controlerNiveauCarburant(unittest.TestCase) :

    def testControle1(self) :
        self.assertEqual(controlerCarburant(60,50,5), 600.0, "Le résultat est celui attendu")

    def testControle2(self) :
        self.assertEqual(controlerCarburant(90,25,9), 250.0, "Le résultat est celui attendu")     

if __name__ == '__main__':
    unittest.main()