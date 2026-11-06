def find_rounds(numbers:list):
    # TODO find next element, increased by one. add to ordered
    # if the next item is continuous, collect in a same list
    if not numbers:
        return []
    ordered = []
    temp = []
    round = 1
    n=1
    end = len(numbers) + 1

    while n < end: # n terms inside
        while len(temp) < round:
            if not numbers:
                break
            if len(numbers) < n:
                temp.append(numbers)
                break
            inter = []
            inter = consec_num(n,inter,numbers)
            n += len(inter)
            numbers = clean_up(inter, numbers)
            temp.append(inter)
        
        round += 1
        if not numbers:
            ordered.append(temp)
            break
        ordered.append(temp)


    return ordered
        
    
def consec_num(first:int, inter:list, numbers:list):
    if not inter:
        inter.append(first)
    idx = numbers.index(first)
    for m in range(idx,len(numbers)):
        if not numbers:
            return inter
        if numbers[m] == inter[-1]+1:
            inter.append(numbers[m]) 
    return inter

def clean_up(inter:list, numbers):
    for num in inter:
        if num in numbers:
            numbers.pop(numbers.index(num))
    return numbers
    



    
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
    