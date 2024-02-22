from __future__ import annotations


class Editor:
    text: str
    _cur_x: int
    _cur_y: int

    def __init__(self) -> None:
        self.text = ""
        self._cur_x = 0
        self._cur_y = 0

    def set_text(self, text: str):
        self.text = text

    def set_cursor(self, x: int, y: int):
        self._cur_x = x
        self._cur_y = y

    def create_snapshot(self) -> Snapshot:
        return Snapshot(self, self.text, self._cur_x, self._cur_y)


class Snapshot:
    _editor: Editor
    _text: str
    _cur_x: int
    _cur_y: int

    def __init__(self, editor: Editor, text: str, cur_x: int, cur_y: int) -> None:
        self._editor = editor
        self._text = text
        self._cur_x = cur_x
        self._cur_y = cur_y

    def restore(self):
        self._editor.set_text(self._text)
        self._editor.set_cursor(self._cur_x, self._cur_y)


if __name__ == "__main__":
    editor = Editor()
    editor.set_text("Hello")
    editor.set_cursor(0, 1)
    print(editor.text)
    snapshot1 = editor.create_snapshot()
    editor.set_text("Hello World")
    print(editor.text)
    editor.set_cursor(0, 2)
    snapshot2 = editor.create_snapshot()
    snapshot1.restore()
    print(editor.text)
