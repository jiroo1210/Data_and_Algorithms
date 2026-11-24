def count_pairs(numbers:list)->int:
    # TODO list of positive integers -> the maximal number of valid pairs
    # a pair (a,b) is valid if 2a <= b
    # each element cannot be used twice
    # plan: sort list; mark mid point
    # max pairs is n//2 
    # iteration start at x=0, y = n//2
    """ # old moves toward the larger 
    valid = 0
    n = len(numbers)
    if n < 2:
        return 0
    sorted_numbers = sorted(numbers)
    x = 0
    y = n//2

    while x< n//2 and y < n:
        if 2*sorted_numbers[x] <= sorted_numbers[y]:
            valid += 1
            x += 1
            y += 1
        else:
            y += 1

    return valid
    """
    # backward towards the smaller number
    valid = 0
    n = len(numbers)
    if n < 2:
        return 0
    sorted_numbers = sorted(numbers)
    x = n//2 -1
    y = n-1

    while x>=0 and y>=n//2:
        if 2*sorted_numbers[x] <= sorted_numbers[y]:
            valid += 1
            x -= 1
            y -= 1
        else:
            x-= 1
    return valid
    
    """ # model solution
    # if smallest element, a, can pair with k larger integers, 
    # there are at most k pairs meeting the condition
    # because a is the most restrictive condition
    # and the optimal solution will pair the a with the first b in larger integers it can pair with
    # and increment count, then move to the next smallest element to be paired
    def count_pairs(numbers):
    length = len(numbers)
    numbers = sorted(numbers)

    count = 0
    right_pos = length // 2
    for left_pos in range(length // 2):
        while right_pos < length and numbers[left_pos] * 2 > numbers[right_pos]:
            right_pos += 1
        if right_pos < length:
            count += 1
            right_pos += 1

    return count
    """    
    
    
if __name__ == "__main__":
    print(count_pairs([1])) # 0
    print(count_pairs([1, 2, 3])) # 1
    print(count_pairs([1, 2, 3, 4])) # 2
    print(count_pairs([1, 1, 1, 1])) # 0
    print(count_pairs([10**9, 1, 1, 1])) # 1
    print(count_pairs([4, 5, 1, 4, 7, 8])) # 2
    print(count_pairs([1, 2, 3, 2, 4, 6])) # 3

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    print(count_pairs(numbers)) # 41176
    print(count_pairs([1,2,4,5,10,20,21]))