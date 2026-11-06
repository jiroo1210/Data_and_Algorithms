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



if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440