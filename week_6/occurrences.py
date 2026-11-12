class OccurrenceTracker:
    def __init__(self):
        # TODO  how many distinct occurrence counts there are
        # for numbers in the list
        # i.e. some occured once, some twice.... -> how many distinct occurences
        self.list=[]
        self.dict = {}

    def append(self, number):
        # TODO add number to the end of the list
        self.list.append(number)
        if number not in self.dict:
            self.dict[number] = 0
        self.dict[number] += 1

    def count(self):
        # TODO return the number of distinct occurrence counts
        # take set of values of self.dict and count its len
        return len(set(self.dict.values()))
    
if __name__ == "__main__":
    tracker = OccurrenceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count()) # 2

    tracker.append(2)
    tracker.append(3)
    print(tracker.count()) # 1

    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count()) # 3

    tracker = OccurrenceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(i % 100 + 1)
        total += tracker.count()
    print(total) # 198901