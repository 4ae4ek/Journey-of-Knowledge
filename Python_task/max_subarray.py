def max_sequence(arr):
    max_sum = 0
    for i in range(len(arr)):
        summ = arr[i]
        if summ > max_sum:
            max_sum = summ
        for j in range(i + 1, len(arr)):
            summ += arr[j]
            if summ > max_sum:
                max_sum = summ
        if summ > max_sum:
            max_sum = summ
    return max_sum if max_sum > 0 else 0


def maxSequence(arr):
    max, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0: curr = 0
        if curr > max: max = curr
    return max


def max_sequence_fast(items):
    iter_items = iter(items)
    try:
        temp_sum = next(iter_items)
    except StopIteration:
        temp_sum = 0
    max_sum = temp_sum
    for item in iter_items:
        temp_sum += item
        if item > temp_sum:
            temp_sum = item
        if temp_sum > max_sum:
            max_sum = temp_sum
    return max_sum if max_sum > 0 else 0


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence_fast([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
