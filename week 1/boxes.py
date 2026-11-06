def min_count(product_count, box_size):
    # returns the minimum number of boxes needed to pack product_count items
    return (product_count//box_size + (1 if product_count % box_size != 0 else 0))


if __name__ == "__main__":
    print(min_count(10, 3)) # 4
    print(min_count(10, 4)) # 3
    print(min_count(100, 1)) # 100
    print(min_count(100, 100)) # 1
    print(min_count(100, 99)) # 2
    print(min_count(5, 5)) # 1
    print(min_count(5, 6)) # 1