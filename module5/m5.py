import sys

DIGIT_MAP = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def convert(s):
    """ Converts a string to a number.

    Args:
        s: The string to convert.

    Returns:
        The string as a number.

    Raises:
        KeyError: The string was not found in the dictionary.
    """
    number = ""
    invalid_tokens = set()

    for token in s:
        if token not in DIGIT_MAP:
            invalid_tokens.add(token)
        else:
            number += DIGIT_MAP[token]

    if len(invalid_tokens) > 0:
        raise KeyError(f"Invalid tokens: {invalid_tokens}")

    return int(number)
