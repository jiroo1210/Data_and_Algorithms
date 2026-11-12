def create_string(pages:list)->str:
    # TODO group the elements
    s_page = sorted(pages)
    if len(pages) == 1:
        return f"{pages[0]}"
    page_string = ""
    page_list = []
    s_page.insert(0,0)
    temp_string = str(s_page[1])    
    for i in range(1,len(pages)): 
        if s_page[i] +1 == s_page[i+1]:
            if not temp_string:
                temp_string = str(s_page[i])
            temp_string += '-' + str(s_page[i+1])
        elif s_page[i] == s_page[i+1]:
            continue
        elif s_page[i] != s_page[i+1]:
            if not temp_string:
                temp_string = str(s_page[i])
            page_list.append(temp_string)
            temp_string = ""
    if temp_string:
        page_list.append(temp_string)
    
    if str(s_page[-1]) not in page_list[-1]:
        page_list.append(str(s_page[-1]))

    for string in page_list:
        if len(string.split('-')) == 1:
            page_string += string + ','
        else:
            splited = string.split('-')
            page_string += splited[0] + '-' + splited[-1] +','
            
    return page_string.strip(',')



        


if __name__ == "__main__":
    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9
    print(create_string([23, 12, 23])) # 12,23
    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    print(pages) # [3, 2, 1, 3, 2, 1]