def count_pairs(numbers:list)->int:
    # TODO list of positive integers -> the maximal number of valid pairs
    # a pair (a,b) is valid if 2a <= b
    # each element cannot be used twice
    # plan: sort list; mark mid point
    # iteration start at x=0, y = n//2
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