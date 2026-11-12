def count_children(node):
    counts = []
    count_children_helper(node, counts) 
    # recursion happens within helper function
    return sorted(counts)

def count_children_helper(node, counts):
    counts.append(len(node.children))
    for child in node.children:
        count_children_helper(child, counts)