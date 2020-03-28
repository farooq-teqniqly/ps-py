def first_n_numbers(n):
    for x in range(n):
        yield x


# Prints 0 - 9
for n in first_n_numbers(10):
    print(n)


def take(count, iterable):
    counter = 0

    for i in iterable:
        if counter == count:
            return

        counter += 1
        yield i


items = range(10)

# Prints 0 - 2
for i in take(3, items):
    print(i)


def distinct(iterable):
    s = set()

    for i in iterable:
        if i not in s:
            s.add(i)
            yield i


items = [0, 0, 1, 1, 2, 2, 3, 3]

# Prints 0, 1, 2, 3
for i in distinct(items):
    print(i)

def filter(iterable, func):
    for i in iterable:
        if func(i):
            yield i


items = range(10)

# Prints even numbers between 0 and 9
for i in filter(items, lambda j: j % 2 == 0):
    print(i)

# Combining iterators. Prints 2, 4, 6
items = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8]

for i in take(3, filter(distinct(items), lambda j: j % 2 == 0)):
    print(i)
