def find_order(n):
    # TODO every second player leaves. find the order in which the players leave the circle.
    # Tip says make a new list of survivors
    if n == 0: return None
    if n == 1: return [1]
    # dictionary for each value's next one
    next_one = {i:i+1 for i in range(1,n)} # last pair needs to be n-1 :n
    # step size 2 sounded more reasonable, but loop below did not work
    # when n%2 == 1, error.
    # last key of next_one needs to circle back to 1
    next_one[n] = 1 # back to start

    max_size = len(next_one)
    current = 1
    lost = []
    # using range iteration doesnt work; reduce?

    while len(lost) < max_size:
        booted = next_one[current] # current, booted, next guy; next guy == next_one[i+2]
        lost.append(booted)
        next_one[current] = next_one[booted] # connect current with next guy
        # need to update current
        current = next_one[current] # next_one[booted] causes error
        # beacuse next_one[current] is the next guy

    return lost


    
    

if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]
    order = find_order(10**5)
    print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]