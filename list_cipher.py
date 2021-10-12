from random import randint
import string
import load_dictionary

input_message = "Panel at east end of chapel slides"
word_list = load_dictionary.load('2of4brif.txt')


def editing_message(input_message):
    message = ''
    for chair in input_message:
        if chair in string.ascii_letters:
            message += chair
    print(message, "\n")
    message = ''.join(message.split())
    return message


def build_message(message):
    """Строит список словаря со скрытым сообщением."""
    vocab_list = []
    for letter in message:
        size = randint(6, 10)
        for word in word_list:
            if len(word) == size and word[2].lower() == letter.lower() \
                    and word not in vocab_list:
                vocab_list.append(word)
                break
    if len(vocab_list) < len(message):
        print("Список слов слишком мал. Попробуйте более крупный \
            словарь либо более короткое сообщение!")
    else:
        print("Слова словаря для блока 1: \n", *vocab_list, sep="\n")


def main():
    message = editing_message(input_message)
    build_message(message)


if __name__ == '__main__':
    main()
