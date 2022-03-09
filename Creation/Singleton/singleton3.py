"""
Utilizando o Singleton como uma MetaClasse.
"""

class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'Tema escuro.'


if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()

    as1.tema = 'Tema claro'
    
    print(as1.tema)
    print(as2.tema)
