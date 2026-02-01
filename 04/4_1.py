#my_list = [0, 1, 0, 12, 3]
#my_list = [0]
#my_list = [1, 0, 13, 0, 0, 0, 5]
my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
my_list_interim = []
count_zeros = 0
for element in my_list:
    if element != 0:
        my_list_interim.append(element)
        continue
    count_zeros += 1
my_list = my_list_interim + count_zeros * [0]
print(my_list)
