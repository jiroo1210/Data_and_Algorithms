class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_tree(grid:list)-> Node: 
    # TODO tructure of the depicted tree using the class Node
    # 1. read the file: do not replace dot. approach as grid[row][colum]
    # 2. need recursion in format of 
    #   Node(parent, children)

    # need row, column to be independent of index
    # choose -1; make sure row and col are positive int
    r_row, r_col = -1, -1
    # finding root
    # .replace() .strip() did not help
    # check if O(n^2) is accepted
    for row in range(len(grid)):
        for column in range(len(grid[row])): 
            # TODO find a way to find root
            if grid[row][column].isdigit():
                r_row, r_col = row, column
                break # BUG only stops column loop
        if r_row != -1: # stop row loop
            break
    if r_row == -1:
        return None
    
    return tree_helper(grid,r_row,r_col)

def tree_helper(grid, r_row, r_column) ->Node:
    parent = int(grid[r_row][r_column]) # need to be int
    children = []
    # position of / | \ are set, regardless of they exist or not
    # "/" r+1 c-1 ; "|" r+1 c ; "\" r+1 c+1
    # A: r+2 c-2 ; B r+2 c ; C r+2 c+2
    # next digit
    # above is wrong. 
    # one or more connection symbols
    # no hard coding

    # need the r c not exceed range
    # different for each connector
    
    # "/" left down  if same, no child
    if (r_row+1 < len(grid)) and (r_column -1 >= 0) and (grid[r_row + 1][r_column -1] == r"/"):
        # use while and update row & column 
        # bc in while loop need one update
        # set row column inside loop
        row, column = r_row +1,r_column -1
        while row + 1 < len(grid) and column -1 >=0:
            if grid[row+1][column - 1].isdigit():
                children.append(
                    tree_helper(grid,row+1,column-1))
                break
            # BUG need to update by 1 only
            row += 1
            column -= 1
    
    # "|" straight down
    if (r_row + 1 < len(grid)) and (0<=r_column< len(grid[0])) and (grid[r_row + 1][r_column] == r"|"):
        row, column = r_row +1, r_column
        while row +1 <len(grid):
            if grid[row+1][column].isdigit():
                children.append(
                    tree_helper(grid,row+1,column))
                break
            row += 1
            # column no change

    # need to reset row & column
    
    # "\" r"\" did not work nor r"\\" 
    if (r_row+1 < len(grid)) and (r_column + 1 < len(grid[0])) and \
        (grid[r_row+1][r_column +1] == "\\"):
        row, column = r_row + 1, r_column +1

        while row +1 <len(grid) and column +1 < len(grid[0]):
            if grid[row+1][column +1].isdigit():
                children.append(
                    tree_helper(grid,row+1,column+1))
                break
            row += 1
            column += 1 # BUG moving right

    return Node(parent, children)



if __name__ == "__main__":
    grid = [r"...........",
            r"...........",
            r"......5....",
            r"...../.\...",
            r"....3...\..",
            r"....|....1.",
            r"....2......"]
    tree = find_tree(grid)
    print(tree)
    # Node(5, [Node(3, [Node(2)]), Node(1)])

    grid = [r"....1.....",
            r".../.\....",
            r"..2...\...",
            r"..|....3..",
            r"..7.../|\.",
            r"./.\.4.5.6",
            r"8...9....."]
    tree = find_tree(grid)
    print(tree)
    # Node(1, [Node(2, [Node(7, [Node(8), Node(9)])]), Node(3, [Node(4), Node(5), Node(6)])])
    grid = [r"6"]
    tree = find_tree
    print(tree)