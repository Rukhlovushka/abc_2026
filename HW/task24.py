# # todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.


with open('message.txt', 'w', encoding='utf-8') as f:
    f.write("Привет, мир!\n")
    f.write("Это вторая строка.\n")
    f.write("А это третья.")

ALPHABET_UPPER = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ALPHABET_LOWER = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char in ALPHABET_UPPER:
            new_index = (ALPHABET_UPPER.index(char) - shift) % len(ALPHABET_UPPER)
            result += ALPHABET_UPPER[new_index]
        elif char in ALPHABET_LOWER:
            new_index = (ALPHABET_LOWER.index(char) - shift) % len(ALPHABET_LOWER)
            result += ALPHABET_LOWER[new_index]
        else:
            result += char
    return result

with open('message.txt', 'r', encoding='utf-8') as infile, open('encrypted.txt', 'w', encoding='utf-8') as outfile:
    for line_number, line in enumerate(infile, start=1):
        shift = line_number
        encrypted_line = caesar_cipher(line, shift)
        outfile.write(encrypted_line)

print("Шифрование завершено. Результат в файле encrypted.txt")




