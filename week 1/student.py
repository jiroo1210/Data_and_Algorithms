def check_number(number:int):
    # numbers is 9 in length
    # multiplied by the values 3,7,1,3,7,1,3,7 (l-2-r )
    # If sum(mul*val) % 10 == 0 & numbers[-1] ==0: True. 
    # Otherwise, the check digit is the distance of the sum to the next multiple of 10
    # TODO
    num_str = str(number)
    if len(num_str)!=9:
        return False
    if num_str[0] != '0':
        return False
    check_num = int(num_str[-1])
    new_sum = 0
    for i in range(8):
        if i % 3 == 0:
            new_sum += int(num_str[i]) * 3
        elif i % 3 == 1:
            new_sum += int(num_str[i]) * 7
        else:
            new_sum += int(num_str[i]) * 1
    
    if new_sum % 10 == 0:
        return check_num == 0
    else:
        return (10 - new_sum % 10) == check_num


if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False