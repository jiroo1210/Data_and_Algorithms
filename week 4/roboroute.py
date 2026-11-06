def analyze_route(grid:list) -> tuple:
    # TODO return (# of unique squares visited:int, exited:bool)
    # plan: translate grid into list of list of 1 character
    # if up tile is #, move right
    # if outside of limits, Exited
    
    # initialization
    exited = True
    r_location = (0,0)
    

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