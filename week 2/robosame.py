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
        if attempts > 5000:
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

    return False
    # rules composed of (cur_sym, cur_st, new_sym, new_st, action)
def create_rules():
    # TODO accept input[:mid] == input[mid:] 
    # TODO reject input == input[::-1]
    from random import randint
    import string
    accepted_str = "01"+ string.ascii_uppercase # accepted symbol
    accepted_ran = list(range(1,101)) # range of string, not position
    actions = ["LEFT","RIGHT", "ACCEPT", "REJECT"]
    rules = []
   

    # after research, this is Turin machine simulator
    # finding group1group1 repeatition
    
    # states:
    # 1 move to right
    # 2 
    # Shouldn't have changed all 01 to AB
    # state 1: first move to R
    rules.append(("L", 1, "L", 1, "RIGHT"))
    rules.append(("1", 1, "A", 2, "RIGHT"))
    rules.append(("0", 1, "B", 2, "RIGHT"))
    # mark 1 digit change by increasing state

    # Pass through "0" and "1"
    rules.append(("1", 2, "1", 2, "RIGHT"))
    rules.append(("0", 2, "0", 2, "RIGHT"))

    # state 3: turned left at R, 'X', 'Y'
    rules.append(("R", 2, "R", 3, "LEFT"))
    rules.append(("X", 2, "X", 3, "LEFT"))
    rules.append(("Y", 2, "Y", 3, "LEFT"))

    # state 4 "X" "Y" added
    rules.append(("1", 3, "X", 4, "LEFT"))
    rules.append(("0", 3, "Y", 4, "LEFT"))
    
    # case: "A" or "B" -> odd length (no 0,1 to be "X" or "Y")
    rules.append(("A", 3, "A", 3, "REJECT"))
    rules.append(("B", 3, "B", 3, "REJECT"))

    # back to state for travelling left; no change
    rules.append(("0", 4, "0", 4, "LEFT"))
    rules.append(("1", 4, "1", 4, "LEFT"))

    # left wall: "L", "A", "B"
    # then travel to right (state 1)
    rules.append(("L", 4, "L", 1, "RIGHT"))
    rules.append(("A", 4, "A", 1, "RIGHT"))
    rules.append(("B", 4, "B", 1, "RIGHT"))

    # at middle point, back to "L"
    rules.append(("X", 1, "X", 5, "LEFT"))
    rules.append(("Y", 1, "Y", 5, "LEFT"))

    # need cases for "A", "B", "X", "Y", "0", "1" to move to left
    # do I only need for abxy?
    for c in ["A", "B", "X", "Y", "0", "1"]:
        rules.append((c, 5, c, 5, "LEFT"))
    
    # stop at L, start searching
    rules.append(("L", 5, "L", 6, "RIGHT"))

    # matching "A" and "X" (originally 1)
    # change to "C" so it can be marked
    # state 7
    rules.append(("A", 6, "C", 7, "RIGHT"))

    # matching "B" and "Y" (originally 0)
    # also "C" state 8
    rules.append(("B", 6, "C", 8, "RIGHT"))

    # skipping counted "C"
    rules.append(("C", 6, "C", 6, "RIGHT"))

    # success when nothing left to turn D
    rules.append(("D", 6, "D", 6, "ACCEPT"))
    

    # move along until "X" state 7
    for c in ["A", "B", "C", "D", "0", "1"]:
        rules.append((c, 7, c, 7, "RIGHT"))

    # @ X
    rules.append(("X", 7, "D", 9, "LEFT"))
    rules.append(("Y", 7, "Y", 7, "REJECT")) # different group
    rules.append(("R", 7, "R", 7, "REJECT")) # wall

    # travel right
    for c in ["A", "B", "C", "D", "0", "1"]: # no xy 
        rules.append((c, 8, c, 8, "RIGHT"))

    # @ Y
    rules.append(("Y", 8, "D", 9, "LEFT")) # matched Y
    rules.append(("X", 8, "X", 8, "REJECT")) # match fail
    rules.append(("R", 8, "R", 8, "REJECT")) # wall

    # travel left as being matched
    for c in ["A", "B", "C", "D", "0", "1"]:
        rules.append((c, 9, c, 9, "LEFT"))
    
    # back to L to start loop again
    # start searching again (state 6)
    rules.append(("L", 9, "L", 6, "RIGHT"))

    return rules

    

if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules)) # True
    print(calculate("001001", rules)) # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules)) # False
    print(calculate("00100", rules)) # False
    print(calculate("10111101", rules)) # False
    print(calculate("0111101111", rules))