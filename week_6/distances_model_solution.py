class DistanceTracker:
    def __init__(self):
        self.pos = 0
        self.count = {}
        self.last_pos = {}
        self.last_sum = {}
        self.total_sum = {}

    def append(self, number):
        if number in self.count:
            add = self.count[number] * (self.pos - self.last_pos[number])
            self.count[number] += 1
            self.last_sum[number] += add
            self.total_sum[number] += self.last_sum[number]
        else:
            self.count[number] = 1
            self.last_sum[number] = 0
            self.total_sum[number] = 0

        self.last_pos[number] = self.pos
        self.pos += 1

    def sum(self, number):
        if number in self.total_sum:
            return self.total_sum[number]
        else:
            return 0
        
    """
    count: how many times the number occurs on the list
    last_pos: what is the last (right-most) position of an occurrence
    last_sum: the sum of distances for occurrence pairs involving last_pos (i.e., the increase in the total sum when the last occurrence was added)
    total_sum: the sum of distances for all occurrence pairs (i.e., the desired answer to the sum query)
    """