import random

def check_overlapping(reservations:list) -> bool:
    # TODO check if reservations overlap
    # reservation in tuple(int,int)
    # check if lowerbound of any is smaller than upper bound
    if len(reservations) < 2:
        return False
    sorted_list = sorted(reservations)
    start = sorted_list[0][0]
    end = sorted_list[0][1]
    for i in range(1,len(reservations)):
        if sorted_list[i][0] <= end:
            if start <= sorted_list[i][0]:
                return True
        start = sorted_list[i][0]
        end = sorted_list[i][1]
        
    return False
     
   
if __name__ == "__main__":
    print(check_overlapping([])) # False
    print(check_overlapping([(1, 3)])) # False
    print(check_overlapping([(4, 7), (1, 2)])) # False
    print(check_overlapping([(4, 7), (1, 5)])) # True
    print(check_overlapping([(1, 1), (2, 2)])) # False
    print(check_overlapping([(1, 1), (1, 1)])) # True
    print(check_overlapping([(2, 3), (5, 5), (3, 4)])) # True
    print(check_overlapping([(2, 3), (5, 5), (1, 4)])) # True
    print(check_overlapping([(2, 3), (5, 5), (1, 5)])) # True

    reservations = [(day, day) for day in range(1, 10**5+1)]
    random.shuffle(reservations)
    print(check_overlapping(reservations)) # False

    reservations.append((42, 1337))
    random.shuffle(reservations)
    print(check_overlapping(reservations)) # True