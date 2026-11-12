def count_rounds(numbers):
    n = len(numbers)
    
    rounds = 1
    for i in range(1, n):
        if numbers.index(i + 1) < numbers.index(i):
            rounds += 1
            
    return rounds

# using model solution

def count_rounds_2(numbers):
    n = len(numbers)
    pos = [0] * (n+1)

    for i in range(n):
        pos[numbers[i]] = i

    rounds = 1
    for number in range(2, n+1):
        if pos[number] < pos[number - 1]:
            rounds += 1

    return rounds

if __name__ == "__main__":
    import time
    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    start_time = time.time()
    count_rounds(numbers)
    end_time = time.time()
    print(round(end_time - start_time, 4))

    start_time = time.time()
    count_rounds_2(numbers)
    end_time = time.time()
    print(round(end_time - start_time, 4))