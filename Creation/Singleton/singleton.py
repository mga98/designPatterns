"""
O padrão de criação Singleton garante que uma classe tenha apenas uma 
instância e que esta instância possa ser referenciada globalmente.
"""


class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self):
        self.tema = 'Tema Escuro'


if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()

    as1.tema = 'Tema Claro'
    print(as1.tema)
    print(as2.tema)