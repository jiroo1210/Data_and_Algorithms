import math

class Comparer:
    def __init__(self, numbers):
        self.numbers = numbers # numbers range from 1..n, in mixed order
        self.counter = 0
        n = len(self.numbers)
        self.bound = n * math.floor(math.log2(n))

    def list_size(self):
        return len(self.numbers)

    def smaller(self, a, b):
        self.counter += 1
        if self.counter > self.bound:
            raise RuntimeError("too many comparisons")
        return self.numbers[a] < self.numbers[b]

def find_list(comparer:Comparer) ->list:
    # TODO implement merge sort 
    n = comparer.list_size()
    import copy
    # returning comparer.numbers caused attribute error
    # don't directly call camparer.numbers
    if n == 0 : return []
    if n == 1: return [1]
    # shallow copy(.copy()) nor deepcopy workeds
    # so hard code for len 0,1?

    # better approach
    # if n <= 1: return list(range(1,n+1))


    # only way to do this is done with a,b both indexes
    # comparer.smaller(a,b) -> True/False
    # comparer.numbers[a] > comparer.numbers[b] or vice versa

    # keep track of this result in separate list?
    # do it like rref(matrice), with identity matrix
    # indentity_index = list(range(n))
    # INDICES
    # follow the "transformation" (marking comparison results)
    # you get "result" (indexes of comparison)
    
    # helper function 1 keep the index "transformation"
    # "transformation" is sort
    # note: plural form of index is indices, not indexes
    def indices_sort(indices):
        # when all index are single list, return
        length = len(indices)
        if length <= 1:
            return indices
        
        m = length//2
        left_sorted = indices_sort(indices[:m])    
        right_sorted = indices_sort(indices[m:])

        return indices_merge(left_sorted,right_sorted)
    
    # merge the list of single index after comparison
    def indices_merge(left,right): # from merge sort example
        merged = []
        i = j  = 0
        # add lesser index to left and bigger index to right
        while i < len(left) and j < len(right):
            if comparer.smaller(left[i],right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # one side is exhausted; the other's remaining items are sorted and
        # larger than everything in merged, so append them with no more comparisons
        merged.extend(left[i:])
        merged.extend(right[j:])
        # checking left or right has last element is not worth the effort
        return merged # now each index has "order" of smallest to largest

    # initial input "identity matrix"
    identity_indices = [x for x in range(n)] 

    # map the "order" of the indices
    sorted_indices = indices_sort(identity_indices)

    # return a new list, [1 to n] as in sorted indices
    answer = [1]*n # index starts at 0, so need to add 1 to all of them
    for order, index in enumerate(sorted_indices): 
        answer[index] += order
    
    return answer

    """ # model solution
    def merge_sort(numbers, comparer):
    if len(numbers) == 1:
        return numbers

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle], comparer)
    right = merge_sort(numbers[middle:], comparer)

    result = []
    while left or right:
        if not right or (left and comparer.smaller(left[0], right[0])):
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    # pop is slow. dont use it
    return result
    # end of def merge_sort

    def find_list(comparer):
        n = comparer.list_size()
        places = merge_sort(list(range(n)), comparer)
        result = [0] * n
        for i in range(n):
            result[places[i]] = i + 1
    return result
    """

    

if __name__ == "__main__":
    comparer = Comparer([3, 1, 2, 4])
    numbers = find_list(comparer)
    print(numbers) # [3, 1, 2, 4]

    comparer = Comparer([1, 6, 2, 5, 3, 4])
    numbers = find_list(comparer)
    print(numbers) # [1, 6, 2, 5, 3, 4]

    comparer = Comparer([1])
    numbers = find_list(comparer)
    print(numbers)