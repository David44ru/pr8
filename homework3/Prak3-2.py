def draw_hollow_square(size):
    for i in range(size):
        for j in range(size):
            # Рисуем границы квадрата
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')  # Пустое пространство внутри
        print()  # Переход на новую строку

if __name__ == "__main__":
    draw_hollow_square(10)
