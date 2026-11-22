def create_distribution(data:str):
    # TODO {sub string length: count}
    n = len(data)
    data_set = set()
    for i in range(n):
        for j in range(i+1,n+1):
            data_set.add(data[i:j])

    count_dict = {}

    for s in data_set:
        if len(s) not in count_dict:
            count_dict[len(s)] = 0
        count_dict[len(s)] += 1

    return dict(sorted(count_dict.items())) 
    # .items() method to iterate key:value pair

""" model solution is too similar; AI suggested solution

from itertools import pairwise

def create_distribution(data: str) -> dict[int, int]:
    n = len(data)
    suffixes = sorted(data[i:] for i in range(n))
    # (n - K + 1) : total number of substrings of length K
    # dup_diff[k] tracks changes in how many duplicates exist at length k

    dup_diff = [0] * (n + 2)
    for s1, s2 in pairwise(suffixes):
        lcp = 0 # lcp = longest common prefix of s1 and s2
        while lcp < len(s1) and lcp < len(s2) and s1[lcp] == s2[lcp]:
            lcp += 1
        if lcp > 0:
            dup_diff[1] += 1 # start index of duplicate substrings
            dup_diff[lcp + 1] -= 1 # end index of duplicate substrings
    # running sum of dup_diff gives the number of duplicates for each length

    distribution: dict[int, int] = {}
    duplicates = 0
    for length in range(1, n + 1):
        duplicates += dup_diff[length]
        distribution[length] = (n - length + 1) - duplicates
    
    return distribution
"""


if __name__ == "__main__":
    print(create_distribution("aaaa"))
    # {1: 1, 2: 1, 3: 1, 4: 1}
    
    print(create_distribution("abab"))
    # {1: 2, 2: 2, 3: 2, 4: 1}
    
    print(create_distribution("abcd"))
    # {1: 4, 2: 3, 3: 2, 4: 1}

    print(create_distribution("abbbbbb"))
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

    print(create_distribution("aybabtu"))
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}