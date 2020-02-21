def binary_search(lst, item):
    lo = 0
    hi = len(lst) - 1
    found = False

    while lo <= hi and not found:
        mid = lo + (hi-lo) // 2
        if lst[mid] == item:
            found = True
        elif lst[mid] < item:
            lo = mid + 1
        else:
            hi = mid - 1
    return found

def binary_search_rec0(lst, item):
    if len(lst) == 0:
        return False

    mid = len(lst) // 2
    if lst[mid] == item:
        return True
    elif lst[mid] < item:
        return binary_search_rec0(lst[mid+1:], item)
    else:
        return binary_search_rec0(lst[:mid], item)

def binary_search_rec(lst, item, lo, hi):
    if lo > hi:
        return False

    mid = lo + (hi-lo) // 2
    if lst[mid] == item:
        return True
    elif lst[mid] < item:
        return binary_search_rec(lst, item, mid+1, hi)
    else:
        return binary_search_rec(lst, item, lo, mid)

test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(test_list, 2))
print(binary_search(test_list, 12))
print(binary_search_rec0(test_list, 2))
print(binary_search_rec0(test_list, 12))
print(binary_search_rec(test_list, 2, 0, len(test_list)-1))
print(binary_search_rec(test_list, 12, 0, len(test_list)-1))