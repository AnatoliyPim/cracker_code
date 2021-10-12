import math
import itertools

ciphertext = "ДВЙЕЕ ЕЕРКИ ТОНМТ НДРВЕ ААПРС ЧМЕУО ДХЕВЕ ИЕЕЬВ"


def main():
    """Выполнить программу для дешифровки двухрядного зигзагообразного
       шифра."""
    message = prep_ciphertext(ciphertext)
    row1, row2 = split_rails(message)
    decrypt(row1, row2)


def prep_ciphertext(ciphertext):
    """Удалить пробелы."""
    message = "".join(ciphertext.split())
    print(f"\nШифротекст = {ciphertext}")
    return message


def split_rails(message):
    """Разбить сообщение на два, всегда округляя ВВЕРХ
       для первого ряда."""
    row_1_len = math.ceil(len(message) / 2)
    row1 = (message[:row_1_len])
    row2 = (message[row_1_len:])
    return row1, row2


def decrypt(row1, row2):
    """Построить список, чередуя буквы из 2 цепочек символов
       и напечатать."""
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1.lower())
        plaintext.append(r2.lower())
    if None in plaintext:
        plaintext.pop()
    print(f"Ряд 1 = {row1}")
    print(f"Ряд 2 = {row2}")
    print(f"\nОткрытый текст = {''.join(plaintext)}")


if __name__ == '__main__':
    main()
