from itertools import count
from itertools import islice


def sum_of_squares(n):
    return sum(islice((x * x for x in count()), n))


print(sum_of_squares(1000))



