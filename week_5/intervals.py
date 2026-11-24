import random

def count_nested(intervals:list) -> int:
    # TODO takes a list of intervals as a parameter and returns the number of nested intervals
    # plan: sort the list using some tuple key
    
    nested_intervals = 0
    sorted_intervals = sorted(intervals, key =lambda x: (x[0], -x[1]))
    # ascending start, descending end
    # so that
    # sorted_interval[i][0] <= sorted_interval[i+1][0] 
    # sorted_interval[i][1] <= sorted_interval[i+1][1]

    # using the fact that smaller negative number has larger absolute value
    # if the new interval's end is smaller than the previous end, it's nested
    # choose 0 for upperbound
    
    end = float('-inf') # initialization for the end

    for interval in sorted_intervals:
        if interval[1] <= end: # new interval upperbound <= end
            nested_intervals += 1
        else: # initial run will always take this branch
              # also empty or single element list will take this route
            end = interval[1]

    return nested_intervals

    """ # model solution
    def count_nested(intervals):
    def sort_key(interval):
        return (interval[0], -interval[1])

    intervals = sorted(intervals, key=sort_key)

    count = 0
    max_right = 0 # might fail if all intervals are negative

    for left, right in intervals:
        if right <= max_right:
            count += 1
        max_right = max(max_right, right)

    return count
    """
if __name__ == "__main__":
    print(count_nested([])) # 0
    print(count_nested([(1, 2)])) # 0
    print(count_nested([(1, 2), (3, 4)])) # 0
    print(count_nested([(1, 3), (2, 4)])) # 0
    print(count_nested([(1, 4), (2, 3)])) # 1
    print(count_nested([(1, 4), (1, 3)])) # 1
    print(count_nested([(1, 4), (2, 4)])) # 1
    print(count_nested([(1, 1), (1, 2), (1, 3)])) # 2
    print(count_nested([(1, 6), (2, 5), (3, 4)])) # 2
    print(count_nested([(1, 4), (2, 5), (3, 6)])) # 0
    print(count_nested([(538, 788), (693, 771), (634, 738)])) # 2

    intervals = [(x+1, x+3) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 0

    intervals = [(x+1, 2*10**5-x) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 99999