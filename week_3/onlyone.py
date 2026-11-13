def find_number(numbers:list):
    # TODO find the unique num
    if not numbers:
        return []
    
    prev_num = numbers[0]
    for i in range(1, len(numbers)):    
        if prev_num == numbers[i]:
            prev_num = numbers[i]
        else:
            if prev_num == numbers[i-2]:
                return numbers[i]
            else:
                return numbers[i-1]
    
""" model solution
def find_number(numbers):
    min_number = min(numbers)
    max_number = max(numbers)

    if numbers.count(min_number) == 1: # .count() is O(n) 
        return min_number
    else:
        return max_number

"""
        
        


if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2