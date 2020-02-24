def short_bubble_sort(lst):
    exchange = True
    pass_num = len(lst) - 1
    while pass_num > 0 and exchange:
        exchange = False
        for i in range(pass_num):
            if lst[i] > lst[i+1]:
                exchange = True
                lst[i], lst[i+1] = lst[i+1], lst[i]
        pass_num -= 1

l = [1, 9, 8, 2, 3, 7, 6, 4, 5]
print("\nShort Bubble Sort")
short_bubble_sort(l)
print(l)

def selection_sort(lst):
    N = len(lst)
    for i in range(N):
        min = i
        for j in range(i+1, N):
            if lst[j] < lst[min]:
                min = j
        lst[min], lst[i] = lst[i], lst[min]

l = [1, 9, 8, 2, 3, 7, 6, 4, 5]
print("\nSelection Sort")
selection_sort(l)
print(l)

def selection_sort_1(lst):
    for i in range(len(lst)-1, 0 , -1):
        max = i
        for j in range(i):
            if lst[j] > lst[max]:
                max = j
        lst[max], lst[i] = lst[i], lst[max]

l = [1, 9, 8, 2, 3, 7, 6, 4, 5]
print("\nSelection Sort")
selection_sort_1(l)
print(l)

def insetion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        val = lst[i]
        while j > 0 and val < lst[j-1]:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = val

l = [1, 9, 8, 2, 3, 7, 6, 4, 5]
insetion_sort(l)
print("\nInsertion Sort")
print(l)


def shell_sort(lst):
    sublist_count = len(lst) // 2
    while sublist_count > 0:
        for i in range(sublist_count):
            gap_insertion_sort(lst, i, sublist_count)
        print("After increments of size", sublist_count, "The list is", lst)
        sublist_count = sublist_count // 2

def gap_insertion_sort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):
        val = lst[i]
        j = i
        while j >= gap and val < lst[j - gap]:
            lst[j] = lst[j - gap]
            j -= gap
        lst[j] = val


l = [1, 9, 8, 2, 3, 7, 6, 4, 5]
shell_sort(l)
print("\nShell Sort")
print(l)

def shell_sort_1(lst):
    N = len(lst)
    h = 1
    while h < N / 3:
        h = 3 * h + 1
        # 1, 4, 13, 40, 121, 364, 1093, ...
    while h > 0:
        for i in range(h, N):
            j = i
            while j >= h and lst[j] < lst[j - h]:
                lst[j], lst[j-h] = lst[j-h], lst[j]
                j -= h
        h //= 3

l = [1, 9, 8, 2, 3, 7, 6, 4, 5]
shell_sort_1(l)
print("\nShell Sort")
print(l)


def merge_sort(lst):
    print("Splitting ", lst)
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    print("Merging ", lst)

l = [1, 9, 8, 2, 3, 7, 6, 4, 5]
print("\nMerge Sort")
merge_sort(l)
print(l)

def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)

def quick_sort_helper(lst, first, last):
    if first < last:
        split_pt = partition(lst, first, last)
        print(split_pt, first, last)
        quick_sort_helper(lst, first, split_pt-1)
        quick_sort_helper(lst, split_pt+1, last)

def partition(lst, first, last):
    print("partition")
    pivot = lst[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and lst[left] <= pivot:
            left += 1
        while left <= right and lst[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            lst[left], lst[right] = lst[right], lst[left]
    lst[first], lst[right] = lst[right], lst[first]
    return right

l = [5, 1, 8, 2, 3, 7, 6, 4, 9]
print("\nQuick Sort")
quick_sort(l)
print(l)
