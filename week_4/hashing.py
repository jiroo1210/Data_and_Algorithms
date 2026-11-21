def hash_value(input:str):
    # TODO find hash value
    # (c_0 A^{n-1} + c_1 A^{n-2} ... + c_{n-1} A^0) mod M
    # A = 23, M = 2^32
    # 
    import string
    alphabet = string.ascii_lowercase
    alp_dict = {s:i for i,s in enumerate(alphabet)}

    n = len(input)
    hash_val = 0
    for i,s in enumerate(input):
        hash_val += alp_dict[s]*23**(n-1-i)
    return hash_val % (2**32)

""" model solution
A = 23
M = 2**32

def hash_value(string):
    n = len(string)

    result = 0
    for i in range(n):
        code = ord(string[i]) - ord("a") # ord() returns the ascii value of a character
        result += code * A ** (n - i - 1)   # this maps alphabet from 0-25 

    return result % M
"""

""" Honer's method
A = 23
M = 2**32
def hash_value(input: str) -> int:
    result = 0
    for char in input:
        result = (result*A + ord(char)- ord("a")) % M
    return result

# odr("a") is taken off because 'a' is assigned value of 0
# each iteration multiplies the previous result by A
# so that first character get A to the power of N-1, second gets N-2 .. and so on
"""

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440