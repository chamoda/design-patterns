from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    player: Player

    def __init__(self, player: Player) -> None:
        self.player = player

    @abstractmethod
    def on_lock(self) -> str:
        pass

    @abstractmethod
    def on_play(self) -> str:
        pass

    @abstractmethod
    def on_next(self) -> str:
        pass

    @abstractmethod
    def on_previous(self) -> str:
        pass


class LockedState(State):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def on_lock(self) -> str:
        if self.player.is_playing():
            self.player.change_state(ReadyState(self.player))
            return "Stop playing"
        else:
            return "Locked"

    def on_play(self) -> str:
        self.player.change_state(ReadyState(self.player))
        return "Ready"

    def on_next(self) -> str:
        return "Locked"

    def on_previous(self) -> str:
        return "Locked"


class ReadyState(State):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def on_lock(self) -> str:
        self.player.change_state(LockedState(self.player))
        return "Locked"

    def on_play(self) -> str:
        action = self.player.start_playback()
        self.player.change_state(PlayingState(self.player))
        return action

    def on_next(self) -> str:
        return "Locked"

    def on_previous(self) -> str:
        return "Locked"


class PlayingState(State):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def on_lock(self) -> str:
        self.player.change_state(LockedState(self.player))
        self.player.reset_current_track()
        return "Stop playing"

    def on_play(self) -> str:
        self.player.change_state(ReadyState(self.player))
        return "Paused"

    def on_next(self) -> str:
        return self.player.next_track()

    def on_previous(self) -> str:
        return self.player.previous_track()


class Player:
    _state: State
    _playing: bool = False
    _playlist: list[str] = []
    _current_track: int = 0

    def __init__(self) -> None:
        self._state = ReadyState(self)
        for i in range(1, 5):
            self._playlist.append(f"Track {i}")

    def change_state(self, state: State):
        self._state = state

    @property
    def state(self) -> State:
        return self._state

    def set_playing(self, playing: bool):
        self._playing = playing

    def is_playing(self) -> bool:
        return self._playing

    def start_playback(self) -> str:
        return f"Playing {self._playlist[self._current_track]}"

    def next_track(self) -> str:
        self._current_track += 1
        if self._current_track > len(self._playlist) - 1:
            self._current_track = 0
        return f"Playing {self._playlist[self._current_track]}"

    def previous_track(self) -> str:
        self._current_track -= 1
        if self._current_track < 0:
            self._current_track = len(self._playlist) - 1
        return f"Playing {self._playlist[self._current_track]}"

    def reset_current_track(self):
        self._current_track = 0


if __name__ == "__main__":
    player = Player()
    print(player.state.on_play())
    print(player.state.on_next())
    print(player.state.on_previous())
    print(player.state.on_lock())
    print(player.state.on_play())
    print(player.state.on_play())
