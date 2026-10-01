# #todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

def numbers_to_letters(text: str) -> str:
    result = []
    tokens = text.split(' ')

    for token in tokens:
        if token.isdigit():
            num = int(token)
            if 1 <= num <= 26:
                letter = chr(ord('a') + num - 1)
                result.append(letter)
            else:
                result.append(token)
        else:
            result.append(token)

    return ' '.join(result)


print(numbers_to_letters("8 5 12 12 15"))

print(numbers_to_letters("8 5 12 12 15 , 0 23 15 18 12 4 !"))
