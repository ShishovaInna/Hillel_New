from human import Human
from database import ListPeople
registry = ListPeople()
filename = 'people.json'
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
        registry.load_from_file(filename)

    elif choice == '2':
        registry.save_to_file(filename)

    elif choice == '3':
        first_name = input('Ім\'я: ')
        father_name = input('По батькові: ') or None
        last_name = input('Прізвище: ') or None
        gender = input('м/ж: ')
        birth_str = input('Дата народження (дд.мм.рррр): ')
        data_birth = Human.replace_date(birth_str)
        death_str = input('Дата смерті (якщо є): ')
        data_death = Human.replace_date(death_str) if death_str else None
        new_person = Human(first_name, gender, data_birth, data_death, father_name, last_name)
        registry.add_people(new_person)
        print('Запис додано!')

    elif choice == '4':
        query = input('Введіть ім\'я для пошуку: ')
        results = registry.search_people(query)
        if not results:
            print('Нічого не знайдено.')
        else:
            for person in results:
                age = person.calculate_age()
                if (age % 10 == 1 or age == 1) and (age != 11):
                    age_text = 'рік'
                elif ((age in [2, 3, 4] or age % 10 in [2, 3, 4])
                      and age not in [12, 13, 14]):
                    age_text = 'роки'
                else:
                    age_text = 'років'
                gender_text = 'чоловік' if person.gender in ['m', 'м'] else 'жінка'
                born_text = 'народився' if person.gender in ['m', 'м'] else 'народилася'
                print(
                    f'{person.get_full_name()} {age} {age_text}, {gender_text}, {born_text} {person.data_birth.strftime("%d.%m.%Y")}.'
                )

    else:
        registry.save_to_file(filename)  # Рятуємо дані перед виходом
        print("Дані збережено. До побачення!")
        break
