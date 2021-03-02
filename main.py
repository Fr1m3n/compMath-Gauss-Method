from components.Matrix import Matrix
from components.Vector import Vector
import sys

FILE_ARG_KEY = "file"
n = None


def get_header_for_vector(s):
    global n
    temp = [s + str(i) for i in range(1, n + 1)]
    return ''.join(map(lambda x: '{:<10.3}'.format(x), temp))


def read(file):
    matrix = Matrix()
    b_matrix = Vector()

    def f(input_f, comment):
        global n
        if comment:
            print("Введите n: ")
        n = int(input_f())
        b_matrix.nums = [0 for _ in range(n)]
        if comment:
            print("Введите матрицу A и вектор b (вектор b должен быть представлен как n+1 столбец матрицы A:")
        for i in range(n):
            nums = input_f().strip().split(' ')
            b_matrix[i] = float(nums[-1])
            matrix.add_line(Vector(list(map(float, nums[:-1]))))
        return matrix, b_matrix

    if file[0] is True:
        with open(file[1], 'r') as file:
            return f(file.readline, False)
    else:
        return f(input, True)


def is_file_argument_presented():
    for arg in sys.argv:
        splitted_arg = arg.split('=')
        if splitted_arg[0] == FILE_ARG_KEY:
            return True, splitted_arg[1]
    return False, ''


def main():
    global n
    file_name = is_file_argument_presented()
    try:
        matrix, b_vector = read(file_name)  # Решаем, откуда читать и читаем собсна
    except ValueError as e:
        print("Ввод некорректный. Где-то встретился некорректный символ (во вводе допускаются только числа).")
        return
    print(f"Размерность матрицы A: {n}")
    print("\nВведённая матрица коэффициентов A:")
    print(get_header_for_vector('x'))
    print(matrix)
    print("\nВведённый вектор b:")
    print(get_header_for_vector('b'))
    print(b_vector)
    matrix.get_triangle(b_vector)  # Приводим матрицу к треугольному виду
    print("\nМатрица A, приведённая к треугольному виду: ")
    print(get_header_for_vector('x'))
    print(matrix)
    print("\nВектор b после преобразования матрицы A к треугольному виду:")
    print(get_header_for_vector('b'))
    print(b_vector)
    determinator = matrix.det()  # Считаем определитель, нам не лень
    print(f"\nОпределитель матрицы A: {matrix.det()}")
    if determinator == 0.0:  # Ну блин, если определитель равен нулю - наши полномочия тут всё
        print("Определитель равен нулю.\n"
              "Система либо имеет бесконечное кол-во решений, либо не имеет вовсе.\n"
              "Завершение работы программы.")
        return
    x_vector = matrix.solve(b_vector)  # Решаем эту СЛАУ. Ну и само собой сохраняем вектор иксов.
    print("\nВектор неизвестных x:")
    print(get_header_for_vector('x'))
    print(x_vector)
    r_vector = matrix.get_discrepancy(x_vector,
                                      b_vector)  # Неувязочки посчитаем, я загуглил невязка переводится именно так
    print(f"\nВектор невязок r:")
    print(get_header_for_vector('r'))
    print(r_vector)


if __name__ == '__main__':
    main()
