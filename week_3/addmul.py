def evaluate(data:str):
    # TODO evaluate strings
    import re
    # re string, \( for literal, \d for any digit, + for 1 or more repetition
    # 01 should not be processed, replace with [1-9]\d*

    pattern_mul = r"mul\(([1-9]\d*),([1-9]\d*)\)" # any number of digits, but not starting with 0
    pattern_sum = r"add\(([1-9]\d*),([1-9]\d*)\)"

# use two helper function

    new_data = re.sub(pattern_mul, multiply_str, data)
    final_data = re.sub(pattern_sum, sum_str, new_data)

    return final_data

# # use match object from re.search
# use .group() to extract the text from the match object

def multiply_str(match):
    num_1 = int(match.group(1)) # index start from 1; 1st matched group
    num_2 = int(match.group(2)) # 2nd matched group
    
    if num_1 > 0 and num_2 >0:
        return str(num_1*num_2)
    else:
        return match.group()
# first halves are same. can be merged.
def sum_str(match):
    num_1 = int(match.group(1)) # index start from 1; 1st matched group
    num_2 = int(match.group(2)) # 2nd matched group
    if num_1 > 0 and num_2 >0:
        return str(num_1 + num_2)
    else:
        return match.group()

""" model solution #1
import re

def evaluate(data):
    result = ""
    pos = 0

    regex = r"(add|mul)\(([1-9][0-9]*),([1-9][0-9]*)\)"

    for match in re.finditer(regex, data):
        operation = match.group(1)
        left = int(match.group(2))
        right = int(match.group(3))

        result += data[pos:match.start()]

        if operation == "add":
            result += str(left + right)
        if operation == "mul":
            result += str(left * right)

        pos = match.end()

    return result + data[pos:]
"""
""" model solution #2 # similar to my solution, but more concise
import re

def calc(match):
    operation = match.group(1)
    left = int(match.group(2))
    right = int(match.group(3))

    if operation == "add":
        return str(left + right)
    if operation == "mul":
        return str(left * right)

def evaluate(data):
    regex = r"(add|mul)\(([1-9][0-9]*),([1-9][0-9]*)\)"
    return re.sub(regex, calc, data)
"""
if __name__ == "__main__":
    print(evaluate("add(1,2)")) # 3
    print(evaluate("aybabtu")) # aybabtu
    print(evaluate("mul(6,7),mul(7,191)")) # 42,1337
    print(evaluate("abadd(123,456)mulxmul(3,13)")) # ab579mulx39
    print(evaluate("mul()mul(13)mul(0,1)")) # mul()mul(13)mul(0,1)
    print(evaluate("mul(585,600)add(794,845)mul(393,651)mul(944,316)mul(714,210)")) # 3510001639255843298304149940
    print(evaluate("add()add(5)add(0,1)add(1,0)add(1,-1)add(-1,1)add(1, 2)add(1.5,2)add(01,2)")) # add()add(5)add(0,1)add(1,0)add(1,-1)add(-1,1)add(1, 2)add(1.5,2)add(01,2)
    print(evaluate("mul(585,600)add(794,845)mul(393,651)mul(944,316)mul(714,210)")) #3510001639255843298304149940
    data = "mul(6,7)"*10**5
    result = evaluate(data)
    print(len(result)) # 200000
    print(result[:20]) # 42424242424242424242