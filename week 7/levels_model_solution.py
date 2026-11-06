def find_levels(node):
    pairs = []
    find_levels_helper(node, 0, pairs)
    pairs.sort()

    levels = []
    prev_depth = -1

    for depth, value in pairs:
        if depth != prev_depth:
            levels.append([])
        levels[-1].append(value)
        prev_depth = depth

    return levels

def find_levels_helper(node, depth, pairs):
    pairs.append((depth, node.value))
    for child in node.children:
        find_levels_helper(child, depth + 1, pairs)

# model solution only uses list; much faster than my dictionary method