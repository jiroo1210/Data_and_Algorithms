class MaxList: # use mode example
    def __init__(self):
        # TODO maintain list of numbers
        self.list = []
        self.max_num = 0

    def append(self, number):
        # TODO add number to the list
        self.list.append(number)
        self.max_num = max(self.max_num, number)

    def max(self):
        # TODO return max number
        return self.max_num

if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max()) # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max()) # 8
    numbers = MaxList()
    total = 0
    for i in range(10**5):
        numbers.append(i * 999983 % 10**9)
        total += numbers.max()
    print(total) # 99498381797517