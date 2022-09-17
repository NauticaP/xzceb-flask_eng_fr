import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class testE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
        self.assertNotEqual(englishToFrench('0'), '0')

class testF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
        self.assertNotEqual(frenchToEnglish('0'), '0')

unittest.main()