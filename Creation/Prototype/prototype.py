"""
Especifica os tipos de objetos a serem criados e permite
criar uma cópia dos mesmos que podem ser alteradas sem afetar
sua fonte.
"""

from __future__ import annotations
from typing import List
from copy import deepcopy


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == '__main__':
    miguel = Person('Miguel', 'Almeida')
    address_miguel = Address('13 de Maio', '860')
    miguel.add_address(address_miguel)

    jose = miguel.clone()
    jose.firstname = 'José'

    print(miguel)
    print(jose)
