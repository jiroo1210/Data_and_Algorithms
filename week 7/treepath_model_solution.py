def find_path(node, a, b):
    path_to_a = path_to_node(node, a)
    path_to_b = path_to_node(node, b)

    if path_to_a and path_to_b:
        while path_to_a and path_to_b and path_to_a[0] == path_to_b[0]:
            highest_node = path_to_a[0]
            path_to_a.pop(0)
            path_to_b.pop(0)
        path_to_a.reverse()
        return path_to_a + [highest_node] + path_to_b
    else:
        return None
# this pop at 0 position is laboursome(new indexing of whole list)

def path_to_node(node, x):
    if node.value == x:
        return [x]

    for child in node.children:
        path = path_to_node(child, x)
        if path:
            return [node.value] + path

    return None

# much more graceful approach