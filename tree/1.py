from typing import List


class Node:
    def __init__(self, name: int):
        self.name = name
        self.is_root = True
        self.children: List[Node] = []

a = Node()
b = Node()
c = Node()
d = Node()
e = Node()
f = Node()
g = Node()
h = Node()
i = Node()
j = Node()
k = Node()

a.children = [b,c,d,e]
b.children = [f,g,h]
c.children = [i,j]
d.children = [k]