class Target:
    def request(self) -> str:
        return "Target: Default behaviour"


class Adaptee:
    def spacific_request(self) -> str:
        return "ruoivaheb cificepS"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Target: {self.spacific_request()[::-1]}"


def client(target: Target):
    print(target.request())


if __name__ == "__main__":
    target = Target()
    client(target)

    adapter = Adapter()
    client(adapter)
