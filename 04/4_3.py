import random
number_elements = random.randint(3, 10)
my_list = random.choices(range(0,10), k = number_elements)
print(my_list)
second_list = []
for i in (0, 2, len(my_list) - 2):
    second_list.append(my_list[i])
print(second_list)
