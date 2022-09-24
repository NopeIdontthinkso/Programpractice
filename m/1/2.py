from typing import List

class Node:
    def __init__(self, name):
        self.name: int = name
        self.children: List[Node] = []
        self.root: bool = True
        self.height: int = 0
def dfs(node: Node):
    for child in node.children:
        dfs(child)
    if node.children:
        children_values = [child.height for child in node.children]
        node.height = 1 + max(children_values)
        total_height.append(node.height)

z = int(input())
list1 = []
list2 = []
for i in range(z):
    list1.append([int(x) for x in input().split()])
tree = []
for i in range(z):
    tree.append(Node(i+1))
for i in range(z):
    if list1[i][0] != 0:
        for j in range(len(list1[i])-1):
            child_name = list1[i][j+1]
            tree[i].children.append(tree[child_name - 1])
            tree[child_name - 1].root = False

total_height = []

for i in range(len(tree)):
    if tree[i].root == True:
        print(tree[i].name)
        dfs(tree[i])

print(sum(total_height))




