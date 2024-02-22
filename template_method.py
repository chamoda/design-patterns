from abc import ABC, abstractmethod


class Network(ABC):
    username: str
    password: str

    def post(self, message: str) -> bool:
        if self.login(self.username, self.password):
            result = self.send_data(message)
            self.logout()
            return result
        return False

    @abstractmethod
    def login(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def send_data(self, data: str) -> bool:
        pass

    @abstractmethod
    def logout(self) -> None:
        pass


class Facebook(Network):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def login(self, username: str, password: str) -> bool:
        print(f"Login with to Facebook {username} {password}")
        return True

    def send_data(self, data: str) -> bool:
        print(f"Send {data} to Facebook")
        return True

    def logout(self):
        print("Logout Facebook")


class Twitter(Network):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def login(self, username: str, password: str) -> bool:
        print(f"Login with to Twitter {username} {password}")
        return True

    def send_data(self, data: str) -> bool:
        print(f"Send {data} to Twitter")
        return True

    def logout(self):
        print("Logout Twitter")


if __name__ == "__main__":
    facebook = Facebook("email", "password")
    facebook.post("Test post1")
    twiter = Twitter("email", "password")
    twiter.post("Test post2")
