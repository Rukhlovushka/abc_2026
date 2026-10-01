#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


#grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

def caesar_bruteforce(ciphertext: str) -> str:
    best_shift = None
    best_text = ""
    keywords = ["although", "obvious", "dutch"]

    for shift in range(1, 26):
        result = []
        for ch in ciphertext:
            if 'a' <= ch <= 'z':
                base = ord('a')
                offset = (ord(ch) - base - shift) % 26
                result.append(chr(base + offset))
            elif 'A' <= ch <= 'Z':
                base = ord('A')
                offset = (ord(ch) - base - shift) % 26
                result.append(chr(base + offset))
            else:
                result.append(ch)
        decoded = ''.join(result)
        print(f"Сдвиг {shift:2d}: {decoded}")

        lower_text = decoded.lower()
        if all(kw in lower_text for kw in keywords):
            best_shift = shift
            best_text = decoded

    return best_text

encoded = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

if __name__ == "__main__":
    print("=== Полный перебор всех сдвигов ===\n")
    found_phrase = caesar_bruteforce(encoded)
    print("\n" + "=" * 40)
    print("НАЙДЕНА РАСШИФРОВАННАЯ ФРАЗА:")
    print(found_phrase)
    print("=" * 40)
