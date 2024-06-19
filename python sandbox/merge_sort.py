def merge_sort(list):
    if len(list) <= 1:
        return list

    left_list, right_list = split_list(list)
    # assume this function split_list is already written (afaw)
    l = merge_sort(left_list)
    r = merge_sort(right_list)

    sorted_list = merge(l, r)  # afaw

    return sorted_list


def split_list(list):
    midpoint = len(list) // 2

    l = list[:midpoint]
    r = list[midpoint:]

    return l, r


def merge(l, r):
    p, q = 0, 0

    sorted_l = []

    # remeber merge sort is dumb, it literally arranges each element, so write that
    while p < len(l) and q < len(r):
        if l[p] < r[q]:
            sorted_l.append(l[p])
            p += 1
        else:
            sorted_l.append(r[q])
            q += 1

    while p < len(l):
        sorted_l.append(l[p])
        p += 1
    while q < len(r):
        sorted_l.append(r[q])
        q += 1

    return sorted_l


def verify_sorted(list):
    if len(list) <= 1:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])


# Test

alist = [11, 33, 22, 55, 66, 77, 99, 77, 87, 88, 32, 43, 76]

print(verify_sorted(alist))
print(verify_sorted(merge_sort(alist)))

# Gyaan

"""
Why is merge sort called efficient, it literally arranges each element multiple times?

Merge sort is considered efficient due to its optimal time complexity for sorting large lists or arrays. Although it may seem inefficient because it arranges each element multiple times during the merge phase, its divide-and-conquer approach results in a time complexity of O(n log n) in the average and worst-case scenarios.

Here's why merge sort is considered efficient:

Optimal Time Complexity: Merge sort divides the array into smaller subarrays until each subarray consists of one or zero elements (base case). Then, it merges these sorted subarrays back together. The key to its efficiency is that the merge operation combines two sorted arrays into a single sorted array in linear time. As a result, the overall time complexity of merge sort is O(n log n), which is optimal for comparison-based sorting algorithms.

Stable Sorting: Merge sort is a stable sorting algorithm, meaning it preserves the relative order of equal elements. This property is valuable in certain applications and ensures predictable behavior.

Consistent Performance: Unlike some other sorting algorithms, such as quicksort, which can have worst-case time complexities of O(n^2) under certain conditions, merge sort guarantees O(n log n) time complexity regardless of the input data. This consistency makes it a reliable choice for sorting large datasets.

Parallelizable: Merge sort is inherently parallelizable, as the merging of sorted subarrays can be performed independently. This characteristic allows for efficient parallel implementations, making merge sort suitable for parallel computing environments.

While merge sort may involve rearranging elements multiple times during the merging phase, its overall efficiency and predictability make it a popular choice for sorting large datasets in practice. 
"""
