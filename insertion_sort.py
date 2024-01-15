def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


if __name__ == '__main__':
    num = [1, 6, 3, 5, 2]
    r = insertion_sort(num)
    print(r)
