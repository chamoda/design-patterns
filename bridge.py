from abc import ABC, abstractmethod


class Device(ABC):
    is_enabled: bool

    @abstractmethod
    def enable(self) -> None:
        ...

    @abstractmethod
    def disable(self) -> None:
        ...

    @abstractmethod
    def status(self) -> str:
        ...


class Remote(ABC):
    @abstractmethod
    def power(self) -> None:
        ...


class Radio(Device):
    def __init__(self) -> None:
        self.is_enabled = False

    def enable(self) -> None:
        self.is_enabled = True

    def disable(self) -> None:
        self.is_enabled = False

    def status(self) -> str:
        return f"Status: {'On' if self.is_enabled else 'Off'}"


class BasicRemote(Remote):
    _device: Device

    def __init__(self, device: Device) -> None:
        self._device = device

    def power(self) -> None:
        if self._device.is_enabled:
            self._device.disable()
        else:
            self._device.enable()


if __name__ == "__main__":
    radio = Radio()
    radioRemote = BasicRemote(radio)
    radioRemote.power()
    print(radio.status())
