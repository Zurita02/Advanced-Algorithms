x = 5
y = 8
z = 10


# AND
print(f'{x & y = :08b}')
print(f'{y & z = :08b}')


# OR
print(f'{x | y = :08b}')
print(f'{y | z = :08b}')


# XOR
print(f'{x ^ y = :08b}')
print(f'{y ^ z = :08b}')


# NOT
print(f'{~x = :08b}')
print(f'{~y = :08b}')
print(f'{~z = :08b}')


# SHL
print(f'{x << 1 = :08b}')
print(f'{y << 3 = :08b}')
print(f'{z << 4 = :08b}')


# SHR
print(f'{x >> 1 = :08b}')
print(f'{y >> 3 = :08b}')
print(f'{z >> 4 = :08b}')


def is_even(n :int) -> bool:
    return (n & 1) == 0


def is_power_of_2(n: int) -> bool:
    return (n & (n-1)) == 0


def twos_complement(n: int) -> int:
    return (~n) + 1


def binary(n: int) -> str:
    if n == 0:
        return '0'
    result: list[str] = []
    while n:
        result.append(str(n & 1))
        # if (n&1) == 1:
        #     result.append('1')
        # else:
        #     result.append('0')

        n >>= 1
        # n = n >> 1
    return ''.join(result[::-1])
    


print(f'{is_even(5) = }')

print(f'{is_power_of_2(8) = }')

print(f'{twos_complement(8) = }')

print(f'{binary(10) =}')



# Value swaping

#Using a temporary var
x = 5
y = 8
print(f'\n{x = }, {y = }')
t = x
x = y
y = t
print(f'{x = }, {y = }')

# using parallel assignment (destructuring)
x = 5
y = 8
print(f'\n{x = }, {y = }')
x, y = y, x
print(f'{x = }, {y = }')


# XOR value swaping
x = 5
y = 8
print(f'\n{x = }, {y = }')
x = x ^ y
y = x ^ y
x = x ^ y
print(f'{x = }, {y = }')
