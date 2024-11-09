from decimal import Decimal
from typing import Optional


class Fact:
    # left = factor * right
    def __init__(self, left: "Node", factor: Decimal, right: "Node") -> None:
        self.left = left
        self.factor = factor
        self.right = right
        self.apply()

    def apply(self):
        fact_added_to_any_graph = False
        fact_added_to_graph = False

        if graph_roots:
            for node in graph_roots:
                for a, b in [(self.left, self.right), (self.right, self.left)]:
                    if fact_added_to_graph:
                        break

                    if node.dfs(a):
                        a.children.append(b)
                        b.parent = a
                        b.weight = self.factor
                        fact_added_to_graph = True

                    if fact_added_to_graph:
                        fact_added_to_any_graph |= True

        if not fact_added_to_any_graph:
            graph_roots.append(self.left)
            self.left.children.append(self.right)
            self.right.parent = self.left
            self.right.weight = self.factor

    def __repr__(self) -> str:
        return f"{self.left} = {self.factor} * {self.right}"


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: list["Node"] = []
        self.parent: Optional["Node"] = None
        self.weight = 1

    def dfs(self, find: "Node"):
        if self == find:
            return True
        for child in self.children:
            if child.dfs(find):
                return True
        return False

    def factor(self, node: "Node"):
        assert node.parent, f"{node} is not a child of any node"
        assert self.dfs(node), f"{node} is not a parent of {self}"

        value = node.weight

        while node.parent:
            node = node.parent
            value *= node.weight

        # assert node == self, f"{self} is not a parent of {node}"

        return value

    def __repr__(self) -> str:
        return self.name

    def render(self, depth: int = 0):
        for child in self.children:
            print("  " * depth, end="")
            print(f"{self} = {self.weight} * {child}")
            child.render(depth=depth + 1)


if __name__ == "__main__":
    global graph_roots, x

    graph_roots: list["Node"] = []
    x = Node("x")

    millimeter = Node("millimeter")
    centimeter = Node("centimeter")
    meter = Node("meter")
    foot = Node("foot")
    inch = Node("inch")
    hour = Node("hour")
    minute = Node("minute")

    rule_sets = [
        Fact(meter, Decimal("3.28084"), foot),
        Fact(millimeter, Decimal("0.001"), meter),
        Fact(centimeter, Decimal("10"), millimeter),
        Fact(foot, Decimal("12"), inch),
        Fact(hour, Decimal("60"), minute),
    ]

    "2 * meter = x * inch"
    print(2 * meter.factor(inch))

    # meter in millimeter
    print(meter.factor(millimeter))

    print(hour.factor(meter))
