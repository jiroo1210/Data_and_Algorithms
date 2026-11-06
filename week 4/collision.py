
# using model solution from prev. task
A = 23
M = 2**32

def hash_value(data:str):
    n = len(data)

    result = 0
    for i in range(n):
        code = ord(data[i]) - ord("a")
        result += code * A ** (n - i - 1)

    return result % M

def find_other(data:str):
    # TODO returns a different string with the same hash value
    hash_val = hash_value(data)
    x = 1

    while True: # add more layer for loop
        shifted_val = hash_val + (M*x) # M mod same with 'result'
        new_string = ""

        while shifted_val > 0:
            remainder = shifted_val % A 
            new_letter = chr(remainder + ord("a")) # inverse of 'code'
            new_string += new_letter
            shifted_val //= A # more division by A^() 
        # all letter added from Cn-1
            reversed_string = new_string[::-1]
            if hash_value(reversed_string) == hash_val:
                if reversed_string != data:
                    return new_string[::-1]
                else:
                    x += 1




if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682