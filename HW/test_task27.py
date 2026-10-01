from helpers import logger, caesar_encrypt, caesar_decrypt

def main():
    logger.info("=== Начало теста helpers ===")

    original = "Hello, World! Привет, Мир!"
    encrypted = caesar_encrypt(original, shift=3)
    decrypted = caesar_decrypt(encrypted, shift=3)

    logger.info(f"Исходный:   {original}")
    logger.info(f"Зашифрован: {encrypted}")
    logger.info(f"Расшифрован: {decrypted}")

    assert original == decrypted, "Ошибка расшифровки!"
    logger.info("Тест шифра Цезаря пройден успешно!")
    logger.info("=== Тест завершён ===")

if __name__ == "__main__":
    main()
