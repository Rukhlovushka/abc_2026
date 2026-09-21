#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#
#
#Для числа 1 минимальное расcтояние в массиве по индексам: 0 и 7
#Для числа 2 минимальное расcтояние в массиве по индексам: 6 и 9
#Для числа 17 нет минимального расcтояния т.к элемент в массиве один.

mass = [12323,222,17,789,17,30,56,2,1,334,222]
found = []

for i in range(len(mass)):
    if mass[i] in found:
        continue
    for j in range(i+1, len(mass)):
        if mass[i] == mass[j]:
            print (f" для числа {mass[i]} минимальное расстояние"
                   f" в массиве по индексам: {i} и {j}")
            found.append(mass[i])
            break
all_numbers = []
for i in range(len(mass)):
    if mass[i] not in all_numbers:
        all_numbers.append(mass[i])
for num in all_numbers:
    if num in found:
        print(f" для числа {num} нет минимального расстояния, "
              f" т.к. элемент в массиве один")