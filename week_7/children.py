class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def count_children(node):
    # TODO returns the list of child counts ascending order
    # starting with empty family_tree did not work

    family_tree = [len(node.children)]
    for child in node.children:
    # adding len(node.children) here made repeated input
        if child.children:
            family_tree.extend(count_children(child))
            # appending lead to list in list
        else:
            family_tree.append(0)
        
    return sorted(family_tree)

""" # model solution
def count_children(node):
    counts = []
    count_children_helper(node, counts) 
    # recursion happens within helper function
    return sorted(counts)

def count_children_helper(node, counts):
    counts.append(len(node.children))
    for child in node.children:
        count_children_helper(child, counts)
"""

""" # Alternative solution from Gemini
    # on how to avoid nested list.
    # yield from will flatten the list while keeping "return"

def count_children(node):
    counts = [len(node.children)] 
    # 1. Count current node's children
    counts.extend(sum([count_children(child) for child in node.children], [])) 
    # 2. Recursively get children counts from all children
    return sorted(counts)
"""

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_children(tree1)) # [0, 0, 0, 0, 1, 2, 3]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(count_children(tree2)) # [0, 1, 1, 1]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(count_children(tree3)) # [0, 0, 0, 3]