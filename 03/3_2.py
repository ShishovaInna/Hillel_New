#Перемістити елемент у списку

list1 = [12, 3, 4, 10]
list2 = [1]
list3 = []
list4 = [12, 3, 4, 10, 8]
my_list = list1
if len(my_list) > 1:
    last_element = my_list.pop()
    my_list.insert(0, last_element)
print(my_list)
