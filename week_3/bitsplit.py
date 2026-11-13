def count_splits(sequence:str):
    # TODO return valid count of splits
    # part.count(0)==part.count(1)
    if len(sequence) < 3:
        return 0
    zeros = sequence.count("0")
    ones = sequence.count("1")
    # if zeros != ones, cannot split evenly
    if zeros != ones:
        return 0

    z_streak = 0
    o_streak = 0

    matched = 0

    for i in range(len(sequence)): # for char in sequence: is better
        if sequence[i] == "0":
            z_streak += 1
        else:
            o_streak += 1
        if z_streak == o_streak:
            matched += 1 
            # if i == len(sequence)-1: matched -=1
            # this will remove the -1 at the return statement
            # but one more step in each iteration is not needed, 
            # so we can just subtract 1 at the end
    # matched - 1 because we cannot "split" at the end of the sequence, 
    # but z_streak == o_streak at the end of the sequence, 
    # so we need to subtract 1 from the count of matched
    return max(matched -1,0) # case of sequence & "" split

    """ model solution
    def count_splits(sequence):
    total0 = sequence.count("0")
    total1 = sequence.count("1")

    if total0 != total1:
        return 0

    count0 = count1 = 0
    result = 0

    for symbol in sequence:
        if symbol == "0":
            count0 += 1
        if symbol == "1":
            count1 += 1

        if count0 == count1:
            result += 1

    return result - 1
    """
    


if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999