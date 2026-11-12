class ChangeList:
    def __init__(self):
        # TODO maintains a list of numbers
        self.list = []
        self.changes = [] # @ same index, mark changes
        self.delta = 0

    def append(self, number):
        # TODO add number to the end of the list
        n = len(self.list) # index upto n-1
        self.list.append(number) # index n filled
        self.changes.append(-self.delta) # no changes so far

    def get(self, index):
        # TODO access a number on the list
        return self.list[index] + self.changes[index] + self.delta

    def change_all(self, amount):
        # TODO increment all list numbers by amount
        self.delta += amount


if __name__ == "__main__":
    numbers = ChangeList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)

    print(numbers.get(0)) # 1
    print(numbers.get(1)) # 2
    print(numbers.get(2)) # 3

    numbers.change_all(2)
    print(numbers.get(0)) # 3
    print(numbers.get(1)) # 4
    print(numbers.get(2)) # 5

    numbers.append(8)
    numbers.change_all(-1)
    print(numbers.get(0)) # 2
    print(numbers.get(1)) # 3
    print(numbers.get(2)) # 4
    print(numbers.get(3)) # 7

    numbers = ChangeList()
    total = 0
    for i in range(10**5):
        numbers.append(i + 1)
        numbers.change_all(i % 11 - 5)
        total += numbers.get(i // 2)
    print(total) # 2500049970