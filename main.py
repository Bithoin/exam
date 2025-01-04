import os

class DictionaryEntry:
    def __init__(self, word: str, meanings: list):
        self.word = word
        self.meanings = meanings

    def __str__(self):
        return f"{self.word}: {', '.join(self.meanings)}"

    def to_dict(self):
        return {"word": self.word, "meanings": self.meanings}

    @staticmethod
    def from_dict(data):
        return DictionaryEntry(data["word"], data["meanings"])


class Dictionary:
    def __init__(self, name: str, type: str):
        self.__name = name
        self.__type = type
        self.entries = {}
        self.load_from_file()

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_type(self, type: str):
        self.__type = type

    def get_type(self):
        return self.__type

    def add_entry(self, word: str, meanings: list):
        if word in self.entries:
            existing_meanings = self.entries[word]
            for meaning in meanings:
                if meaning not in existing_meanings:
                    existing_meanings.append(meaning)
            self.save_to_file()
            return f"Значення для слова '{word}' оновлено."
        else:
            self.entries[word] = meanings
            self.save_to_file()
            return f"Запис для слова '{word}' додано."

    def edit_entry(self, word: str, new_meanings: list):
        if word in self.entries:
            self.entries[word] = new_meanings
            self.save_to_file()
            return f"Значення для слова '{word}' оновлено."
        return f"Слово '{word}' не знайдено."

    def edit_word(self, old_word: str, new_word: str):
        if old_word in self.entries:
            self.entries[new_word] = self.entries.pop(old_word)
            self.save_to_file()
            return f"Слово '{old_word}' змінено на '{new_word}'."
        return f"Слово '{old_word}' не знайдено."

    def delete_entry(self, word: str):
        if word in self.entries:
            del self.entries[word]
            self.save_to_file()
            return f"Запис для слова '{word}' видалено."
        return f"Слово '{word}' не знайдено."

    def delete_meaning(self, word: str, meaning: str):
        if word in self.entries:
            meanings = self.entries[word]
            if len(meanings) == 1:
                return f"Не можна видалити останнє тлумачення слова '{word}'."
            if meaning in meanings:
                meanings.remove(meaning)
                self.save_to_file()
                return f"Тлумачення для слова '{word}' видалено."
            return f"Тлумачення '{meaning}' не знайдено для слова '{word}'."
        return f"Слово '{word}' не знайдено."

    def search_entry(self, word: str):
        if word in self.entries:
            return f"{word}: {', '.join(self.entries[word])}"
        return f"Слово '{word}' не знайдено."

    def save_to_file(self):
        filename = f"{self.__name}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Тип словника: {self.__type}\n")
            for word, meanings in self.entries.items():
                file.write(f"{word}:{','.join(meanings)}\n")

    def load_from_file(self):
        filename = f"{self.__name}.txt"
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                self.__type = file.readline().strip().split(":")[1].strip()
                for line in file:
                    word, meanings = line.strip().split(":", 1)
                    self.entries[word] = meanings.split(",")
        else:
            print(f"Файл '{filename}' не знайдено.")

    def export_word_to_file(self, word: str):
        if word in self.entries:
            filename = f"{word}.txt"
            with open(filename, "w", encoding="utf-8") as file:
                meanings = self.entries[word]
                file.write(f"{word}: {', '.join(meanings)}\n")
            return f"Слово '{word}' і його значення експортовано в файл '{filename}'."
        return f"Слово '{word}' не знайдено."


class DictionaryManager:
    def __init__(self):
        self.dictionaries = {}
        self.current_dictionary = None

    def create_dictionary(self, name: str, type: str):
        if name in self.dictionaries:
            return f"Словник з ім'ям '{name}' вже існує."
        self.dictionaries[name] = Dictionary(name, type)
        return f"Словник '{name}' створено."

    def select_dictionary(self, name: str):
        dictionary = self.dictionaries.get(name)
        if dictionary:
            self.current_dictionary = dictionary
            return f"Словник '{name}' вибрано з пам'яті."

        filename = f"{name}.txt"
        if os.path.exists(filename):
            new_dictionary = Dictionary(name, "Неізвестний")
            new_dictionary.load_from_file()
            self.dictionaries[name] = new_dictionary
            self.current_dictionary = new_dictionary
            return f"Словник '{name}' завантажено з файлу."

        return f"Словник '{name}' не знайдено."

    def get_current_dictionary(self):
        return self.current_dictionary

    def delete_dictionary(self, name: str):
        if name in self.dictionaries:
            del self.dictionaries[name]
        filename = f"{name}.txt"
        if os.path.exists(filename):
            os.remove(filename)
            return f"Словник '{name}' і його файл видалено."
        return f"Словник '{name}' не знайдено."

    def list_dictionaries(self):
        available_files = [f[:-4] for f in os.listdir('.') if f.endswith('.txt')]
        memory_dictionaries = list(self.dictionaries.keys())
        all_dictionaries = set(available_files + memory_dictionaries)
        if not all_dictionaries:
            return "Немає доступних словників."

        dictionary_info = []
        for name in all_dictionaries:
            type_ = self.dictionaries.get(name, None)
            if type_:
                type_ = type_.get_type()
            else:
                type_ = "Неізвестний"
            dictionary_info.append(f"{name} ({type_})")

        return "\n".join(dictionary_info)


class MenuOption:
    def __init__(self, name: str, action):
        self.name = name
        self.action = action


class Menu:
    def __init__(self):
        self.options = []

    def add_option(self, option: MenuOption):
        self.options.append(option)

    def show_submenu(self, submenu_options):
        while True:
            print("\nПідменю:")
            for i, option in enumerate(submenu_options, 1):
                print(f"{i}. {option.name}")
            print("0. Назад")

            choice = input("Виберіть пункт: ")
            if choice.isdigit() and 0 <= int(choice) <= len(submenu_options):
                choice = int(choice)
                if choice == 0:
                    break
                else:
                    submenu_options[choice - 1].action()
            else:
                print("Невірний вибір. Спробуйте ще раз.")

    def show_menu(self):
        while True:
            print("\nМеню:")
            print("1. Управління словниками")
            print("2. Робота з словником")
            print("0. Вихід")

            choice = input("Виберіть пункт: ")
            if choice == "0":
                print("Вихід з меню.")
                break
            elif choice == "1":
                self.manage_dictionaries()
            elif choice == "2":
                self.work_with_dictionary()
            else:
                print("Невірний вибір. Спробуйте ще раз.")

    def manage_dictionaries(self):
        submenu = [
            MenuOption("Створити словник", self.create_dictionary),
            MenuOption("Вибрати словник", self.select_dictionary),
            MenuOption("Список словників", self.list_dictionaries),
            MenuOption("Видалити словник", self.delete_dictionary),
        ]
        self.show_submenu(submenu)

    def work_with_dictionary(self):
        if manager.get_current_dictionary() is None:
            print("Спочатку виберіть словник.")
            return

        submenu = [
            MenuOption("Додати слово", self.add_word),
            MenuOption("Знайти слово", self.search_word),
            MenuOption("Редагувати слово", self.edit_word),
            MenuOption("Редагувати тлумачення", self.edit_meaning),
            MenuOption("Видалити слово", self.delete_word),
            MenuOption("Видалити тлумачення", self.delete_meaning),
            MenuOption("Експортувати слово в файл", self.export_word),
        ]
        self.show_submenu(submenu)

    def create_dictionary(self):
        name = input("Введіть ім'я словника: ")
        type_ = input("Введіть тип словника (наприклад, англо-російський): ")
        print(manager.create_dictionary(name, type_))

    def select_dictionary(self):
        name = input("Введіть ім'я словника для вибору: ")
        print(manager.select_dictionary(name))

    def list_dictionaries(self):
        print(manager.list_dictionaries())

    def delete_dictionary(self):
        name = input("Введіть ім'я словника для видалення: ")
        print(manager.delete_dictionary(name))

    def add_word(self):
        current_dictionary = manager.get_current_dictionary()
        word = input("Введіть слово: ")
        meanings = input("Введіть тлумачення через кому: ").split(", ")
        print(current_dictionary.add_entry(word, meanings))

    def search_word(self):
        current_dictionary = manager.get_current_dictionary()
        word = input("Введіть слово для пошуку: ")
        print(current_dictionary.search_entry(word))

    def edit_word(self):
        current_dictionary = manager.get_current_dictionary()
        old_word = input("Введіть старе слово: ")
        new_word = input("Введіть нове слово: ")
        print(current_dictionary.edit_word(old_word, new_word))

    def edit_meaning(self):
        current_dictionary = manager.get_current_dictionary()
        word = input("Введіть слово для редагування: ")
        new_meanings = input("Введіть нові тлумачення через кому: ").split(", ")
        print(current_dictionary.edit_entry(word, new_meanings))

    def delete_word(self):
        current_dictionary = manager.get_current_dictionary()
        word = input("Введіть слово для видалення: ")
        print(current_dictionary.delete_entry(word))

    def delete_meaning(self):
        current_dictionary = manager.get_current_dictionary()
        word = input("Введіть слово для видалення тлумачення: ")
        meaning = input("Введіть тлумачення для видалення: ")
        print(current_dictionary.delete_meaning(word, meaning))

    def export_word(self):
        current_dictionary = manager.get_current_dictionary()
        word = input("Введіть слово для експорту в файл: ")
        print(current_dictionary.export_word_to_file(word))


if __name__ == "__main__":
    manager = DictionaryManager()
    menu = Menu()
    menu.show_menu()
