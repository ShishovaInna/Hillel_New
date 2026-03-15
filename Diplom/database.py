from human import Human
import json
class ListPeople:
    def __init__(self):
        self.people = []

    def add_people(self, people):
        """Додає до списку людину"""
        self.people.append(people)

    def search_people(self, query):
        """Пошук людини"""
        query = query.lower()
        results = []
        for person in self.people:
            if query in person.get_full_name().lower():
                results.append(person)
        return results

    def save_to_file(self, filename):
        """Запис даних до файлу"""
        # Створюємо список словників замість списку об'єктів
        data_to_save = [person.to_dict() for person in self.people]

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data_to_save, file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        """Зчитуємо текст із файлу"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data_list = json.load(file)
                self.people = []
                for item in data_list:
                    birth_date = Human.replace_date(item['data_birth'])
                    death_date = Human.replace_date(item['data_death']) if item['data_death'] else None

                    new_person = Human(
                        first_name = item['first_name'],
                        gender = item['gender'],
                        data_birth = birth_date,
                        data_death = death_date,
                        father_name = item.get('father_name'),
                        last_name = item.get('last_name')
                    )
                    self.add_people(new_person)
        except FileNotFoundError:
            print('Файл не знайдено.')
