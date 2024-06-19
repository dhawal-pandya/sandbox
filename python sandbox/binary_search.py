def binary_search(li, target):
    if len(li) == 1:
        if li[0] == target:
            return 0

    first = 0
    last = len(li) - 1

    while first <= last:
        mid = (first + last) // 2

        if li[mid] == target:
            return mid
        elif li[mid] > target:
            last = mid - 1
        else:
            first = mid + 1

    return None


# Test

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(binary_search(new_list, 10))

# Gyaan
