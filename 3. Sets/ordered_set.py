
from __future__ import annotations
from typing import Generic, TypeVar, cast
from _collections_abc import Iterable, Iterator

T = TypeVar('T')
N = TypeVar('N')
I = TypeVar('I')

class OrderedSet(Generic[T]):
    
    class __Node(Generic[N]):
        info: N | None
        next: OrderedSet.__Node[N]
        prev: OrderedSet.__Node[N]

        def __init__(self, value: N | None = None) -> None:    #Self refers to the same class
            self.info = value
            self.next = self
            self.prev = self


    class __Iterator(Generic[I]):
        
        __sentinel: OrderedSet.__Node[I]
        __current: OrderedSet.__Node[I]

        #Complexity: O(1)
        def __init__(self, sentinel: OrderedSet.__Node[I]) -> None:
            self.__sentinel = sentinel
            self.__current = self.__sentinel.next

        #Complexity: O(1)
        def __iter__(self) -> Iterator[I]:
            return self

        #Complexity: O(1)
        def __next__(self) -> I:
            if self.__sentinel == self.__current:
                raise StopIteration
            result = cast(I, self.__current.info)
            self.__current = self.__current.next
            return result            


    
    __sentinel: OrderedSet.__Node[T]
    __count: int

     # Complexity: O(N^2)
    def __init__(self, values: Iterable[T] = []) -> None:
        self.__sentinel = OrderedSet.__Node()
        self.__count = 0
        for elem in values:
            self.add(elem)

    
    # Complexity: O(n)
    def add(self, value: T) -> None:
        if value in self:
            print(f'Ya existe el valor: {value}')
            return 
        self.__count += 1
        new_node = OrderedSet.__Node(value)
        new_node.next = self.__sentinel
        new_node.prev = self.__sentinel.prev
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity: O(n)
    def __repr__(self) -> str:
        #result: list[T] = []
        #current = self.__sentinel.next
        #while current != self.__sentinel:
        #    if current.info is not None: 
        #        result.append(current.info)
        #    current = current.next
        if self:
            return f'OrderedSet({list(self)})'
        return 'OrderedSet()'
    
    def __contains__(self, value: T) -> bool:
        #current = self.__sentinel.next
        #while current != self.__sentinel:
        #    if current.info == value:
        #        return True
        #    current = current.next
        #return False
        for elem in self:
            if elem == value:
                return True
        return False

    
    #Complexity: O(1)
    def __len__(self) -> int:
        return self.__count

    #Complexity: O(1)
    def __iter__(self) -> Iterator[T]:
        return OrderedSet.__Iterator(self.__sentinel)
    
    #Complexity: O(n)
    def discard(self, value: T) -> None:
        current = self.__sentinel.next
        while current != self.__sentinel:
            if current.info == value:
                current.next.prev = current.prev
                current.prev.next = current.next
                self.__count -= 1
                return
            current = current.next

    #Complexity: O(n)
    def remove(self, value: T) -> None:
        if value in self:
            self.discard(value)
        else:
            raise KeyError
        
    #Complexity: O(n^2), n = len(self), n = len(other)
    def __eq__(self, other: object) -> bool:
        if isinstance(other, OrderedSet) and len(self) == len(other):
            for elem in self:
                if elem not in other:
                    return False
            return True
        else:
            return False
        

    #Complexity: O(n^2), n = len(self), n = len(other)
    def __le__(self, other: OrderedSet[T]) -> bool:
        if len(self) <= len(other):
            for elem in self:
                if elem not in other:
                    return False
            return True
        else:
            return False
        
    #Complexity: O(n^2), n = len(self), n = len(other)
    def __lt__(self, other: OrderedSet[T]) -> bool:
        if len(self) < len(other):
            for elem in self:
                if elem not in other:
                    return False
            return True
        else:
            return False
        
    #Complexity: O(n^2), n = len(self), n = len(other)
    def __ge__(self, other: OrderedSet[T]) -> bool:
        if len(self) >= len(other):
            for elem in self:
                if elem not in other:
                    return False
            return True
        else:
            return False
        

    #Complexity: O(n^2), n = len(self), n = len(other)
    def __gt__(self, other: OrderedSet[T]) -> bool:
        if len(self) > len(other):
            for elem in other:
                if elem not in self:
                    return False
            return True
        else:
            return False
        

    #Complexity: O(n^2), n = len(self), n = len(other)
    def isdisjoint(self, other: OrderedSet[T]) -> bool:
        for elem in self:
            if elem in other:
                return False
        return True


    #Complexity: O(n * m * j), n = len(self), m = len(other), j = len(result)
    def __and__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem in other:
                result.add(elem)
        return result
    

    #Complexity: O(n^2 + m^2), n = len(self), m = len(other)
    def __or__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
                result.add(elem)
        for elem in other:
            result.add(elem)
        return result
    

    #Complexity: O(n * m * j), n = len(self), m = len(other), j = len(result)
    def __sub__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem not in other:
                result.add(elem)
        return result
    

    #Complexity: O(n*m*j + n*m*j), n = len(self), m = len(other), j = len(result)
    def __xor__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem not in other:
                result.add(elem)
        for elem in other:
            if elem not in self:
                result.add(elem)
        return result
    

    #Complexity: O(n^2), n = len(self)
    def clear(self) -> None:
        for elem in self:
            self.remove(elem)
        return self
    

    #Complexity: O(n), n = len(self)
    def pop(self) -> T:
        if len(self) == 0:
            raise KeyError
        else:
            last = self.__sentinel.prev.info
            self.remove(last)
            return last
    

if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet([16,28,15])
    print(a)
    print(f'{hash(a) = :x}')
    print(f'{a is None = }')
    print(f'{a == a = }')
    print(f'{repr(a) = }')
    a.add(4)
    a.add(8)
    a.add(15)
    a.add(4)
    print(a)
    print(f'Elementos en la lista: {len(a)}')
    a.add(7)
    print(a)
    print(f'Elementos en la lista: {len(a)}')
    b: OrderedSet[str] = OrderedSet()
    print(f'{b = }')
    b.add('hello')
    b.add('bye')
    c = OrderedSet(b)
    c.add('Hi')

    print(f'{b = }')
    print(f'{c = }')

    d = OrderedSet('hello world')
    print(f'{d = }')

    e = OrderedSet((5,6,7,8))
    print(f'{e = }')

    f = OrderedSet({'uno': 'one', 'dos': 'two', 'tres': 'three'}.items())
    print(f'{f = }')

    print(a)
    a.remove(16)
    print(a)

    print(f'{a == a = }')