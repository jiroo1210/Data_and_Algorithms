class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_path(node:Node, a:int, b:int)-> list:
    # TODO returns the path as a list, or None if there is no path
    # finding "path" is same as finding subtree that includes a & b
    # 1. find the diverging fork : above doesn't matter
    # 2. find a_route and b_route
    # 3. return a_route portion reversed + b_route
    # a_route[i-1:] include last shared parent
    # a_route[i:][::-1] take reverse 

    # work as from this list a_route, take this slicing [i:]
    # then of that list, a_route[i:], take this slicing [::-1] 
    # reverse

    path_a = []
    path_b = []
    a_route = path_helper(node,a,path_a)
    b_route = path_helper(node,b,path_b)

    # both of them needs to be True    
    if not a_route or not b_route:
        return None
    
    # need to cut off overlap
    i =0
    # "break points" 
    while i <len(a_route) and i<len(b_route):
        if a_route[i] != b_route[i]:
            break # at ith index their parents are different
        i += 1
    # share ancestors upto (i-1) index
    # paths now ready to recycled
    path_a = a_route[i-1:][::-1] 
    # portion out from common parent to a
    # then 'reverse', only include a_route

    path_b = b_route[i:] # b 

    # read from "left" to "right"
    return path_a + path_b

    # need to pass through empty list as start
    # passing [] did not work.
    # do something with None and initial set value
def path_helper(node,target,path:None):
    if path is None: path = [] # initial set up
    # also when recursion had dead end in one of branches

    # start by adding point and check
    path.append(node.value)

    # base case: found the node?
    if node.value == target: return path 
    # no need to change path
    
    # recursion
    for child in node.children:
        result = path_helper(child,target,path)
        if result: # node had a child that leads to a point
            return result
    
    # result not returned? than fail!
    path.pop() # remove last = dead end

    return None # this tree is done


if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_path(tree1, 3, 2)) # [3, 4, 1, 2]
    print(find_path(tree1, 1, 7)) # [1, 4, 7]
    print(find_path(tree1, 5, 5)) # [5]
    print(find_path(tree1, 7, 3)) # [7, 4, 3]
    print(find_path(tree1, 4, 8)) # None

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_path(tree2, 1, 4)) # [1, 2, 3, 4]
    print(find_path(tree2, 4, 1)) # [4, 3, 2, 1]
    print(find_path(tree2, 2, 3)) # [2, 3]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_path(tree3, 2, 3)) # [2, 1, 3]
    print(find_path(tree3, 1, 2)) # [1, 2]
    print(find_path(tree3, 5, 5)) # None

    

        
            

    

    



    

# model solution from last assignment

"""
def ancestor(node, a, b):
    return ancestor_helper(node, a, b, False)

def ancestor_helper(node, a, b, found_a):
    if node.value == a:
        found_a = True
    if node.value == b and found_a:
        return True

    for child in node.children:
        if ancestor_helper(child, a, b, found_a):
            return True
    return False
"""


if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_path(tree1, 3, 2)) # [3, 4, 1, 2]
    print(find_path(tree1, 1, 7)) # [1, 4, 7]
    print(find_path(tree1, 5, 5)) # [5]
    print(find_path(tree1, 7, 3)) # [7, 4, 3]
    print(find_path(tree1, 4, 8)) # None

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_path(tree2, 1, 4)) # [1, 2, 3, 4]
    print(find_path(tree2, 4, 1)) # [4, 3, 2, 1]
    print(find_path(tree2, 2, 3)) # [2, 3]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_path(tree3, 2, 3)) # [2, 1, 3]
    print(find_path(tree3, 1, 2)) # [1, 2]
    print(find_path(tree3, 5, 5)) # None