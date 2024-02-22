from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WinButton(Button):
    def render(self) -> None:
        print("Rendering win button")


class WinCheckbox(Checkbox):
    def render(self) -> None:
        print("Rendering win checkbox")


class MacButton(Button):
    def render(self) -> None:
        print("Rendering mac button")


class MacCheckbox(Checkbox):
    def render(self) -> None:
        print("Rendering mac checkbox")


class WinGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class MacGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class Application:
    __factory: GUIFactory
    __button: Button
    __checkbox: Checkbox

    def __init__(self, factory: GUIFactory) -> None:
        self.__factory = factory

    def create_ui(self) -> None:
        self.__button = self.__factory.create_button()
        self.__checkbox = self.__factory.create_checkbox()

    def render(self) -> None:
        self.__button.render()
        self.__checkbox.render()


if __name__ == "__main__":
    factory = MacGUIFactory()
    application = Application(factory)
    application.create_ui()
    application.render()
