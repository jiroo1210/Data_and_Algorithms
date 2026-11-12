def count_substrings(data:str):
    # TODO count distinct substrings
    # [a-z], len(input) ~= 20
    n = len(data)
    final_set = set()
    for i in range(n):
        for j in range(i+1,n+1):
            final_set.add(data[i:j])

    return len(final_set) 
if __name__ == "__main__":
    print(count_substrings("aaaa")) # 4
    print(count_substrings("abab")) # 7
    print(count_substrings("abcd")) # 10
    print(count_substrings("abbbbbb")) # 13
    print(count_substrings("aybabtu")) # 26
    print(count_substrings("saippuakauppias")) # 110