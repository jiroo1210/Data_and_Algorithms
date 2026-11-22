def count_substrings(data:str):
    # TODO count distinct substrings
    # [a-z], len(input) ~= 20
    n = len(data)
    final_set = set()
    for i in range(n):
        for j in range(i+1,n+1):
            final_set.add(data[i:j])

    return len(final_set) 

""" model solution was similar to my soultion.
    Instead, AI suggested solution

from itertools import pairwise

def count_substrings(data: str) -> int:
    n = len(data)
    suffixes = sorted(data[i:] for i in range(n)) # Sorts all suffixes lexicographically
    
    duplicates = 0
    for s1, s2 in pairwise(suffixes):
        lcp = 0 # Longest Common Prefix length
        while lcp < len(s1) and lcp < len(s2) and s1[lcp] == s2[lcp]:
            lcp += 1
        duplicates += lcp
        
    return (n * (n + 1)) // 2 - duplicates # Total number of substrings - duplicate substrings

"""
if __name__ == "__main__":
    print(count_substrings("aaaa")) # 4
    print(count_substrings("abab")) # 7
    print(count_substrings("abcd")) # 10
    print(count_substrings("abbbbbb")) # 13
    print(count_substrings("aybabtu")) # 26
    print(count_substrings("saippuakauppias")) # 110