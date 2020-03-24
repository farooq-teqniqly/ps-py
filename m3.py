"""
    A module containing helpers to download and print words contained in documents.

    Usage:
        python m3.py <URL>
"""


import sys
from urllib.request import urlopen


def get_words(url):
    """ Fetch a list of words from the specified URL.

        Args:
            url: The URL of a UTF-8 text document.

        Returns:
            A list of words from the document.
    """

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
    """ Print a list of words, one word per line.

            Args:
                word_list: The word list.

        """
    for word in word_list:
        print(word)


def main(url):
    """ Print a list of words from the specified URL.

            Args:
                url: The URL of a UTF-8 text document.

        """
    words = get_words(url)
    print_words(words)


if __name__ == "__main__":
    main(sys.argv[1])
