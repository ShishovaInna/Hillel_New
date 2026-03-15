from human import Human
from database import ListPeople
registry = ListPeople()
while True:
    print('''
    1. Відкрити файл
    2. Записати файл
    3. Додати дані про людину
    4. Шукати дані про людину
    5. Закінчити роботу
    ''')
    print('Щоб продовжити роботу, натисніть потрібну цифру: ')
    choice = input()
    if choice == '1':
        registry.load_from_file('People')
        continue
    elif choice == '2':
        registry.save_to_file('People')
        continue
    elif choice == '3':
        first_name = input('Ім\'я: ')
        father_name = input('Прізвище: ') or None
        last_name = input('По батькові: ') or None
        gender = input('m/f: ')
        birth_str = input('Дата народження (дд.мм.рррр): ')
        data_birth = Human.replace_date(birth_str)
        death_str = input('Дата смерті (якщо є): ')
        data_death = Human.replace_date(death_str) if death_str else None
        new_person = Human(first_name, gender, data_birth, data_death, father_name, last_name)
        registry.add_people(new_person)
        print('Запис додано!')
        continue
    elif choice == '4':
        query = input('Введіть ім\'я для пошуку: ')
        results = registry.search_people(query)
        if not results:
            print('Нічого не знайдено.')
        else:
            age = results.calculate_age()
            gender_text = "чоловік" if results.gender == "m" else "жінка"
            born_text = "Народився" if results.gender == "m" else "Народилася"
            print(
                f'{results.get_full_name()} {age} років, {gender_text}: {born_text} {results.data_birth.strftime('%d.%m.%Y')}.')
        continue
    else:
        break
