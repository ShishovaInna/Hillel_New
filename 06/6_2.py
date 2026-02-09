number = int(input('Введіть число від 0 до 8640000: '))
days_count = number // (24*60*60)
hours_count = (number % (24*60*60)) // (60 *60)
minutes_count = ((number % (24*60*60)) % (60 *60)) // 60
seconds_count = number % 60

if (days_count % 10 == 1 or days_count == 1) and (days_count != 11):
    word_form = 'день'
elif ((days_count in [2, 3, 4] or days_count % 10 in [2, 3, 4])
    and days_count not in [12, 13, 14]):
    word_form = 'дні'
else:
    word_form = 'днів'

print(f'{days_count} {word_form}, {hours_count:02}:{minutes_count:02}:{seconds_count:02}')
