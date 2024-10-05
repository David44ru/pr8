def print_integers_between(a, b):
    # Определяем меньшую и большую границу
    start = min(a, b) + 1
    end = max(a, b)

    # Выводим целые числа между a и b
    for num in range(start, end):
        print(num)

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное целое число.")

if __name__ == "__main__":
    a = get_integer_input("Введите первое число (a): ")
    b = get_integer_input("Введите второе число (b): ")
    
    print(f"Целые числа между {a} и {b}:")
    print_integers_between(a, b)
