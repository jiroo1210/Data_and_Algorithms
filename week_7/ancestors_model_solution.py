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

# model solution pass bool as I wanted
# shorter code and less recursion