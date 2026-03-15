from datetime import date
class Human:
    def __init__(self, first_name, gender, data_birth, data_death = None, father_name = None, last_name = None):
        self.first_name = first_name
        self.father_name = father_name
        self.last_name = last_name
        self.gender = gender
        self.data_birth = data_birth
        self.data_death = data_death

    def calculate_age(self):
        """
        Обчислює кількість повних років людини
        :return: int
        """

        if self.data_death is not None:
            today = date.today()
        else:
            today = self.data_death

        age = today.year - self.data_birth.year

        if (self.data_birth.month, self.data_birth.day) > (today.month, today.day):
            age -= 1
        return age

    def get_full_name(self):
        """Збирає ПІБ в один рядок для зручного пошуку."""

        full_name = [self.last_name, self.first_name, self.father_name]
        return " ".join([x for x in full_name if x])

    @staticmethod
    def replace_date(date_str):
        """Перетворення дати"""
        if not date_str:
            return None
        new_date = date_str.replace(' ', '.').replace('/', '.').replace('-', '.')
        parts = new_date.split('.')
        return date(int(parts[2]), int(parts[1]), int(parts[0]))

    def to_dict(self):
        """Повертати дані людини у вигляді простого словника (для json)"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'father_name': self.father_name,
            'gender': self.gender,
            'data_birth': self.data_birth.strftime('%d.%m.%Y'), # Перетворюємо дату в рядок
            'data_death': self.data_death.strftime('%d.%m.%Y') if self.data_death else None
        }
