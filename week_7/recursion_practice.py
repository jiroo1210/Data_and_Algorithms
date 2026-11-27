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
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        for col in range(width):
            if grid[row][col].isdigit():
                return tree_helper(grid,row,col)
    return None

def parse_node(grid, y,x):
    height = len(grid)
    width = len(grid[0])
    left = x
    right = x
    
    while (left -1 >= 0) and (grid[y][left-1].isdigit()):
        left -= 1
    while (right+1 < width) and (grid[y][right+1].isdigit()):
        right += 1
    value = int(grid[y][left:right+1])
    return (value, left, right)            

def find_child_location(grid, y, left, right):
    
    height = len(grid)
    width = len(grid[0])
    
    if y+1 >=height:
        return []
    cur_y = y + 1 
    # y is "Node.value" ; locator on y+1
    cur_x = None
    # 1. find "|"
    for col in range(left,right+1):
        if grid[cur_y][col] == "|":
            cur_x = col
            break
    if cur_x is None:
        return []
    # 2. walk down the legs
    while cur_y +1 < height and grid[cur_y][cur_x] == "|":
        cur_y += 1
    # locator at row next to "|"

    # 3. check if cur_y  is leaf or horizontal bar
    # 3.1 if locator is at leaf's row 
    if grid[cur_y][cur_x].isdigit():
        return [(cur_y, cur_x)]
    
    # 3-2 If locator is at "horizontal bar" row, find horizontal bar
    bar_y = cur_y # to remind that locator is at the bar row

    left_end = cur_x
    right_end = cur_x

    while left_end -1 >= 0 and grid[bar_y][left_end - 1] in "-+":
        left_end -= 1
    while right_end + 1 < width and grid[bar_y][right_end + 1] in "-+":
        right_end += 1
    
    # 4. find children on under the horizontal bar row
    child_loc = []
    for col in range(left_end, right_end+1):
        if bar_y +1 < height and grid[bar_y + 1][col] == "|":
            child_y = bar_y + 1
            while child_y < height and grid[child_y][col] == "|":
                child_y += 1
                # in case there is more than 1 "|" in a column
            child_loc.append((child_y,col)) 

    return child_loc

def tree_helper(grid, y,x):
    value, left, right = parse_node(grid, y,x)
    child_loc = find_child_location(grid, y, left, right)
    children = [tree_helper(grid,cy,cx) for (cy,cx) in child_loc]
    return Node(value, children)


if __name__ == "__main__":
    grid = [
    "......100......",
    ".......|.......",
    "..+----+----+..",
    "..|....|....|..",
    "..25...7...304.",
    "..|.........|..",
    "..9.......+-+-+",
    "..........|...|",
    ".........12...8",]

    print(find_tree(grid))
    # Expected:
    # Node(100, [Node(25, [Node(9)]), Node(7), Node(304, [Node(12), Node(8)])]

    grid_edges = [
    "4096",
    "|...",
    "|...",
    "12..",
    ".|..",
    ".999"]
    # Expected:
    # Node(4096, [Node(12, [Node(999)])])
    grid_asymmetric = [
    "10........",
    "|.........",
    "+-----+--+",
    "|.....|..|",
    "2.....|..5",
    "......|...",
    ".....300.."]
    # Expected:
    # Node(10, [Node(2), Node(300), Node(5)])
    grid_tight = [
    "......50......",
    ".......|......",
    ".+--+--+---+..",
    ".|..|......|..",
    "11.22.....33..",
    "...........|..",
    ".........+-+-+",
    ".........|.|.|",
    ".........4.5.6"]
    # Expected:
    # Node(50, [Node(11), Node(22), Node(33, [Node(4), Node(5), Node(6)])])

    assert repr(find_tree(grid_edges)) == "Node(4096, [Node(12, [Node(999)])])"
    assert repr(find_tree(grid_asymmetric)) == "Node(10, [Node(2), Node(300), Node(5)])"
    assert repr(find_tree(grid_tight)) == "Node(50, [Node(11), Node(22), Node(33, [Node(4), Node(5), Node(6)])])"
    assert repr(find_tree(["..4096.."])) == "Node(4096)"
    print("All edge cases passed!")