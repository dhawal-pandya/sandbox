def insertion_sort(list):
    for i in range(1, len(list)):
        curr = list[i]
        j = i - 1
        while j >= 0 and curr < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = curr
    return list


def verify_sorted(list):
    if len(list) <= 1:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])


# Test

alist = [11, 33, 22, 55, 66, 77, 99, 77, 87, 88, 32, 43, 76]

print(verify_sorted(alist))
print(verify_sorted(insertion_sort(alist)))
