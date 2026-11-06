class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def count_leaves(node:Node) -> int:
    # TODO a reference to the root of the tree as a parameter and returns the number of leaves
    if not node.children:
        return 1

    no_leaves = 0
    for child in node.children:
        if not child.children:
            no_leaves += 1
        else:
            no_leaves += count_leaves(child)
    return no_leaves

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_leaves(tree1)) # 4

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(count_leaves(tree2)) # 1

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(count_leaves(tree3)) # 3

    single_node = Node(1)
    print(count_leaves(single_node)) # 1