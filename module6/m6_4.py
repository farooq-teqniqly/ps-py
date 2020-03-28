def n_squares(n):
    return (x * x for x in range(1, n))


def n_squares2(n):
    for i in range(1, n):
        yield i * i
