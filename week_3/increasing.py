def count_sublists(numbers: list):
    # TODO
    # number of sublists for numbers[a:b +1] = 
    # number of sublists for numbers[a:b] + (b +1 - a)
    # triangle number = n(n+1)/2

    n = 1 # total number of sublists
    x = 1 # length of new sublists
    # last = numbers[0] can cause index error if numbers is empty
    
    for i in range(1, len(numbers)):
        if numbers[i - 1] < numbers[i]:
            x += 1 # length increased by 1, so number of sublists increased by x(prev) + 1
        else:
            x = 1 # new streak
        n += x # add the length of new sublists to total number of sublists
           
    return  n

    """ model solution
    def count_sublists(numbers):
    total = 1
    count = 1

    for i in range(1, len(numbers)):
        if numbers[i - 1] < numbers[i]:
            count += 1
        else:
            count = 1
        total += count

    return total
    """

if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4])) # 7
    print(count_sublists([1, 2, 3, 4])) # 10
    print(count_sublists([4, 3, 2, 1])) # 4
    print(count_sublists([1, 1, 1, 1])) # 4
    print(count_sublists([1, 2, 1, 2])) # 6

    numbers = list(range(1, 10**5+1))
    print(count_sublists(numbers)) # 5000050000