def count_parts(songs:list)-> int:
    # TODO count sublist with no repeated songs
    # use window method songs[a],songs[b] -> {song:i}
    count = 0
    start = 0
    last_pos = {}
    for cutoff, song in enumerate(songs):
        if song in last_pos and last_pos[song] >= start:
            start = last_pos[song] + 1 # remove old chunk cotaining old song

        last_pos[song] = cutoff

        count += (cutoff - start + 1) # (b-a + 1) from prev tasks

    return  count
""" 
# model solution is too similar;
# AI suggested improvement

def count_parts(songs: list) -> int:
    count = 0
    start = 0
    last_pos = {}
    # using get instead of if condition
    for cutoff, song in enumerate(songs):
    #   index, value  
        prev = last_pos.get(song, -1) # this line replaces the if-check 
        if prev >= start:
            start = prev + 1
            
        last_pos[song] = cutoff
        count += cutoff - start + 1
        
    return count

"""
if __name__ == "__main__":
    print(count_parts([1, 1, 1, 1])) # 4
    print(count_parts([1, 2, 3, 4])) # 10
    print(count_parts([1, 2, 1, 2])) # 7
    print(count_parts([1, 2, 1, 3])) # 8
    print(count_parts([1, 1, 2, 1])) # 6

    songs = [1, 2] * 10**5
    print(count_parts(songs)) # 399999
    songs = list(range(1, 10**5 + 1)) * 2
    print(count_parts(songs)) # 15000050000