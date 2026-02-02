answer_str = "Y"
while answer_str == "Y":
    a = float(input("Введіть перше число: "))
    operation = input("Введіть математичну дію (+, -, *, /): ")
    b = float(input("Введіть друге число: "))
    if operation == "+":
        print("Результат: ", a, operation, b, " = ", a + b)
    elif operation == "-":
        print("Результат: ", a, operation, b, " = ", a - b)
    elif operation == "*":
        print("Результат: ", a, operation, b, " = ", a * b)
    elif operation == "/":
        if b == 0:
            print("Ділення на 0!")
        else: print("Результат: ", a, operation, b, " = ", a / b)
    else:
        print("Невідома математична дія")
    answer_str = input("Продовжуємо? Натисніть Y/N: ").upper()
else:
    print("До зустрічі наступного разу!")
