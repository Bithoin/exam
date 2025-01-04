import unittest
from main import DictionaryManager

class TestDictionaryManager(unittest.TestCase):

    def setUp(self):
        self.manager = DictionaryManager()

    def test_create_dictionary(self):
        result = self.manager.create_dictionary("test_dict", "English-Russian")
        self.assertEqual(result, "Словник 'test_dict' створено.")
        self.assertIn("test_dict", self.manager.dictionaries)

    def test_select_dictionary(self):
        self.manager.create_dictionary("test_dict", "English-Russian")
        result = self.manager.select_dictionary("test_dict")
        self.assertEqual(result, "Словник 'test_dict' вибрано з пам'яті.")
        self.assertIsNotNone(self.manager.get_current_dictionary())

    def test_delete_dictionary(self):
        self.manager.create_dictionary("test_dict", "English-Russian")
        result = self.manager.delete_dictionary("test_dict")
        self.assertEqual(result, "Словник 'test_dict' і його файл видалено.")
        self.assertNotIn("test_dict", self.manager.dictionaries)

if __name__ == '__main__':
    unittest.main()
