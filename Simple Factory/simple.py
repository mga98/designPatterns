from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    @abstractmethod
    def buscarCliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscarCliente(self) -> None:
        print('Carro de luxo está buscando cliente...')


class CarroPopular(Veiculo):
    def buscarCliente(self) -> None:
        print('Carro popular está buscando o cliente...')


class Moto(Veiculo):
    def buscarCliente(self) -> None:
        print('Moto está buscando o cliente...')


class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()

        if tipo == 'popular':
            return CarroPopular()

        if tipo == 'moto':
            return Moto()

        assert 0, 'Veículo não existe.'


if __name__ == '__main__':
    carrosDisponiveis = ['luxo', 'popular', 'moto']

    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carrosDisponiveis))
        carro.buscarCliente()
