class DistanceTracker:
    def __init__(self):
        # TODO 1. maintains a list of numbers 
        # TODO 2. efficiently computing the sum of distances 
        #           between all pairs of occurrences of a given number
        
        self.list = []
        self.dict = {}
        self.next_idx = 0 # for indexing

        # total distance = old_distance + new_distance = old_sum + pos*frequency - sum_of_indices
        # keep track of [old_sum, frequency, sum_of_indices] in dict as values and update them

    def append(self, number):
        # TODO add number to the end of the "list"
        self.list.append(number)
        new_entry = self.dict.get(number) # entry is None
        if new_entry is None:
            self.dict[number] = [0,1,self.next_idx]# old_sum, freq, sum_of_indices

        self.dict[number][0] += self.next_idx*self.dict[number][1]-self.dict[number][2]
        self.dict[number][1] += 1 # freq
        self.dict[number][2] += self.next_idx # sum_of_indices
        self.next_idx += 1 # this will be the index for next element
        
    def sum(self, number):
        # TODO return the sum of distances for number

        if number not in self.dict:
            return 0
        return self.dict[number][0]

""" 2nd old solution - but functional
class DistanceTracker:
    def __init__(self):
        # TODO maintains a list of numbers 
        # efficiently computing the sum of distances 
        # between all pairs of occurrences of a given number
        self.list = []
        self.dict = {}
        self.count = 0 # for indexing

        # list of indices L
        # new position, pos
        # new distance = sum(pos - i for i in L)
        # = pos*(len(L)) - sum(L)
        # total distance = new + old
        # = old_sum + pos*(Len(L)) - sum L
        # Len(L) is O(1), but sum(L) is O(n)
        # task ask for O(1)
        # keep track of old_sum, len(L), sum(L)
        # do not keep L, but just update the 3 values?

    def append(self, number):
        # TODO add number to the end of the "list"
        self.list.append(number)
        if number not in self.dict:
            self.dict[number] = [0,0,0] 
        self.dict[number][1] += 1 # length
        self.dict[number][2] += self.count # sum
        self.dict[number][0] += self.count*self.dict[number][1]\
                                - self.dict[number][2] # old_sum += new_distance
        self.count += 1 # this will be the index for next element
        
    def sum(self, number):
        # TODO return the sum of distances for number

        if number not in self.dict:
            return 0
        return self.dict[number][0]
"""

"""
    # old version: O(n^2)
    
    def sum(self, number):
        # TODO return the sum of distances for number
        sum = 0
        if number not in self.dict:
            return 0
        if len(self.dict[number]) <= 1:
            return 0
        for i in range(len(self.dict[number])):
            j = i
            while j < len(self.dict[number]):
                sum += self.dict[number][j]-\
                    self.dict[number][i]
                j += 1
        
        return sum
    
"""
""" # model solution
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


if __name__ == "__main__":  
    tracker = DistanceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    tracker.append(3)
    tracker.append(1)
    tracker.append(2)
    tracker.append(1)

    print(tracker.sum(1)) # 24
    print(tracker.sum(2)) # 5
    print(tracker.sum(3)) # 1

    tracker.append(1)
    tracker.append(2)
    tracker.append(3)

    print(tracker.sum(1)) # 42
    print(tracker.sum(2)) # 16
    print(tracker.sum(3)) # 14

    tracker = DistanceTracker()
    print(tracker.sum(1)) # 0
    tracker.append(1)
    print(tracker.sum(1)) # 0

    tracker = DistanceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(1)
        total += tracker.sum(1)
    print(total) # 4166749999583325000