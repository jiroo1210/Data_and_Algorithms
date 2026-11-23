def analyze_route(grid:list) -> tuple:
    # TODO return (# of unique squares visited:int, exited:bool)
    # plan: translate grid into list of list of 1 character
    # if up tile is #, move right
    # if outside of limits, Exited
    """ # old solution
    # initialization
    exited = True
    r_location = (0,0)
    
    # translate string into list of list
    data = []
    for row, line in enumerate(grid):
        temp_list = []
        for col, letter in enumerate(line):
            if letter == "R":
                r_location = (row,col)
                letter = '.' # "clean" grid
            temp_list.append(letter)
        data.append(temp_list)
    # translation done

    # find boundaries
    width_max = len(grid[0])
    height_max = len(grid)

    # set up while loop
    row, col =  r_location 
    d_row, d_col = -1, 0
    visited = {(row, col)}
    repeat_check = {(row,col,d_row,d_col)} #start location
    
    # need to check data[row + d_row][col + d_col]
    while True:        
        next_row = row + d_row  
        next_col = col + d_col 
    
        if not (0 <= next_row < height_max and 0 <= next_col < width_max): # [0:next_]
            exited = True
            break       
        if data[next_row][next_col] == "#": 
            d_row, d_col = d_col, -d_row # wall; 90 degree clockwise   
            
        else: # path clear
            row , col = next_row, next_col
        
        if (row,col,d_row,d_col) in repeat_check:
            exited = False
            break

        visited.add((row,col))
        repeat_check.add((row,col,d_row,d_col))
            
    sq_count = len(visited)
    return (sq_count,exited)
    """
    # initialization
    exited = True
    r_location = (0,0)
    
    # find boundaries
    width_max = len(grid[0])
    height_max = len(grid)

    # Find Robot location

    for row in range(height_max):
        if "R" in grid[row]:
            r_location = (row,grid[row].index("R"))
            break

    # set up while loop
    row, col =  r_location 
    d_row, d_col = -1, 0
    visited = {(row, col)} # visited squares
    repeat_check = {(row,col,d_row,d_col)} # location and direction of next move
    
    # need to check data[row + d_row][col + d_col]
    while True:        
        next_row = row + d_row  
        next_col = col + d_col 
    
        if not (0 <= next_row < height_max and 0 <= next_col < width_max): # [0:next_]
            exited = True
            break       
        if grid[next_row][next_col] == "#": 
            d_row, d_col = d_col, -d_row # wall; 90 degree clockwise   
            
        else: # path clear
            row , col = next_row, next_col
        
        if (row,col,d_row,d_col) in repeat_check: 
            # check after move as start state will be already in repeat_check
            exited = False
            break

        visited.add((row,col))
        repeat_check.add((row,col,d_row,d_col))
            
    sq_count = len(visited)
    return (sq_count,exited)


    
    """ # model solution
    def analyze_route(grid):
    height = len(grid)
    width = len(grid[0])

    for y in range(height):
        if "R" in grid[y]:
            start_y = y
            start_x = grid[y].index("R")

    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0
    robo_y, robo_x = start_y, start_x

    visited_squares = set()
    visited_states = set()

    while True:
        visited_squares.add((robo_y, robo_x))

        state = (robo_y, robo_x, direction)
        if state in visited_states:
            escape = False
            break
        visited_states.add(state)

        new_y = robo_y + moves[direction][0]
        new_x = robo_x + moves[direction][1]

        if new_y < 0 or new_y >= height or new_x < 0 or new_x >= width:
            escape = True
            break

        if grid[new_y][new_x] == "#":
            direction = (direction + 1) % 4
            continue

        robo_y, robo_x = new_y, new_x

    return len(visited_squares), escape
    """

    

if __name__ == "__main__":
    grid1 = [".#......",
             "..#.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid1)) # (14, True)

    grid2 = ["........",
             ".##.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid2)) # (12, False)