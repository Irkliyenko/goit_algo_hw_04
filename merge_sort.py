def merge_sort(arr):
    # If the array is empty or has one element, it's already sorted.
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves and then merge them.
    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Merge the two halves by comparing their elements and collecting in order.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append remaining elements (if any) from left and right
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


if __name__ == '__main__':
    num = [1, 6, 3, 5, 2]
    r = merge_sort(num)
    print(r)
