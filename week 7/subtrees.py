class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def count_subtrees(node):
    # TODO list of subtree sizes (not a set)
    subtrees = []
    # try helper recursive function
    subtrees_helper(node,subtrees)
    return sorted(subtrees)

def subtrees_helper(node, subtrees):
    # leaf is counted as 1
    # start count from 1
    count = 1
    # no need to return 1 yet
    for child in node.children:
        count += subtrees_helper(child,subtrees) 
        # stacking count recursively
    subtrees.append(count)
    # add current node's count to subtrees
    # only because the task asks for all node's subtrees count
    # seems redundant idk
    
    return count #for recursion 

if __name__ == "__main__":

    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_subtrees(tree1)) # [1, 1, 1, 1, 2, 3, 7]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(count_subtrees(tree2)) # [1, 2, 3, 4]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(count_subtrees(tree3)) # [1, 1, 1, 4]