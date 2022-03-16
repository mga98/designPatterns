"""
Command tem intenção de encapsular uma solicitação como um objeto,
desta forma permitindo parametrizar clientes com diferentes solicitações,
enfileirar ou fazer registro (log) de solicitações e suportar operações
que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca
as solicitações), um ou vários objetos de comando (que fazem a ligação
entre o receiver e a ação a ser executada) e um receiver (o objeto que
vai executar a ação no final).
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


class Light:
    """ Receiver - Luz Inteligente """

    def __init__(self, name: str, room_name: str) -> None:
        self.name: str = name
        self.room_name: str = room_name
        self.color: str = 'Default color'

    def on(self) -> None:
        print(f'{self.name} no {self.room_name} está ligada.')

    def off(self) -> None:
        print(f'{self.name} no {self.room_name} está desligada.')

    def set_color(self, color:str) -> None:
        self.color = color
        print(f'{self.name} no {self.room_name} cor: {self.color}')


class ICommand(ABC):
    """ Interface de comando """

    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    """ Comando concreto """

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightChangeColor(ICommand):
    """ Comando concreto """

    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.set_color(self.color)

    def undo(self) -> None:
        self.light.set_color(self._old_color)


class RemoteController:
    """ Invoker """

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_pressed(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()


if __name__ == '__main__':
    bedroom_light = Light('Luz do quarto', 'Quarto')
    bathroom_light = Light('Luz do banheiro', 'Banheiro')

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'blue')
    bedroom_light_red = LightChangeColor(bedroom_light, 'red')


    remote = RemoteController()
    remote.button_add_command('first_button', bedroom_light_on)
    remote.button_add_command('second_button', bathroom_light_on)
    remote.button_add_command('third_button', bedroom_light_blue)
    remote.button_add_command('fowrth_button', bedroom_light_red)

    remote.button_pressed('first_button')
    remote.button_undo('first_button')
    
    remote.button_pressed('second_button')
    remote.button_undo('second_button')

    remote.button_pressed('third_button')
    remote.button_undo('third_button')
    
    remote.button_pressed('fowrth_button')
    remote.button_undo('fowrth_button')
