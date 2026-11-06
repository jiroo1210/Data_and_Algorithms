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