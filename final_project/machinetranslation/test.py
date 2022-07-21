import unittest
from translator import englishToFrench, frenchToEnglish

class Tests(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(None), None)
        self.assetEqual(englishToFrench("Hello"), "Bonjour")


    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(None), None)
        self.assetEqual(frenchToEnglish("Bonjour"), "Hello")


if __name__ == "__main__":
    unittest.main()