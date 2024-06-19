import random


def isSorted(list):
    if len(list) == 1:
        return True
    return list[0] <= list[1] and isSorted(list[1:])


def bogo_sort(list):
    attempts = 0
    while not isSorted(list):
        random.shuffle(list)
        print(attempts)
        attempts += 1
    return list


alist = [1, 33, 452354, 33, 43, 5453, 200, 4234, 12]

print(alist)
print(bogo_sort(alist))
