import zlib
from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def write_data(self, data: bytes) -> None:
        pass

    @abstractmethod
    def read_data(self) -> bytes:
        pass


class DataSourceDecorator(DataSource):
    def __init__(self, source: DataSource) -> None:
        self._wrappee = source

    def write_data(self, data: bytes) -> None:
        self._wrappee.write_data(data)

    def read_data(self) -> bytes:
        return self._wrappee.read_data()


class FileDataSource(DataSource):
    def __init__(self, name: str) -> None:
        self._name = name

    def write_data(self, data: bytes) -> None:
        with open(self._name, "wb") as f:
            f.write(data)

    def read_data(self) -> bytes:
        with open(self._name, "rb") as f:
            return f.read()


class EncryptionDecorator(DataSourceDecorator):
    def __init__(self, source: DataSource) -> None:
        super().__init__(source)

    def encrypt(self, data: bytes) -> bytes:
        return data[::-1]

    def decrypt(self, data: bytes) -> bytes:
        return data[::-1]

    def write_data(self, data: bytes) -> None:
        super().write_data(self.encrypt(data))

    def read_data(self) -> bytes:
        return self.decrypt(super().read_data())


class CompressionDecorator(DataSourceDecorator):
    def __init__(self, source: DataSource) -> None:
        super().__init__(source)

    def compress(self, data: bytes) -> bytes:
        return zlib.compress(data)

    def decompress(self, data: bytes) -> bytes:
        return zlib.decompress(data)

    def write_data(self, data: bytes) -> None:
        super().write_data(self.compress(data))

    def read_data(self) -> bytes:
        return self.decompress(super().read_data())


if __name__ == "__main__":
    source: DataSourceDecorator = CompressionDecorator(
        EncryptionDecorator(FileDataSource("data/data.txt"))
    )
    source.write_data(b"test data")
    print(source.read_data())
