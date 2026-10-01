#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# # Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

# Открываем файл для чтения и получаем список строк
with open('inverted_sort.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Очищаем строки от лишних символов (\n) и переворачиваем список
clean_lines = [line.strip() for line in lines]  # Убираем переносы строк
clean_lines.reverse()  # Переворачиваем список (теперь первая строка стала последней)

# Выводим строки в обратном порядке
for line in clean_lines:
    print(line)

# Дописываем строки в конец того же файла
with open('inverted_sort.txt', 'a', encoding='utf-8') as file:  # Режим 'a' — дописывание
    for line in clean_lines:
        file.write(line + '\n')  # Добавляем перенос строки при записи
