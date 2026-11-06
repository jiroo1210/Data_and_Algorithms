import random

def count_nested(intervals:list) -> int:
    # TODO takes a list of intervals as a parameter and returns the number of nested intervals
    # plan: sort the list using some tuple key
    if not intervals:
        return 0
    if len(intervals) == 1:
        return 0
    nested_intervals = 0
    sorted_intervals = sorted(intervals, key =lambda x: (x[0], -x[1]))
    # ascending start, descending end
    # then for all interval[i][0] <= interval[i+1][0] 
    # and only need to check if interval[i+1][1] <= interval[i][1]
    # need to choose big end, but i=0, end = sorted_intervals[0][1] takes extra count
    # make the iteration go else: that end is sorted_intervals[0][1] for i = 1
    # choose -inf for upperbound
    
    end = float('-inf')
    for interval in sorted_intervals:
        if interval[1] <= end: # new interval upperbound <= end
            nested_intervals += 1
        else: # end is not nested
            end = interval[1]


    return nested_intervals
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