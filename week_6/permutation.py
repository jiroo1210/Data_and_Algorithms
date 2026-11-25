
""" # old solution
class PermutationTracker:
    def __init__(self):
        # TODO contains a list
        
        self.set = set()
        self.max = 0 # keep track of n from[1,..,n]
        self.repeated = False

    def append(self, number):
        # TODO add number to internal list
        # but don't need to check permutation each time I add
        if self.repeated:
            return
        if number in self.set:
            self.repeated = True
            return
        self.set.add(number)
        self.max = max(self.max, number) # new max
        
    
    def check(self): # only check permutation when .check() is called
        # more efficient
        # TODO return if list if permutation
        if self.repeated:
            return False
        return self.max == len(self.set) # len(range(1,n+1))
"""

""" # model solution
class PermutationTracker:
    def __init__(self):
        self.numbers = set()
        self.count = 0
        self.min = None
        self.max = None

    def append(self, number):
        self.numbers.add(number)
        self.count += 1

        if self.count == 1:
            self.min = self.max = number
        else:
            self.min = min(self.min, number)
            self.max = max(self.max, number)

    def check(self):
        if self.count != len(self.numbers):
            return False
        if self.min != 1 or self.max != self.count:
            return False
        return True
"""
class PermutationTracker:
    def __init__(self):
        # TODO contains a list
        
        self.set = set()
        self.min_val = float('-inf')
        self.max_val = 0 # keep track of n from[1,..,n]
        self.broken = False

    def append(self, number):
        # TODO add number to internal list
        # but don't need to check permutation each time I add
        if number < 1:
            self.broken = True
        if self.broken:
            return
        if number in self.set:
            self.broken = True
            return
        self.set.add(number)
        self.max_val = max(self.max_val, number) # new max
        self.min_val = min(self.min_val, number) # new min
        
    
    def check(self): # only check permutation when .check() is called
        # more efficient
        # TODO return if list if permutation
        if self.broken:
            return False
        return self.max_val == len (self.set)

if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False

    tracker = PermutationTracker()
    total = 0
    for i in range(10**5):
        if i%2 == 0:
            tracker.append(i + 2)
        else:
            tracker.append(i)
        if tracker.check():
            total += 1
    print(total) # 50000