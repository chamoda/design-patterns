from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self):
        pass


class MacButton(Button):
    def render(self):
        print("Mac button")

    def on_click(self):
        print("Mac button clicked")


class WebButton(Button):
    def render(self):
        print("Web button")

    def on_click(self):
        print("Web button clicked")


class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self):
        button = self.create_button()
        button.render()


class MacDialog(Dialog):
    def create_button(self) -> Button:
        return MacButton()


class WebDialog(Dialog):
    def create_button(self) -> Button:
        return WebButton()


if __name__ == "__main__":
    web_dialog = WebDialog()
    web_dialog.render()
