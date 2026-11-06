class OccurrenceTracker:
    def __init__(self):
        self.number_count = {}
        self.total_count = {}

    def add_count(self, count):
        if count in self.total_count:
            self.total_count[count] += 1
        else:
            self.total_count[count] = 1

    def remove_count(self, count):
        self.total_count[count] -= 1
        if self.total_count[count] == 0:
            del self.total_count[count]

    def append(self, number):
        if number in self.number_count:
            self.remove_count(self.number_count[number])
            self.number_count[number] += 1
        else:
            self.number_count[number] = 1
        self.add_count(self.number_count[number])

    def count(self):
        return len(self.total_count)