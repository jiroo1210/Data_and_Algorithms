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
    """ model solution
    def calculate(input, rules):
    symbols = ["L"] + list(input) + ["R"]

    pos = 0
    state = 1
    counter = 0

    while True:
        found = False

        for old_symbol, old_state, new_symbol, new_state, action in rules:
            if symbols[pos] == old_symbol and state == old_state:
                found = True
                counter += 1

                symbols[pos] = new_symbol
                state = new_state

                if action == "RIGHT": pos += 1
                if action == "LEFT": pos -= 1
                if action == "ACCEPT": return True
                if action == "REJECT": return False

                if pos < 0 or pos >= len(symbols):
                    return False

                break

        if not found or counter == 1000:
            return False
    """

def create_rules():
    # TODO accept input[:mid] == input[mid:] 
    # TODO reject input == input[::-1] input[mid] never used
    
    rules = []
    # rules composed of (cur_sym, cur_st, new_sym, new_st, action)

    # after research, this is Turing machine simulator
    # finding group1group1 repeatition
    
    
    # state 1: first move to right until R
    # change first 0 to A, 
    #              1 to B, 
    # no change for L & R
    rules.append(("L", 1, "L", 1, "RIGHT"))
    rules.append(("1", 1, "A", 2, "RIGHT"))
    rules.append(("0", 1, "B", 2, "RIGHT"))
    # mark 1 digit change by increasing state

    # state 2: move to right end of string
    rules.append(("1", 2, "1", 2, "RIGHT"))
    rules.append(("0", 2, "0", 2, "RIGHT"))

    # state 3: turned left at R, 'X', or 'Y'
    rules.append(("R", 2, "R", 3, "LEFT"))
    rules.append(("X", 2, "X", 3, "LEFT"))
    rules.append(("Y", 2, "Y", 3, "LEFT"))

    # state 4 : first 0 from travel to left is replaced with "X" 
    #           first 1 from travel to left is replaced with "Y" 
    rules.append(("1", 3, "X", 4, "LEFT"))
    rules.append(("0", 3, "Y", 4, "LEFT"))
    
    # state 4_1 : fails when "A" or "B" -> odd length (no 0,1 to be "X" or "Y")
    rules.append(("A", 3, "A", 3, "REJECT"))
    rules.append(("B", 3, "B", 3, "REJECT"))

    # state 4_2: back to left wall by passthrough "0" and "1"
    rules.append(("0", 4, "0", 4, "LEFT"))
    rules.append(("1", 4, "1", 4, "LEFT"))

    # state 4_3: at left wall, no change, go to state 5 to travel right
    # left wall: "L", "A", "B"
    # then travel to right (state 1)
    rules.append(("L", 4, "L", 1, "RIGHT"))
    rules.append(("A", 4, "A", 1, "RIGHT"))
    rules.append(("B", 4, "B", 1, "RIGHT"))

    # state 5: back to left wall, no change

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

    """ model solution
    def create_rules():
    rules = []

    # phase 1: find first 0 or 1, mark as A or B, move to right wall 
    #          then move left to find first 0 or 1, mark as C or D, move to left wall

    # state 1: move to right until first 0 or 1
    #          then change to A or B, and move to state 2
    # state 2: passthrough to right until R

    rules.append(("L", 1, "L", 1, "RIGHT"))
    rules.append(("0", 1, "A", 2, "RIGHT"))
    rules.append(("1", 1, "B", 2, "RIGHT"))
    rules.append(("A", 1, "A", 1, "RIGHT"))
    rules.append(("B", 1, "B", 1, "RIGHT"))
    rules.append(("0", 2, "0", 2, "RIGHT"))
    rules.append(("1", 2, "1", 2, "RIGHT"))
    rules.append(("C", 2, "C", 2, "RIGHT"))
    rules.append(("D", 2, "D", 2, "RIGHT"))
 
    # state 2->3: reached right wall, turn left
    # state 3:   move until first 0 or 1, change to C or D,
    #          passthrough A, B, C, D, and move to state 4
    # state 4: Rewinds back (passthrough) to L to start the next search
    rules.append(("R", 2, "R", 3, "LEFT"))
    rules.append(("0", 3, "C", 4, "LEFT"))
    rules.append(("1", 3, "D", 4, "LEFT"))
    rules.append(("C", 3, "C", 3, "LEFT"))
    rules.append(("D", 3, "D", 3, "LEFT"))
    rules.append(("0", 4, "0", 4, "LEFT"))
    rules.append(("1", 4, "1", 4, "LEFT"))
    rules.append(("A", 4, "A", 4, "LEFT"))
    rules.append(("B", 4, "B", 4, "LEFT"))
    rules.append(("L", 4, "L", 1, "RIGHT"))
 
    # phase 2: all 0,1 converted to A,B,C,D
    #          now convert A,B or C,D to X 
    #          passthrough after conversion
    #          when no more A,B or C,D, accept
    #  
    # state 1->5: only found C, or D, to start phase 2 
    # state 5: move left until L, passthrough A, B, C, D
    # state 6: move right until first A or B, change to X as marked
    #          move to state 7 or 8 depending on A or B changed
    # state 7,8 : move to right wall, passthrough A, B, C, D, X   
    rules.append(("C", 1, "C", 5, "LEFT"))
    rules.append(("D", 1, "D", 5, "LEFT"))
    rules.append(("A", 5, "A", 5, "LEFT"))
    rules.append(("B", 5, "B", 5, "LEFT"))
    rules.append(("L", 5, "L", 6, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("A", 6, "X", 7, "RIGHT"))
    rules.append(("B", 6, "X", 8, "RIGHT"))
    rules.append(("A", 7, "A", 7, "RIGHT"))
    rules.append(("A", 8, "A", 8, "RIGHT"))
    rules.append(("B", 7, "B", 7, "RIGHT"))
    rules.append(("B", 8, "B", 8, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))
    rules.append(("X", 8, "X", 8, "RIGHT"))
    rules.append(("C", 7, "X", 5, "LEFT"))
    rules.append(("D", 8, "X", 5, "LEFT"))
    rules.append(("X", 5, "X", 5, "LEFT"))
    rules.append(("R", 6, "R", 6, "ACCEPT"))
 
    return rules

    """

    

if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules)) # True
    print(calculate("001001", rules)) # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules)) # False
    print(calculate("00100", rules)) # False
    print(calculate("10111101", rules)) # False
    print(calculate("0111101111", rules))