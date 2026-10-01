# #todo Задача 1. Чтение матрицы, load_matrix(filename)
# # Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)

# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36


# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.

# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

def load_matrix(filename):
    matrix = [
        [int(num) for num in line.split()]
        for line in open(filename, 'r', encoding='utf-8') if line.strip()
    ]

    if not matrix:
        return matrix
    first_len = len(matrix[0])
    all_same_length = all(
        [len(row) == first_len for row in matrix]
    )

    return matrix if all_same_length else False

test_filename = "matrix.txt"
test_data = """11 12 13 14 15 16
21 22 23 24 25 26
31 32 33 34 35 36
"""

with open(test_filename, "w", encoding="utf-8") as f:
    f.write(test_data)

result = load_matrix(test_filename)
print("Результат загрузки матрицы:", result)

bad_filename = "bad_matrix.txt"
bad_data = """1 2 3
4 5
6 7 8 9
"""
with open(bad_filename, "w", encoding="utf-8") as f:
    f.write(bad_data)

bad_result = load_matrix(bad_filename)
print("Результат для некорректной матрицы:", bad_result)
