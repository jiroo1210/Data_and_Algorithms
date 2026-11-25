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
        # may not be O(1)

""" # model solution was not clear at all.
# more readable version

class OccurrenceTracker:
    def __init__(self):
        # number -> how many times it has appeared
        self.num_to_freq = {}
        # frequency -> how many distinct numbers currently have that frequency
        self.freq_to_num_count = {}

    def append(self, number):
        old_freq = self.num_to_freq.get(number, 0)
        new_freq = old_freq + 1

        # 1. Remove the number from its old frequency bucket
        if old_freq > 0:
            self.freq_to_num_count[old_freq] -= 1
            if self.freq_to_num_count[old_freq] == 0:
                del self.freq_to_num_count[old_freq]

        # 2. Update the number's frequency
        self.num_to_freq[number] = new_freq

        # 3. Add the number to its new frequency bucket
        self.freq_to_num_count[new_freq] = self.freq_to_num_count.get(new_freq, 0) + 1

    def count(self):
        # Number of active frequency buckets
        return len(self.freq_to_num_count)
"""

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