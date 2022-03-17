"""
Template Method (comportamental), tem a intenção de definir um algoritmo de um método,
postergando alguns passos para as subclasses por herança. Template method permite que
subclasses redefinam certos passos de um algorítimo sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle.) 
"""

from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Classe abstrata """

    def prepare(self) -> None:
        """ Template method """
        print()  # Quebra de linha
        self.hook_before_add_ingredientes()  # Hook
        self.add_ingredientes()  # Abstract
        self.cook()  # Abstract
        self.hook_after_cook()  # Hook
        self.cut()  # Concrete
        self.serve()  # Concrete

    def hook_before_add_ingredientes(self) -> None: pass

    def hook_after_cook(self) -> None: pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando a pizza...')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Servindo a pizza...')

    @abstractmethod
    def add_ingredientes(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class Calabresa(Pizza):
    def hook_after_cook(self) -> None:
        print(f'Deixar a pizza de {self.__class__.__name__} descansar por 5 minutos.')

    def add_ingredientes(self) -> None:
        print(f'Ingredientes {self.__class__.__name__}: queijo, calabresa, orégano.')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: 45 minutos no forno a lenha.')


class Margherita(Pizza):
    def hook_before_add_ingredientes(self) -> None:
        print(f'Lavando os ingredientes de {self.__class__.__name__}')

    def add_ingredientes(self) -> None:
        print(f'Ingredientes {self.__class__.__name__}: mussarela, orégano, tomate.')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: 40 minutos no forno a lenha.')


if __name__ == '__main__':
    calabresa = Calabresa()
    calabresa.prepare()

    margherita = Margherita()
    margherita.prepare()

    print()
