def count_numbers(a:int, b:int):
    # TODO find how may z in [a,b] that z = (2 or 5) *10 + (2 or 5)
    # did he meant [a,b) or [a,b]?
    # idea 1 use str and bool var for pass
    # idea 2 num of possibilities

    # method 1 too slow
    """
    count = 0
    
    for x in range(a,b+1):
        matched = True
        for y in str(x):
            if y in ['2','5']:
                pass
            else:
                matched = False
        if matched:
            count += 1
    
    return count
    """

    # method 2 count possible choices
    # each digit can be 2 or 5 (2 choices)
    # 2^number of digits?
    # use helper variable to count upto a - 1  & b
    return upto(b)-upto(a-1)

def upto(n:int):
    if n <2:
        return 0
    count = 0
    x = str(n)
    y = len(x) # front digit needs to be counted seperately
       
    # easy part
    for i in range(1,y): # for digits < y 
        count += 2**i
        # candidate - choice
    # for digits exactly y 
    for i in range(y):
        j = int(x[i]) # num on front 
        k = y - i - 1 # rest of digits that can be 2 or 5 & y-i (free positions) - 1(front num)
        if j > 5: # 2,5 can work on all digits
            count += 2*(2**k)
            return count 
        elif j == 5: # all of digits need to be verified (2 or 5)
            count += 1*(2**k)
            if i == y-1: # last digit
                count += 1
        elif j > 2:
            count += 1*(2**k) # only 2 works
            return count
            
        elif j ==2:
            # all of digits need to be verified (2 or 5)
            if i == y-1: # last digit
                count +=1
        else:
            return count

    return count

"""model solution
def count_numbers(a, b):
    numbers = [2, 5]
    count = 0

    for number in numbers:
        if a <= number <= b:
            count += 1

        if number > b: break

        numbers.append(number * 10 + 2)
        numbers.append(number * 10 + 5)

    return count
"""

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512
    print(upto(1))
    print(count_numbers(518, 875)) #4