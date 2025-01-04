# Dictionary Management System

This project is a Python-based Dictionary Management System where users can manage multiple dictionaries, add words, edit entries, delete words, and export words to files. The data is stored in text files, ensuring persistence across different sessions.

## Features

- **Dictionary Management**: 
  - Create, select, list, and delete dictionaries.
  - Dictionary data is saved to a text file for persistence.
  
- **Word Management**: 
  - Add, edit, and delete words and their meanings in selected dictionaries.
  - Manage multiple meanings for a single word.
  
- **Search and Export**:
  - Search for words and their meanings.
  - Export a word and its meanings to a separate text file.
  
## Classes

### `DictionaryEntry`

Represents an entry in the dictionary consisting of a word and its meanings.

#### Methods
- `__init__(self, word: str, meanings: list)`
- `__str__(self)`
- `to_dict(self)`
- `from_dict(data)`

### `Dictionary`

Represents the dictionary itself, containing words and their meanings.

#### Methods
- `__init__(self, name: str, type: str)`
- `add_entry(self, word: str, meanings: list)`
- `edit_entry(self, word: str, new_meanings: list)`
- `edit_word(self, old_word: str, new_word: str)`
- `delete_entry(self, word: str)`
- `delete_meaning(self, word: str, meaning: str)`
- `search_entry(self, word: str)`
- `save_to_file(self)`
- `load_from_file(self)`
- `export_word_to_file(self, word: str)`

### `DictionaryManager`

Manages multiple dictionaries and allows for creating, selecting, and deleting dictionaries.

#### Methods
- `create_dictionary(self, name: str, type: str)`
- `select_dictionary(self, name: str)`
- `get_current_dictionary(self)`
- `delete_dictionary(self, name: str)`
- `list_dictionaries(self)`

### `Menu`

Provides an interactive menu system for navigating through the actions in the application.

#### Methods
- `add_option(self, option: MenuOption)`
- `show_submenu(self, submenu_options)`
- `show_menu(self)`

### `MenuOption`

Represents an option in the menu system.

#### Methods
- `__init__(self, name: str, action)`

## Usage

1. Clone the repository or download the Python file.

   ```bash
   git clone https://github.com/your-username/dictionary-management-system.git
