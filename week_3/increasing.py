def count_sublists(numbers: list):
    # TODO
    # number of sublists for numbers[a:b +1] = 
    # number of sublists for numbers[a:b] + (b +1 - a)
    # trianle number = n(n+1)/2

    n = 0 # total number of sublists
    x = 0 # length of new sublists
    last = numbers[0]
    no_sub = True
    for i in range(1,len(numbers)):
        if numbers[i] > last:
            last = numbers[i]
            x += 1
            n += x
            no_sub = False
        else:
            x = 0
            last = numbers[i]
    
    
    if no_sub:
        return len(numbers)
    
    return  n + len(numbers)
if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4])) # 7
    print(count_sublists([1, 2, 3, 4])) # 10
    print(count_sublists([4, 3, 2, 1])) # 4
    print(count_sublists([1, 1, 1, 1])) # 4
    print(count_sublists([1, 2, 1, 2])) # 6

    numbers = list(range(1, 10**5+1))
    print(count_sublists(numbers)) # 5000050000