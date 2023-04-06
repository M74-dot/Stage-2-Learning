import bisect


def binary_insertion_sort(lst):

    for i in range(1, len(lst)):
        val = lst[i]
        j = bisect.bisect_left(lst, val, 0, i)
        lst[j+1:i+1] = lst[j:i]
        lst[j] = val
    return lst
