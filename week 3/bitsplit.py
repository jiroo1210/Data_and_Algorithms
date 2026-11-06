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

    for i in range(len(sequence)):
        if sequence[i] == "0":
            z_streak += 1
        else:
            o_streak += 1
        if z_streak == o_streak:
            matched += 1
    
    return max(matched -1,0) # case of sequence & "" split

    


if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999