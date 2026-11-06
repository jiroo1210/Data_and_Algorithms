def count_sublists(numbers:list):
    # TODO count number of sublists with even numbers
    # not subsets, but numbers[a:b]
    # number of sublists for numbers[a:b +1] = 
    # number of sublists for numbers[a:b] + (b +1 - a)
    
    n = 0 # total number of sublists
    x = 0 # length of new sublists
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            x += 1
            n += x # x is increased
        else:
            x = 0
    
    return  n



if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6])) # 4
    print(count_sublists([1, 2, 3, 4])) # 2
    print(count_sublists([1, 1, 1, 1])) # 0
    print(count_sublists([2, 2, 2, 2])) # 10
    print(count_sublists([1, 1, 2, 1])) # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers)) # 5000050000