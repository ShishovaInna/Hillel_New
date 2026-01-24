#Розділити один список на два списки
my_list = [1, 2, 3, 4, 5, 6]
i = (len(my_list) - 1) // 2
element1 = my_list[:i+1]
element2 = my_list[i+1:]
my_list_of_two = [element1, element2]
print(my_list_of_two)