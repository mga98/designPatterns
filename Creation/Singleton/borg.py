"""
Borg ou Monostate é uma variação do Singleton onde é possível garantir
que o estado do objeto seja igual para todas as instâncias.
"""

from __future__ import annotations
from typing import Dict


class StringReprMixin:
    def __str__(self) -> str:
        params = ' / '.join(
            [f'{k}: {v}' for k, v in self.__dict__.items()]
        )

        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class MonoState(StringReprMixin):
    _state: Dict = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state

        return obj

    def __init__(self, nome=None, sobrenome=None) -> None:
        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == '__main__':
    m1 = MonoState(nome='Miguel')
    m2 = MonoState(sobrenome='Almeida')

    print(m1)
    print(m2)
