def find_rounds(numbers:list):
    # TODO find next element, increased by one. add to ordered
    # if the next item is continuous, collect in a same list
    if not numbers:
        return []
    ordered = []
    
    n = 1
    end = len(numbers) + 1
    while n < end:
        temp = []
        idx = numbers.index(n)
        temp.append(numbers.pop(idx)) # len(numbers) 1 shorter 
        n += 1
        # numbers[idx] = numbers[idx+1] before pop
        while idx < len(numbers):
            if numbers[idx] == temp[-1] + 1:
                temp.append(numbers.pop(idx)) # pop used. dont increase idx
                n += 1
            else:
                idx += 1
        ordered.append(temp)

    return ordered

""" model solution
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

    
if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
    