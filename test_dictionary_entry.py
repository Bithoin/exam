import unittest
from main import DictionaryEntry

class TestDictionaryEntry(unittest.TestCase):

    def setUp(self):
        self.word = "test"
        self.meanings = ["to check", "to try"]
        self.entry = DictionaryEntry(self.word, self.meanings)

    def test_init(self):
        self.assertEqual(self.entry.word, self.word)
        self.assertEqual(self.entry.meanings, self.meanings)

    def test_str(self):
        self.assertEqual(str(self.entry), "test: to check, to try")

    def test_to_dict(self):
        expected_dict = {"word": "test", "meanings": ["to check", "to try"]}
        self.assertEqual(self.entry.to_dict(), expected_dict)

    def test_from_dict(self):
        data = {"word": "test", "meanings": ["to check", "to try"]}
        new_entry = DictionaryEntry.from_dict(data)
        self.assertEqual(new_entry.word, "test")
        self.assertEqual(new_entry.meanings, ["to check", "to try"])

if __name__ == '__main__':
    unittest.main()
