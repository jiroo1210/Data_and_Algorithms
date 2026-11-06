class SumList:
    def __init__(self):
        # TODO maintains a list of numbers
        self.list = []
        self.sum_upto = [0]

    def append(self, number):
        # TODO add number to the end of the list
        self.list.append(number)
        self.sum_upto.append(self.sum_upto[-1] + number) 
        # self.sum_upto[x] will give sum(self.list[:x]) upto x-1 term
        


    def sum(self, a, b):
        # TODO return the sum of the numbers from the position a to the position b
        return self.sum_upto[b+1] - self.sum_upto[a] # sum(self.list[:b]) - sum(self.list[:a-1])
    
if __name__ == "__main__":
    numbers = SumList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    numbers.append(4)
    numbers.append(5)

    print(numbers.sum(0, 4)) # 15
    print(numbers.sum(1, 1)) # 2
    print(numbers.sum(1, 3)) # 9
    print(numbers.sum(2, 3)) # 7
    print(numbers.sum(0, 3)) # 10

    numbers.append(1)
    print(numbers.sum(0, 5)) # 16
    print(numbers.sum(5, 5)) # 1

    numbers = SumList()
    total = 0
    for i in range(10**5):
        numbers.append(i + 1)
        total += numbers.sum(i // 2, i)
    print(total) # 125005000050000