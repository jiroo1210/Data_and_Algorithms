def find_distances(street:str):
    # TODO return list with distance to nearest shop, "1"
    # aim for O(2N)
    n = len(street)
    street_map = [n]*n
    dis = n # when dis = 0, [0] position is considered "1" 
    # left to right pass
    for i in range(n):
        if street[i]== "1":
            dis = 0
        else: # else can be removed if street_map[i] = dis is moved above and dis += 1 is moved below it
            dis += 1
        street_map[i] = dis # faster than min(street_map[i], dis) because dis is always increasing

    
    dis = n
    # right to left pass
    for i in range(n-1,-1,-1):
        if street[i] == "1":
            dis = 0
        else:
            dis += 1
        street_map[i] = min(street_map[i], dis)    


    return street_map
    """ model solution
    def find_distances(street):
    length = len(street)
    inf = 10**9 
    # float('inf') is safer but slower than 10**9; 
    # n is good enough for this problem

    result = [inf] * length

    dist = inf
    for pos in range(length):
        if street[pos] == "1": # no need for else
            dist = 0 
        result[pos] = min(result[pos], dist) # distance assigned
        dist += 1 # distance incremented for next iter

    dist = inf
    for pos in range(length - 1, -1, -1):
        if street[pos] == "1":
            dist = 0
        result[pos] = min(result[pos], dist)
        dist += 1

    return result
    """
if __name__ == "__main__":
    print(find_distances("00100010")) # [2, 1, 0, 1, 2, 1, 0, 1]
    print(find_distances("00100000")) # [2, 1, 0, 1, 2, 3, 4, 5]
    print(find_distances("11111111")) # [0, 0, 0, 0, 0, 0, 0, 0]
    print(find_distances("01010101")) # [1, 0, 1, 0, 1, 0, 1, 0]
    print(find_distances("10000000")) # [0, 1, 2, 3, 4, 5, 6, 7]
    print(find_distances("00000001")) # [7, 6, 5, 4, 3, 2, 1, 0]
    print(find_distances("0011")) # [2, 1, 0, 0]

    n = 10**5
    street = "0"*n + "1" + "0"*n
    distances = find_distances(street)
    print(distances[1337]) # 98663