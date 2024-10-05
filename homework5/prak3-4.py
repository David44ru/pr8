def main():
    total_sum = 0
    
    while True:
        user_input = input("Введите число (или 'stop'/'end' для завершения): ")
        
        if user_input.lower() in ['stop', 'end']:
            break
        
        try:
            number = float(user_input)  # Преобразуем ввод в число
            total_sum += number          # Добавляем к общей сумме
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    print(f"Сумма введенных чисел: {total_sum}")

if __name__ == "__main__":
    main()
