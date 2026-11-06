def count_splits(numbers:list)->int:
    # TODO count number of ways to 
    # split list so that set(lhs) == set (rhs)
    
    whole_set = set(numbers)
    unique = len(whole_set)
    
    n = len(numbers)
    left_end = -1 # start before positon 0
    right_end = n # after index of the last position
    # find set(numbers[:left_end]) == set(numbers[right_end:]) == whole_set
    # then sub list count = b - a + 1

    lhs = set()
    rhs = set()
    for i in range(n):
        lhs.add(numbers[i])
        if len(lhs) == unique:
            left_end = i + 1
            break

    back_numbers = numbers[::-1]
    for i in range(n):
        rhs.add(back_numbers[i])
        if len(rhs) == unique:
            right_end = n - (i + 1)
            break

    count = right_end - left_end + 1
    # count > -1 
    return max(count,0) # if split not found, 0


if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1])) # 3
    print(count_splits([1, 1, 2, 1])) # 0
    print(count_splits([1, 2, 1, 2])) # 1
    print(count_splits([1, 2, 3, 4])) # 0
    print(count_splits([1, 2, 1, 2, 1, 2])) # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers)) # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers)) # 1