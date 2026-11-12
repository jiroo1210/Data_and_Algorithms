def find_distances(street:str):
    # TODO return list with distance to nearest shop, "1"
    # aim for O(2N)
    n = len(street)
    street_map = [n]*n
    dis = n # when dis = 0, [0] position is considered "1" 

    for i in range(n):
        if street[i]== "1":
            dis = 0
        else:
            dis += 1
        street_map[i] = dis

    
    dis = n


    for i in range(n-1,-1,-1):
        if street[i] == "1":
            dis = 0
        else:
            dis += 1
        street_map[i] = min(street_map[i], dis)    

    return street_map

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