class AppSettings:
    def __init__(self):
        self.tema = 'Tema Escuro'


if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()

    as1.tema = 'Tema Claro'
    print(as1.tema)
    print(as2.tema)