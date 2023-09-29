from _collections_abc import Iterator


def example1() -> Iterator[int]:
    x = 4
    yield x
    x *= 2
    yield x
    x += 3
    yield x


def pow2() -> Iterator[int]:
    i = 1
    while True:
        yield i
        i *= 2



if __name__ == '__main__':
    g1 = example1()
    print(f'{next(g1) = }')
    print(f'{next(g1) = }')
    print(f'{next(g1) = }')
    # print(f'{next(g1) = }')
    for i in example1():
        print(f'{i = }')
    g2 = pow2()
    print(f'{next(g2) = }')
    print(f'{next(g2) = }')
    print(f'{next(g2) = }')
    print(f'{next(g2) = }')
    for i in g2:
        print(f'{i = }')
        if i > 1_000:
            break