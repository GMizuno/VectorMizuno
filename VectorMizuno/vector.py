from math import sqrt
from typing import Union
from typing import List
from typing import Union
import numbers


class Vector:
    '''
    Simple class that works with vectors
    '''

    def __init__(self, vectors: List[Union[int, float]]) -> List[Union[int,
                                                                       float]]:
        '''[summary]

        Args:
            vectors (List[Union[int, float]]): [description]

        Raises:
            TypeError: [description]
            TypeError: [description]

        Returns:
            List[Union[int, float]]: [description]
        '''

        if len(vectors) == 0:
            raise TypeError("You must pass not empty list")

        if not isinstance(vectors, List):
            raise TypeError("You must pass a list")

        if all(isinstance(vec,  numbers.Real) for vec in vectors):
            self.vectors = vectors

        else:
            TypeError('You must pass float or int')

    def __repr__(self) -> str:
        '''Return the vector instance representation.

        Returns:
        str: The representation of the vector instance.
        '''

        return f'Vector({self.vectors})'

    def __str__(self) -> str:
        '''The vector instance as a string.

        Returns:
            str: The vector instance as a string.
        '''

        return f'{self.vectors}'

    def __len__(self) -> numbers.Real:
        '''[summary]

        Returns:
            numbers.Real: [description]
        '''

        return len(self.vectors)

    def __mul__(self, other: Union[Vector, numbers.Real]) -> Vector:
        '''[summary]

        Args:
            other (Vector): [description]

        Returns:
            Vector: [description]
        '''

        if isinstance(other, Vector):
            if len(self.vectors) == len(other.vectors):
                return Vector([self.vectors[i]*other.vectors[i] for i in
                              range(len(other))])

            raise ValueError("Dimensions of {other} and {self} are different")

        if isinstance(other, numbers.Real):
            return Vector([i*other for i in self.vectors])

    def __rmul__(self, other: Union[Vector, numbers.Real]) -> Vector:
        '''[summary]

        Args:
            other (Union[Vector, numbers.Real]): [description]

        Returns:
            Vector: [description]
        '''
        return self.__mul__(other)

    def __add__(self, other: Union[Vector, numbers.Real]) -> Vector:
        '''[summary]

        Args:
            other (Union[Vector, numbers.Real]): [description]

        Returns:
            Vector: [description]
        '''

        if isinstance(other, Vector):
            if len(self.vectors) == len(other.vectors):
                return Vector([self.vectors[i] + other.vectors[i] for i in
                               range(len(other))])
            raise ValueError("Dimensions of {other} and {self} are different")

        if isinstance(other, numbers.Real):
            return Vector([i + other for i in self.vectors])

    def __radd__(self, other: Union[Vector, numbers.Real]) -> Vector:
        '''[summary]

        Args:
            other (Union[Vector, numbers.Real]): [description]

        Returns:
            Vector: [description]
        '''

        return self.__add__(other)


a = Vector([1, 2, 1])
b = Vector([1, 2, 8])

len(a)
len(b)

a*3
3*a
a*b
41*a

a + b 
10 + b 
a + b + 20