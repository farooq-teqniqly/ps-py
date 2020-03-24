import sys
from urllib.request import urlopen


def get_words(url):
    try:
        book = urlopen(url)
        word_list = []

        for line in book:
            words = line.decode("utf8").split()

            for word in words:
                word_list.append(word)

        return word_list
    finally:
        book.close()


def print_words(word_list):
    for word in word_list:
        print(word)


def main(url):
    words = get_words(url)
    print_words(words)


if __name__ == "__main__":
    main(sys.argv[1])
