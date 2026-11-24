def count_steps(numbers:list)->int:
    # TODO return number of steps
    # make dictionary for number, index?
    if len(numbers) == 1:
        return 0
    number_index ={number: i for i, number in enumerate((numbers))}
    sorted_numbers = sorted(numbers)
    step = 0
    pos = 0
    for number in sorted_numbers:
        step += abs(number_index[number] - pos)
        pos = number_index[number]
    
    return step

""" # model solution

def count_steps(numbers):
    pairs = [] # using tuple to store number and index
    for pos, number in enumerate(numbers):
        pairs.append((number, pos))
    pairs.sort() # sort by (number, position) and no need to look up dict

    robo_pos = 0
    total_steps = 0
    for number, pos in pairs:
        total_steps += abs(robo_pos - pos) # how far is the next number?
        # if robo_pos < pos, value is negative, thus abs()
        robo_pos = pos

    return total_steps
"""

if __name__ == "__main__":
    print(count_steps([1])) # 0
    print(count_steps([1, 2, 3])) # 2
    print(count_steps([3, 2, 1])) # 4
    print(count_steps([42, 1337, 1, 10**9])) # 7
    print(count_steps([1, 3, 5, 7, 8, 6, 4, 2])) # 28
    print(count_steps([10**6, 10**8, 10**7, 10**9])) # 5

    numbers = [(x * 999983) % 10**9 + 1 for x in range(10**5)]
    print(count_steps(numbers)) # 4871908997