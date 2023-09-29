# ----------------------------------------------------------
# Lab #3: Combinatorics
# Permutations and combinations with repetitions.
#
# Date: 29-Sep-2022
# Authors:
#           
#           A01748227 Diego Zurita Villarreal
#           A01747363 Julián Cisneros Cortés
#           
# ----------------------------------------------------------

from comparable import C


def power_set(s: list[C]) -> list[list[C]]:
    if s:
        # Recursion Call
        r = power_set(s[0:-1])
        # Getting the last element and concatenating it,
        # to each element of the previous power set.
        return r + [t + [s[-1]] for t in r]
    else:
        # If the list is empty
        # Base case:
        return [s]


def sorted_nicely(s: list[list[C]]) -> list[list[C]]:
    # A private function that returns a tuple with (len(Each set), Each set)
    def size_and_content(t: list[C]) -> tuple[int, list[C]]:
        return (len(t), t)
    # Return the sorted list of lists, with a criteria of len first
    # and then the alphabetical oreder of the elems in the list
    return sorted(s, key=size_and_content)

# We use the power set, but only get the lists that are os size k.


def combinations(s: list[C], k: int) -> list[list[C]]:
    return [t for t in power_set(s) if len(t) == k]


def insert(x: C, s: list[C], i: int) -> list[C]:
    return s[:i] + [x] + s[i:]


def insert_everywhere(x: C, s: list[C]) -> list[list[C]]:
    return [insert(x, s, i) for i in range(len(s) + 1)]


def permute(s: list[C]) -> list[list[C]]:
    if s:
        return sum([insert_everywhere(s[0], t)
                    for t in permute(s[1:])], [])
    else:
        return [s]


def permutations(s: list[C], k: int) -> list[list[C]]:
    return sum([permute(t) for t in combinations(s, k)], [])


def permutations_with_repetition(s: list[C], k: int) -> list[list[C]]:
    if k == 0:
        return []

    def recursion(s: list[C], k: int) -> list[list[C]]:

        if k == 0:
            return [[]]

        v = s
        w = recursion(s, k - 1)
        z = []

        for elem in w:
            for i in v:
                z.append(elem + [i])

        return z
    return recursion(s, k)


def combinations_with_repetition(s: list[C], k: int) -> list[list[C]]:
    permutaciones = permutations_with_repetition(s, k)
    lista = []

    for valor in permutaciones:
        if sorted(valor) not in lista:
            lista.append(valor)

    return lista


if __name__ == '__main__':
    from pprint import pprint
    # pprint(power_set([]))
    # pprint(power_set(['x']))
    # pprint(power_set(['x', 'y']))
    # pprint(power_set(['x', 'y', 'z']))
    # pprint(sorted_nicely(power_set(['x', 'y', 'z', 'w'])))
    # pprint(sorted_nicely(combinations(['a', 'b', 'c', 'd'], 0)))
    # pprint(sorted_nicely(combinations(['a', 'b', 'c', 'd'], 1)))
    # pprint(sorted_nicely(combinations(['a', 'b', 'c', 'd'], 2)))
    # pprint(sorted_nicely(combinations(['a', 'b', 'c', 'd'], 3)))
    # pprint(sorted_nicely(combinations(['a', 'b', 'c', 'd'], 4)))
    # Cannot create groups of 5, because the list has only 4 elems
    # pprint(sorted_nicely(combinations(['a', 'b', 'c', 'd'], 5)))
    # pprint(insert('x', ['y', 'z'], 0))
    # pprint(insert('x', ['y', 'z'], 1))
    # pprint(insert('x', ['y', 'z'], 2))
    # pprint(insert_everywhere('x', ['y', 'z']))
    # pprint(sorted_nicely(permute(['x', 'y', 'z'])))
    # pprint(sorted_nicely(permutations([0, 1], 4)))
    # pprint(sorted_nicely(permutations_with_repetition(['w', 'x', 'y', 'z'],
    #  3)))
    # pprint(len(permutations_with_repetition(range(3), 6)))
    # pprint(len(permutations_with_repetition(range(10), 4))
    pprint(sorted_nicely(permutations_with_repetition([0, 1], 4)))
    pprint(sorted_nicely(combinations_with_repetition([0, 1], 4)))
    pprint(sorted_nicely(combinations_with_repetition([1, 2, 3, 4], 0)))
    pprint(sorted_nicely(combinations_with_repetition([], 5)))