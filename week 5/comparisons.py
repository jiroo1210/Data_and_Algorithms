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
    def indices_merge(left,right):
        merged = []
        i = j  = 0
        # left and right will build from len 1 to len n//2 each
        while i < len(left) and j < len(right):
            if comparer.smaller(left[i],right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # if len(l or r) % 2 != 0, one element will be left on last iteration
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged # now each index has "order" of smallest to largest

    # initial input "identity matrix"
    identity_indices = [x for x in range(n)] 

    # the answer key to smallest to largest
    sorted_indices = indices_sort(identity_indices)

    # return a new list, [1 to n] as in sorted indices
    answer = [1]*n # index starts at 0, so need to add 1 to all
    # order of smallest to largest
    # index of comparer.numbers
    for order, index in enumerate(sorted_indices): 
        answer[index] += order
    
    return answer


    

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