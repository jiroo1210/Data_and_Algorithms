def create_string(pages):
    pages = sorted(pages)
    ranges = []

    def string_helper(pre,suf):
        if pre==suf:
            return str(pre)
        else:
            return str(pre) + '-' + str(suf)
    pre = suf = pages[0]

    for page in pages:
        if page <= pre + 1: # need to conside same element repeated
            suf = page # extend
        else:
            ranges.append(string_helper(pre, suf))
            pre = suf = page # reset

    return ','.join(ranges)

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