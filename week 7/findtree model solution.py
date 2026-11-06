class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_tree(grid):
    height, width = len(grid), len(grid[0])

    for y in range(height):
        for x in range(width):
            if grid[y][x] != '.':
                return create_node(grid, y, x)

def create_node(grid, y, x):
    height, width = len(grid), len(grid[0])

    value = int(grid[y][x])
    children = []

    directions = [(1, -1, "/"), (1, 0, "|"), (1, 1, "\\")]

    for dy, dx, char in directions:
        child_y = y + dy
        child_x = x + dx

        if child_y < height and child_x >= 0 and child_x < width:
            if grid[child_y][child_x] == char:
                while grid[child_y][child_x] == char:
                    child_y += dy
                    child_x += dx
                children.append(create_node(grid, child_y, child_x))

    return Node(value, children)