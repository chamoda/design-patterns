from __future__ import annotations
from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: Component, event: str):
        pass


class Component:
    def __init__(self, dialog: Mediator) -> None:
        self._dialog = dialog

    def click(self):
        self._dialog.notify(self, "click")


class Button(Component):
    pass


class Dialog(Mediator):
    ok_button: Button
    cancel_button: Button

    def __init__(self) -> None:
        self.ok_button = Button(self)
        self.cancel_button = Button(self)

    def notify(self, sender: Component, event: str):
        if sender == self.ok_button and event == "click":
            print("Ok button clicked")
        if sender == self.cancel_button and event == "click":
            print("Cancel button clicked")


if __name__ == "__main__":
    dialog = Dialog()
    dialog.ok_button.click()
    dialog.cancel_button.click()
