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
        sum = 0
        if number not in self.dict:
            return 0
        return self.dict[number][0]
    
    # old version: O(n^2)
    """
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