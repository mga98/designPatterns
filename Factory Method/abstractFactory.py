from abc import ABC, abstractmethod


class VeiculoPopular(ABC):
    @abstractmethod
    def buscarCliente(self) -> None: pass


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscarCliente(self) -> None: pass


class CarroLuxoZN(VeiculoLuxo):
    def buscarCliente(self) -> None:
        print('Carro de luxo ZN está buscando cliente...')


class CarroLuxoZS(VeiculoLuxo):
    def buscarCliente(self) -> None:
        print('Carro de luxo ZS está buscando cliente...')


class CarroPopularZN(VeiculoPopular):
    def buscarCliente(self) -> None:
        print('Carro popular ZN está buscando o cliente...')


class CarroPopularZS(VeiculoPopular):
    def buscarCliente(self) -> None:
        print('Carro popular ZS está buscando o cliente...')


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
    
    print('-' * 50)
