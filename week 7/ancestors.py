class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def ancestor(node, a, b):
    # TODO returns bool if a is ancestor of b
    # plan: set bool; run recursive down the tree
    # include checking if node == a in node_locator
    a_tree = node_locator(node,a)

    # == None needs more computing than is
    # if expecting None, always use if a is None:
    if a_tree is None: return False
    
    b_tree = node_locator(a_tree,b)
    
    if b_tree is None: return False
    
    return True

# finding checks node.value & recursion

def node_locator(node, target):
    # base case
    if node.value == target: return node
    # recursion
    for child in node.children:
        descendant = node_locator(child,target)        
        if descendant is not None:
            return descendant
    # decendant is None
    return None
    # return decendant at the end will cause 
    # unnecessary computations


if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(ancestor(tree1, 1, 3)) # True
    print(ancestor(tree1, 2, 6)) # True
    print(ancestor(tree1, 3, 1)) # False
    print(ancestor(tree1, 5, 6)) # False
    print(ancestor(tree1, 3, 3)) # True

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(ancestor(tree2, 1, 4)) # True
    print(ancestor(tree2, 3, 2)) # False

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(ancestor(tree3, 1, 2)) # True
    print(ancestor(tree3, 1, 1)) # True
    print(ancestor(tree3, 2, 1)) # False
    print(ancestor(tree3, 5, 5)) # False