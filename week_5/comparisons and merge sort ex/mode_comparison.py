def find_mode(numbers):
    count = {}
    mode = (0, 0)

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        mode = max(mode, (count[x], x))

    return mode[1]

def find_mode_sort(numbers):
    
    sorted_numbers = sorted(numbers)
    count = [sorted_numbers[0],0]
    mode = (sorted_numbers[0],0)

    for x in sorted_numbers:
        if x == count[0]:
            count[1] += 1
        if count[1] >= mode[1]:
            mode = count[0],count[1]
    
    return mode[1]


if __name__ == "__main__":
    import time
    import random
    n = 10**7
    numbers = [random.randint(1, 1000) for _ in range(n)]
    start_time = time.time()
    find_mode(numbers)
    end_time = time.time()
    print(end_time - start_time)
    
    start_time = time.time()
    find_mode_sort(numbers)
    end_time = time.time()
    print(end_time - start_time)
    