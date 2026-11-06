def count_rounds(numbers:list):
    # TODO find a way to count rounds

    """
    model solution from rounds
    def find_rounds(numbers):
    n = len(numbers)

    result = []
    current = 1

    while current <= n:
        round = []
        for number in numbers:
            if number == current:
                round.append(number)
                current += 1
        result.append(round)

    return result
    """
    n = len(numbers)

    round = 1
    # make an value-index dictionary to find index of certain value easily
    # essentially a glossary
    position = {}
    for index, item in enumerate(numbers): # enumerate(list) gives iterable emnumerate objects, of (index,value)
        position[item] = index
    # if the index of next value is greater, than round continues
    for current in range(1,n): # 1<= current <= n; NOT index
        if position[current+1] < position[current]: # need new round
            round += 1
    return round
    
if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4
    for index, item in enumerate([2, 1, 4, 7, 5, 3, 6, 8]):
        print(index,item)
    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000