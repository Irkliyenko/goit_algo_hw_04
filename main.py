import timeit
import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort

if __name__ == '__main__':
    # Generate random list of 1000 elements
    small_list = [random.randint(0, 1000) for _ in range(1000)]
    medium_list = [random.randint(0, 20000) for _ in range(20000)]

    insertion_sort_small_time = timeit.timeit(
        lambda: insertion_sort(small_list), number=10)
    merge_sort_small_time = timeit.timeit(
        lambda: merge_sort(small_list), number=10)
    timsort_sorted_small_time = timeit.timeit(
        lambda: sorted(small_list), number=10)
    timsort_sort_small_time = timeit.timeit(
        lambda: small_list.sort(), number=10)

    insertion_sort_medium_time = timeit.timeit(
        lambda: insertion_sort(medium_list), number=5)
    merge_sort_medium_time = timeit.timeit(
        lambda: merge_sort(medium_list), number=5)
    timsort_sorted_medium_time = timeit.timeit(
        lambda: sorted(medium_list), number=5)
    timsort_sort_medium_time = timeit.timeit(
        lambda: medium_list.sort(), number=5)

    print(f' {"Algorithm": <20} | {"Time small dataset": <20} | {"Time medium dataset": <20}')
    print(f'|{"-"*20} | {"-"*20} | {"-"*20} |')
    print(f'|{"Insertion sort":<20} | {insertion_sort_small_time: <20.5f} | {insertion_sort_medium_time: <20.5f} |')
    print(f'|{"Merge sort":<20} | {merge_sort_small_time: <20.5f} | {merge_sort_medium_time: <20.5f} |')
    print(f'|{"Timsort sorted":<20} | {timsort_sorted_small_time: <20.5f} | {timsort_sorted_medium_time: <20.5f} |')
    print(f'|{"Timsort sort":<20} | {timsort_sort_small_time: <20.5f} | {timsort_sort_medium_time: <20.5f} |')
