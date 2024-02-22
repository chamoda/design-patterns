class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1 operation1"

    def operation2(self) -> str:
        return "Subsystem1 operation2"


class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2 operation1"

    def operation2(self) -> str:
        return "Subsystem2 operation2"


class Facade:
    def operation(self) -> str:
        subsystem1 = Subsystem1()
        subsystem2 = Subsystem2()

        results: list[str] = []
        results.append(subsystem1.operation1())
        results.append(subsystem1.operation2())
        results.append(subsystem2.operation1())
        results.append(subsystem2.operation2())

        return "\n".join(results)


if __name__ == "__main__":
    facade = Facade()
    print(facade.operation())
