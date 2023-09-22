
from ordered_set import OrderedSet

x = [3, 7, 10, 28]

# Using iterators
try:
    it = iter(x)
    print(f'{x = }, {it = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
except StopIteration:
    print('Stop')


try: 
    it = iter(x)
    while True:
        print(f'{next(it) = }')
except StopIteration:
    print("Stop")


for elem in x:
    print(f'{elem = }')
else:
    print("Stop")


s = OrderedSet(['one', 'two', 'three', 'four', 'five'])
it2 = iter(s)
print(f'{next(it2) = }')
print(f'{next(it2) = }')


for elem2 in s:
    print(f'{elem2 = }')

