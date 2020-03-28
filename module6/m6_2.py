from glob import glob as glob
import os
from pprint import pprint as pp
from math import factorial


def is_odd(n):
    return n % 2 != 0


files = glob(f"{os.getcwd()}/*.*")

# Dictionary comprehension with a more complex expression
dictionary = {file: os.stat(file).st_size for file in files}
pp(dictionary)

# Dictionary comprehension filtering
files_with_odd_size = {file: os.stat(file).st_size for file in files if is_odd(os.stat(file).st_size)}
pp(files_with_odd_size)

files_with_even_size = {file: os.stat(file).st_size for file in files if not is_odd(os.stat(file).st_size)}
pp(files_with_even_size)

# Dictionary of tuples
dictionary_with_first_three_factorials = {x: (factorial(x), factorial(x + 1), factorial(x + 2)) for x in range(5)}
pp(dictionary_with_first_three_factorials)
