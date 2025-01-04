import unittest
from main import Dictionary

class TestDictionary(unittest.TestCase):

    def setUp(self):
        self.dict_name = "my_dict"
        self.dict_type = "English-Russian"
        self.dictionary = Dictionary(self.dict_name, self.dict_type)

    def test_add_entry(self):
        result = self.dictionary.add_entry("hello", ["привіт", "здравствуйте"])
        self.assertEqual(result, "Запис для слова 'hello' додано.")
        self.assertIn("hello", self.dictionary.entries)

    def test_edit_entry(self):
        self.dictionary.add_entry("hello", ["привіт", "здравствуйте"])
        result = self.dictionary.edit_entry("hello", ["hi", "greetings"])
        self.assertEqual(result, "Значення для слова 'hello' оновлено.")
        self.assertEqual(self.dictionary.entries["hello"], ["hi", "greetings"])

    def test_delete_entry(self):
        self.dictionary.add_entry("hello", ["привіт", "здравствуйте"])
        result = self.dictionary.delete_entry("hello")
        self.assertEqual(result, "Запис для слова 'hello' видалено.")
        self.assertNotIn("hello", self.dictionary.entries)

    def test_search_entry(self):
        self.dictionary.add_entry("hello", ["привіт", "здравствуйте"])
        result = self.dictionary.search_entry("hello")
        self.assertEqual(result, "hello: привіт, здравствуйте")

if __name__ == '__main__':
    unittest.main()
