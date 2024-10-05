while True:
    try:
        # Запрос ввода двух целых чисел
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))
        
        # Вычисление суммы
        result = num1 + num2
        
        # Вывод результата
        print(f"Сумма {num1} и {num2} равна {result}.")
    except ValueError:
        print("Ошибка: пожалуйста, введите целые числа.")
