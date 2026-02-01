#my_list = [0, 1, 7, 2, 4, 8]
my_list = [1, 3, 5]
#my_list = [6]
#my_list = []
if not my_list:
    print(0)
else:
    resultat = 0
    for index, element in enumerate(my_list):
        if (index % 2 == 0):
            resultat += element
    resultat = resultat * my_list[- 1]
    print(resultat)
