class RepeatList:
    def __init__(self):
        # TODO maintain list of numbers; bool if repetition happend
        self.list = [] # adding tupple is not good
        self.occurence = {}
        self.repeated = False
    def append(self, number:int):
        # TODO add number to the list
        if number not in self.occurence:
            self.occurence[number] = 0
        self.occurence[number] += 1
        if self.occurence[number] > 1:
            self.repeated = True
        self.list.append(number)
        
    def repeat(self):
        # TODO retrun if any of them are repeated
        return self.repeated

if __name__ == "__main__":
    numbers = RepeatList()

    print(numbers.repeat()) # False

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.repeat()) # False

    numbers.append(2)
    print(numbers.repeat()) # True

    numbers.append(5)
    print(numbers.repeat()) # True

    numbers = RepeatList()
    total = 0
    for i in range(10**5):
        numbers.append(i * 999983 % 12345)
        if numbers.repeat():
            total += 1
    print(total) # 87655
    