import unittest
from translator import english_to_french, french_to_english

class TestTranslations(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Morning"), "Morning")


    def test_french_to_english(self):
        self.assertEqual(french_to_english(None), None)
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Matin"), "Matin")


if __name__ == "__main__":
    unittest.main()