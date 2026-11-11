def find_sums(numbers:list, size:int):
    # TODO
    if size > len(numbers): return ValueError
    if size == len(numbers): return [sum(numbers)]
    
    first = sum(numbers[:size])
    sum_list = [first]
    # first sublist
    for i in range(len(numbers)-size):
        sum_list.append(sum_list[-1] - numbers[i] + numbers[i + size])
        # from last element of sum_list, 
        # subtract the first element of the previous sublist 
        # and add the last element of the current sublist
    return sum_list
        
"""model solution
def find_sums(numbers, size):
    # does not take account of possible errors
    
    result = []

    current_sum = sum(numbers[:size])
    result.append(current_sum)

    for pos in range(size, len(numbers)):
        current_sum += numbers[pos]
        current_sum -= numbers[pos - size]
        result.append(current_sum)
        # not one liner
    return result

"""
    


if __name__ == "__main__":
    print(find_sums([1], 1)) # [1]
    print(find_sums([1, 8, 2, 7, 3, 6, 4, 5], 6)) # [27, 30, 27]

    print(find_sums([1, 2, 3, 4, 5], 1)) # [1, 2, 3, 4, 5]
    print(find_sums([1, 2, 3, 4, 5], 2)) # [3, 5, 7, 9]
    print(find_sums([1, 2, 3, 4, 5], 3)) # [6, 9, 12]
    print(find_sums([1, 2, 3, 4, 5], 4)) # [10, 14]
    print(find_sums([1, 2, 3, 4, 5], 5)) # [15]

    numbers = list(range(10**5))
    sums = find_sums(numbers, 10**4)
    print(sums[5]) # 50045000
    print(sums[42]) # 50415000
    print(sums[1337]) # 63365000