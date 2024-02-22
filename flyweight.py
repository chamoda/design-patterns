from random import randint
from typing import Dict, List


class TreeType:
    def __init__(self, name: str, color: str) -> None:
        self._name = name
        self._color = color

    def draw(self):
        print(f"{self._color} {self._name}")


class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType) -> None:
        self._x = x
        self._y = y
        self._tree_type = tree_type

    def draw(self):
        self._tree_type.draw()


class TreeFactory:
    _tree_types: Dict[str, TreeType] = {}

    @staticmethod
    def get_tree_type(name: str, color: str) -> TreeType:
        key = f"{name}.{color}"
        if tree_type := TreeFactory._tree_types.get(key):
            return tree_type
        else:
            tree_type = TreeType(name, color)
            TreeFactory._tree_types[key] = tree_type
            return tree_type

    @staticmethod
    def list_tree_types():
        print(TreeFactory._tree_types)


class Forest:
    _trees: List[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str) -> None:
        tree_type = TreeFactory.get_tree_type(name, color)
        tree = Tree(x, y, tree_type)
        self._trees.append(tree)

    def draw(self):
        for tree in self._trees:
            tree.draw()


if __name__ == "__main__":
    forest = Forest()
    for _ in range(1, 100):
        forest.plant_tree(randint(1, 100), randint(1, 100), "Plam", "Green")
        forest.plant_tree(randint(1, 100), randint(1, 100), "Plam", "Yellow")
        forest.plant_tree(randint(1, 100), randint(1, 100), "Plam", "Brown")
        forest.plant_tree(randint(1, 100), randint(1, 100), "Oak", "Green")
        forest.plant_tree(randint(1, 100), randint(1, 100), "Oak", "Yellow")
        forest.plant_tree(randint(1, 100), randint(1, 100), "Oak", "Brown")
    TreeFactory.list_tree_types()
