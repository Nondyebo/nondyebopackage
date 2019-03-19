def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    '''return sorted(items)'''
    a = items.copy()
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]     # Swap!
    return a

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    len_i = len(items)
    if len_i == 1:
        return items
    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])
    return linear_merge(i1, i2)
def linear_merge(list1, list2):
    mergeList = []
    while len(list1)> 0 and len(list2)> 0:
        if list1[0]<list2[0]:
            mergeList.append(list1[0])
            list1.pop(0)
        else:
            mergeList.append(list2[0])
            list2.pop(0)
        if len(list1)==0:
            mergeList += list2
        elif len(list2)==0:
            mergeList += list1
    return mergeList

def quick_sort(items):
    len_i = len(items)
    index = -1

    if len_i <= 1:

        return items

    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
