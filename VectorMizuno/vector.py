from __future__ import annotations

from math import sqrt
from typing import Union
from typing import List
from typing import Union
import numbers


class Vectors:
    '''
    Simple class that works with vectors
    '''

    def __init__(self, vectors: List[Union[int, float]]) -> None:
        '''[summary]

        Args:
            vectors (List[Union[int, float]]): [description]

        Raises:
            TypeError: [description]
            TypeError: [description]
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

    def __mul__(self, other: Union[Vectors, numbers.Real]) -> Vectors:
        '''[summary]

        Args:
            other (Vectors): [description]

        Returns:
            Vectors: [description]
        '''

        if isinstance(other, Vectors):
            if len(self.vectors) == len(other.vectors):
                return Vectors([self.vectors[i]*other.vectors[i] for i in
                                range(len(other))])

            raise ValueError("Dimensions of {other} and {self} are different")

        if isinstance(other, numbers.Real):
            return Vectors([i*other for i in self.vectors])

    def __rmul__(self, other: Union[Vectors, numbers.Real]) -> Vectors:
        '''[summary]

        Args:
            other (Union[Vectors, numbers.Real]): [description]

        Returns:
            Vectors: [description]
        '''
        return self.__mul__(other)

    def __add__(self, other: Union[Vectors, numbers.Real]) -> Vectors:
        '''[summary]

        Args:
            other (Union[Vectors, numbers.Real]): [description]

        Returns:
            Vectors: [description]
        '''

        if isinstance(other, Vectors):
            if len(self.vectors) == len(other.vectors):
                return Vectors([self.vectors[i] + other.vectors[i] for i in
                               range(len(other))])
            raise ValueError("Dimensions of {other} and {self} are different")

        if isinstance(other, numbers.Real):
            return Vectors([i + other for i in self.vectors])

    def __radd__(self, other: Union[Vectors, numbers.Real]) -> Vectors:
        '''[summsary]

        Args:
            other (Union[Vectors, numbers.Real]): [description]

        Returns:
            Vectorss: [description]
        '''

        return self.__add__(other)

    def __eq__(self, other: Union[Vectors, numbers.Real]) -> bool:
        '''[summary]

        Args:
            other (Union[Vectors, numbers.Real]): [description]

        Returns:
            bool: [description]
        '''
        if isinstance(other, Vectors):
            if len(other) == len(self) and self.vectors == other.vectors:
                return True
            else:
                return False
        else:
            return False
