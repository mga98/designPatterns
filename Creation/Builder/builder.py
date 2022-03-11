"""
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos
(method chaining).
"""


from abc import ABC, abstractclassmethod, abstractmethod
from mailbox import NotEmptyError
from typing import List


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixin):
    def __init__(self) -> None:
        self.name = None
        self.lastname = None
        self.age = None


class IUserBuild(ABC):
    @property
    @abstractmethod
    def result(self) -> User: pass

    @abstractmethod
    def add_firstname(self, firstname): pass

    @abstractmethod
    def add_lastname(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass


class UserBuilder(IUserBuild):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._result = User()

    @property
    def result(self) -> User:
        return_data = self._result
        self.reset
        return return_data

    def add_firstname(self, firstname):
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname):
        self._result.lastname = lastname
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    
class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        self._builder = builder

    def with_age(self, firstname, lastname, age) -> User:
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(age)

        return self._builder.result

    def with_name(self, firstname, lastname, age) -> User:
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(age)
        
        return self._builder.result

if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)

    user1 = user_director.with_age('Miguel', 'Almeida', 23)
    user2 = user_director.with_name('Luiz', 'Otávio', 30)

    print(user1)
    print(user2)
