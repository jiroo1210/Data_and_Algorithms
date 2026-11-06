def calculate(input:str, rules:list):
    # TODO
    # Each symbol in the rules is 0, 1 or a letter in the range A–Z. 
    # Each state int:range(1,101)
    # 1 combination : 1 action
    
    import string
    attempts = 0 # max 1000
    accepted_str = "01"+ string.ascii_uppercase # accepted symbol
    accepted_ran = list(range(1,101)) # range of string, not position
    
    rules_dict = {(rule[0],rule[1]):(rule[2],rule[3],rule[4]) for rule in rules}
    

    # initial state
    cmd = [letter for letter in input]
    cmd.append("R")
    cmd.insert(0,"L")
    st = 1
    pos = 0 # position of new string cmd
    # LEFT and RIGHT of string position, not robot position
    # -1 < pos  < len(cmd)
    # Is symbol being written on top of current one? 
    # if above, cmd needs to be list
    

    while -1 < pos < len(cmd):
        ch = cmd[pos] # shallow copy for abbrev
        if ch not in accepted_str:
            return False
        if st not in accepted_ran:
            return False
        if (ch,st ) not in rules_dict:
            return False
        if attempts > 1000:
            return False
        (new_sym, new_st, action) = rules_dict[(ch, st)]
        st = new_st
        cmd[pos]= new_sym # changes cmd 
        if action == "REJECT":
            return False 
        elif action == "ACCEPT":
            return True
        elif action == "LEFT":
            pos -= 1
            attempts += 1
        elif action == "RIGHT":
            pos += 1
            attempts += 1
        else:
            attempts += 1
    
    # do I need to return the input string? No?
    # why is this working?????????
    # no return gives None for certain input
    # when pos < -1 or pos > len(cmd)
    return False

   

if __name__ == "__main__":
    rules = [] # list of tuples
    #           @ sym , st -> @ sym, st 
    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT"))
    rules.append(("1", 4, "X", 5, "RIGHT"))
    rules.append(("1", 2, "X", 6, "RIGHT"))
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    print(calculate("0", rules)) # False
    print(calculate("00", rules)) # False
    print(calculate("01", rules)) # True
    print(calculate("0110", rules)) # True
    print(calculate("0101", rules)) # True
    print(calculate("1000", rules)) # False
    print(calculate("00110101", rules)) # True
    print(calculate("00111101", rules)) # False