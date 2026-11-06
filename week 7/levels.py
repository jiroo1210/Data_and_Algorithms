class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_levels(node:Node)-> list:
    # TODO return a list of the nodes on each level in numerical order
    # plan make dictionary of level:nodes=list
    # make a list for each level
    level_dict = {0:[node.value]}
    level = 1
    depth_helper(node, level_dict, level)
    final_list =[]
    for key,value in level_dict.items():
        final_list.append(sorted(value))
    return final_list

# helper function to do recursive 
def depth_helper(node, level_dict, level):
    for children in node.children:
        if level not in level_dict:
            level_dict[level] =[]
        level_dict[level].append(children.value)
        depth_helper(children,level_dict,level+1)
    


if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_levels(tree1)) # [[1], [2, 4, 5], [3, 6, 7]]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_levels(tree2)) # [[1], [2], [3], [4]]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_levels(tree3)) # [[1], [2, 3, 4]]