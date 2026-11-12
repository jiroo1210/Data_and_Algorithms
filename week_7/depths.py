class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def count_nodes(node, depth):
    # TODO returns the node count for chosen depth
    if depth == 0: # base case when at "bottom"
        return 1
    node_count = 0
    level = depth
    for child in node.children:
        node_count += count_nodes(child,level-1)
    return node_count

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_nodes(tree1, 0)) # 1
    print(count_nodes(tree1, 1)) # 3
    print(count_nodes(tree1, 2)) # 3
    print(count_nodes(tree1, 3)) # 0

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(count_nodes(tree2, 0)) # 1
    print(count_nodes(tree2, 1)) # 1
    print(count_nodes(tree2, 2)) # 1
    print(count_nodes(tree2, 3)) # 1
    print(count_nodes(tree2, 4)) # 0

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(count_nodes(tree3, 0)) # 1
    print(count_nodes(tree3, 1)) # 3
    print(count_nodes(tree3, 2)) # 0