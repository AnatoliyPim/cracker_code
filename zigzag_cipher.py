plaintext = "Давай пересечем реку и отдохнем в тени деревьев"


def main():
    """Выполнить программу шифрования сообщения с помощью
       двухрядного зигзагообразного шифра."""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)


def prep_plaintext(plaintext):
    """Удалить пробелы и начальные/замыкающие пробелы."""
    message = "".join(plaintext.split())
    message = message.upper()

    print(f"\nОткрытый текст = {plaintext}")
    return message


def build_rails(message):
    """Построить семвольные цепочки, беря каждый второй символ
       в сообщении."""
    evens = message[::2]
    odds = message[1::2]
    rails = evens + odds
    return rails


def encrypt(rails):
    """Разбить буквы в шифротексте на куски по 5 букв и сцепить
       в одну цепочку."""
    ciphertext = ' '.join([rails[i:i + 5] for i in range(0, len(rails), 5)])

    print(f"Шифротекст = {ciphertext}")


if __name__ == '__main__':
    main()
