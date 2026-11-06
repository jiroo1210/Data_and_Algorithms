def merge_sort(arr):
    # Base case: A list of zero or one elements is already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle index
    mid = len(arr) // 2
    
    # Divide the array into two halves using slicing
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Call our helper function to stitch them back together
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    i = 0  # Pointer for the left list
    j = 0  # Pointer for the right list
    
    # Traverse both lists, comparing elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    # At this point, one of the lists might still have elements left over.
    # We append any remaining elements directly to the end.
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

# Test array
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(my_list)

print(f"Original: {my_list}")
print(f"Sorted:   {sorted_list}")