from re import T


# Cria um decorador que permite perpetuar uma alteração de uma instância para outras instâncias:
def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)

        return instances[the_class]

    return get_class


def status_function(the_class):
    def get_status(*args, **kwargs):
        print(f'Alterando a classe "{the_class.__name__}"')

        return the_class(*args, **kwargs)

    return get_status


@singleton
@status_function
class AppSettings:
    def __init__(self):
        self.tema = 'Tema Escuro'


if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()

    as1.tema = 'Tema Claro'  # Ao alterar o tema da instância as1 ela se extende para a instância as2.

    print(as1.tema)
    print(as2.tema)
