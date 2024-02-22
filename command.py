from __future__ import annotations
from abc import ABC, abstractmethod


class Editor:
    text: str
    clipboard: str
    select_start: int
    select_end: int
    cursor: int = 0
    _history: CommandHistory

    def __init__(self, text: str) -> None:
        self.text = text
        self._history = CommandHistory()

    def select_text(self, start: int, end: int) -> None:
        self.select_start = start
        self.select_end = end

    @property
    def selected_text(self):
        return self.text[self.select_start : self.select_end]

    def execute_command(self, command: Command):
        if command.exectute():
            self._history.push(command)

    def undo(self):
        if self._history.is_empty():
            return
        command = self._history.pop()
        if command:
            command.undo()


class Command(ABC):
    def __init__(self, editor: Editor) -> None:
        self.editor = editor

    def backup(self):
        self._backup = self.editor.text

    def undo(self):
        self.editor.text = self._backup

    @abstractmethod
    def exectute(self) -> bool:
        pass


class CopyCommand(Command):
    def __init__(self, editor: Editor) -> None:
        super().__init__(editor)

    def exectute(self) -> bool:
        self.editor.clipboard = self.editor.selected_text
        return False


class PasteCommand(Command):
    def __init__(self, editor: Editor) -> None:
        super().__init__(editor)

    def paste(self) -> str:
        start = self.editor.text[: self.editor.cursor]
        clipboard = self.editor.clipboard
        end = self.editor.text[self.editor.cursor :]
        return start + clipboard + end

    def exectute(self) -> bool:
        if not self.editor.clipboard:
            return False
        self.backup()
        self.editor.text = self.paste()
        return True


class CutCommand(Command):
    def __init__(self, editor: Editor) -> None:
        super().__init__(editor)

    def cut(self) -> str:
        start = self.editor.text[0 : self.editor.select_start]
        end = self.editor.text[self.editor.select_end :]
        return start + end

    def exectute(self) -> bool:
        if not self.editor.selected_text:
            return False
        self.backup()
        self.editor.clipboard = self.editor.selected_text
        self.editor.text = self.cut()
        return True


class CommandHistory:
    _history: list[Command] = []

    def push(self, comamnd: Command):
        self._history.append(comamnd)

    def pop(self) -> Command:
        return self._history.pop()

    def is_empty(self) -> bool:
        return len(self._history) == 0


if __name__ == "__main__":
    editor = Editor("Quick fox jumps over the lazy dog")
    editor.select_text(6, 10)
    print(editor.selected_text)
    editor.execute_command(CopyCommand(editor))
    editor.cursor = 30
    editor.execute_command(PasteCommand(editor))
    print(editor.text)
    editor.undo()
    print(editor.text)
    editor.select_text(10, 16)
    editor.execute_command(CutCommand(editor))
    print(editor.text)
    editor.cursor = 15
    editor.execute_command(PasteCommand(editor))
    print(editor.text)
    editor.undo()
    print(editor.text)
    editor.undo()
    print(editor.text)
