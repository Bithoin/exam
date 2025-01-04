import unittest

# Імпортуємо тести з окремих файлів
from test_dictionary_entry import TestDictionaryEntry
from test_dictionary import TestDictionary
from test_dictionary_manager import TestDictionaryManager
from test_menu import TestMenu

def run_all_tests():
    test_suite = unittest.TestSuite()

    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestDictionaryEntry),
        unittest.TestLoader().loadTestsFromTestCase(TestDictionary),
        unittest.TestLoader().loadTestsFromTestCase(TestDictionaryManager),
        unittest.TestLoader().loadTestsFromTestCase(TestMenu)
    ])

    runner = unittest.TextTestRunner()
    runner.run(test_suite)

if __name__ == '__main__':
    run_all_tests()
