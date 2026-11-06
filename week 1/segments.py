def find_segments(data:str):
    # TODO list of tuples, (#, 'char')
    # exceptions for len(data) = 0 or 1
    if not data:
        return []
    if len(data) == 1:
        return [(1,data)]
    final_list = []
    count = 0
    char = ''
    i =0
    while i < len(data):
        if count == 0:
            char = data[i]
            count +=1
            i += 1
        if char == data[i]:
            count +=1
            i += 1
        else:
            final_list.append((count,char))
            count = 0
            i += 1
    final_list.append((count,char))

    return final_list

"""model solution:

import re

def find_segments(data):
    matches = re.findall(r"(([a-z])\2*)", data)
    result = [(len(match[0]), match[1]) for match in matches]
    return result
"""        


if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]
    print(find_segments(''))

    print(find_segments('a'))