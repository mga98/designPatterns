"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.
Princípio: programe para interfaces, não para implementações
"""


from abc import ABC, abstractmethod


class VeiculoPopular(ABC):
    @abstractmethod
    def buscarCliente(self) -> None: pass


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscarCliente(self) -> None: pass


### Carros de luxo ####


class CarroLuxoZL(VeiculoLuxo):
    def buscarCliente(self) -> None:
        print('Carro de luxo ZL está buscando cliente...')


class CarroLuxoZN(VeiculoLuxo):
    def buscarCliente(self) -> None:
        print('Carro de luxo ZN está buscando cliente...')


class CarroLuxoZS(VeiculoLuxo):
    def buscarCliente(self) -> None:
        print('Carro de luxo ZS está buscando cliente...')


### Carros populares ###


class CarroPopularZL(VeiculoPopular):
    def buscarCliente(self) -> None:
        print('Carro popular ZL está buscando o cliente...')


class CarroPopularZN(VeiculoPopular):
    def buscarCliente(self) -> None:
        print('Carro popular ZN está buscando o cliente...')


class CarroPopularZS(VeiculoPopular):
    def buscarCliente(self) -> None:
        print('Carro popular ZS está buscando o cliente...')


### Motos ###


class MotoZL(VeiculoPopular):
    def buscarCliente(self) -> None:
        print('Moto ZL está buscando o cliente...')


class MotoZN(VeiculoPopular):
    def buscarCliente(self) -> None:
        print('Moto ZN está buscando o cliente...')


class MotoZS(VeiculoPopular):
    def buscarCliente(self) -> None:
        print('Moto ZS está buscando o cliente...')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass

    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_moto() -> VeiculoPopular: pass


class ZonaNorteFactory(VeiculoFactory):
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_moto() -> VeiculoPopular:
        return MotoZN()


class ZonaSulFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto() -> VeiculoPopular:
        return MotoZS()


class ZonaLesteFacotry(VeiculoFactory):
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZL()
    
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroPopularZL()
    
    @staticmethod
    def get_moto() -> VeiculoPopular:
        return MotoZL


class Cliente:
    def app_zonaNorte(self) -> None:
        appNorte = ZonaNorteFactory()

        carro_luxo = appNorte.get_carro_luxo()
        carro_luxo.buscarCliente()

        carro_popular = appNorte.get_carro_popular()
        carro_popular.buscarCliente()

        moto = appNorte.get_moto()
        moto.buscarCliente()

    def app_zonaSul(self) -> None:
        appSul = ZonaSulFactory()

        carro_popular = appSul.get_carro_popular()
        carro_popular.buscarCliente()

        moto = appSul.get_moto()
        moto.buscarCliente()

    def app_zonaLeste(self) -> None:
        appLeste = ZonaLesteFacotry()

        carro_popular = appLeste.get_carro_popular()
        carro_popular.buscarCliente()


if __name__ == '__main__':
    cliente = Cliente()
    
    print('=' * 50)
    
    titulo = 'ZONA SUL'
    print(titulo.center(50))
    print('=' * 50)
    cliente.app_zonaSul()
    
    print('=' * 50)
    
    titulo2 = 'ZONA NORTE'
    print(titulo2.center(50))
    print('=' * 50)
    cliente.app_zonaNorte()
    
    print('=' * 50)

    titulo3 = 'ZONA LESTE'
    print(titulo3.center(50))
    print('=' * 50)
    cliente.app_zonaLeste()

    print('=' * 50)
