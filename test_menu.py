import unittest
from unittest.mock import patch
from main import Menu, MenuOption, DictionaryManager

class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()
        self.manager = DictionaryManager()

    @patch('builtins.input', return_value="1")
    def test_show_menu_manage_dictionaries(self, mock_input):
        self.menu.add_option(MenuOption("Управління словниками", self.menu.manage_dictionaries))
        self.menu.show_menu()
        self.assertTrue(mock_input.called)

    @patch('builtins.input', return_value="2")
    def test_show_menu_work_with_dictionary(self, mock_input):
        self.menu.add_option(MenuOption("Робота з словником", self.menu.work_with_dictionary))
        self.menu.show_menu()
        self.assertTrue(mock_input.called)

    def test_add_option(self):
        option = MenuOption("Option 1", lambda: None)
        self.menu.add_option(option)
        self.assertEqual(len(self.menu.options), 1)

if __name__ == '__main__':
    unittest.main()
