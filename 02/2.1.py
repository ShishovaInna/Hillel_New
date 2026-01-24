#Квадрат числа
any_number = float(input("Enter any number: "))
print("Square of a number: ", any_number ** 2)

#Середнє трьох чисел
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
third_number = float(input("Enter third number: "))
mean = (first_number + second_number + third_number) / 3
print("Arithmetic mean: ", mean)

#Перетворення хвилин у години
minutes = int(input("Введіть кількість хвилин: "))
print(minutes // 60, "год.", minutes % 60, "хв.")

#Розрахунок знижки
price = float(input("Введіть ціну: "))
discount = float(input("Введіть знижку (%): "))
print("Ціна зі знижкою: ", price * (1 - discount / 100))

#Остання цифра числа
number = int(input("Введіть число: "))
print("Остання цифра: ", number % 10)

#Периметр прямокутника
a = int(input("Введіть довжину: "))
b = int(input("Введіть ширину: "))
print("Периметр: ", (a+b)*2)

#Виведення числа в стовпчик
c = int(input("Введіть 4-х значне число з клавіатури: "))
print(c // 1000)
print((c // 100) % 10)
print((c // 10) % 10)
print(c % 10)
