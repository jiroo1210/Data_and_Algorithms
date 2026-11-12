def find_number(numbers:list):
    # TODO find the unique num
    first = numbers[0]

    for i in range(1, len(numbers)):    
        if first == numbers[i]:
            first = numbers[i]
        else:
            if i -1 > -1:
                if first == numbers[i-2]:
                    return numbers[i]
                else:
                    return numbers[i-1]


        
        


if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2