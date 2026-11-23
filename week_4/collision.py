
# using model solution from prev. task
A = 23
M = 2**32

def hash_value(string):
    n = len(string)

    result = 0
    for i in range(n):
        code = ord(string[i]) - ord("a") # ord() returns the ascii value of a character
        result += code * A ** (n - i - 1)   # this maps alphabet from 0-25 

    return result % M
""" # old solution
    # while True: is not safe, it can cause infinite loop
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
            new_string = new_letter + new_string # += new_letter causes string reversal
            shifted_val //= A # more division by A^() 
            if hash_value(new_string) == hash_val:
                if new_string != data:
                    return new_string
                else:
                    x += 1
"""
def create_string(hash_val):
    new_string = "" 
    while hash_val > 0: # reverse of hash_value(string)
        new_string = chr(ord("a") + hash_val % A) + new_string
        hash_val //= A
    return new_string

def find_other(data:str):
    # TODO returns a different string with the same hash value
    hash_val = hash_value(data)
    new_string = create_string(hash_val + M)

    return new_string if new_string != data else create_string(hash_val + 2*M)
    # need second candidate for the case that new_string == data
    # return new_string or create_string(hash_val + 2*M) will work recursively 
    # as it calls itself until new_string != data

""" # model solution
def create_string(hash_sum):
    string = ""
    while hash_sum > 0:
        string = chr(ord("a") + hash_sum % A) + string
        hash_sum //= A
    return string

def find_other(string):
    hash = hash_value(string)
    string1 = create_string(hash)
    string2 = create_string(hash + M)

    return string1 if string1 != string else string2

"""


if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682