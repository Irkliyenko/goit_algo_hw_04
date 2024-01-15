**Performance Analysis of Sorting Algorithms**

In this analysis, I compared the performance of four sorting algorithms: Insertion Sort, Merge Sort, and Python's Timsort (used in the sorted() function and .sort() method). Two different list sizes were used for the tests: a small list (ls1) with 1000 elements and a medium-sized list (ls2) with 10000 elements.

**Table 1: Sorting Performance on Different List Sizes**

| Algorithm        | Time Small Dataset | Time Medium Dataset |
| ---------------- | ------------------ | ------------------- |
| Insertion Sort   | 0.09627            | 5.11667             |
| Merge Sort       | 0.01112            | 0.07008             |
| Timsort (sorted) | 0.00050            | 0.00394             |
| Timsort (.sort)  | 0.00007            | 0.00087             |

The initial test (Table 1) was conducted to evaluate the performance of each algorithm directly on the lists. The results indicate that Timsort (both sorted() and .sort()) significantly outperforms both Insertion Sort and Merge Sort. This efficiency can be attributed to Timsort's sophisticated design, which is a hybrid of Insertion Sort and Merge Sort, optimized for real-world data.

Following the initial analysis, a second test was conducted to examine the consistency of the algorithm performances with a larger dataset. This time, the list size was increased to 20000 elements. The results of this extended test are consistent with the findings from the first test, reaffirming the performance characteristics of each algorithm.

**Table 2: Extended Test with Larger Dataset**

| Algorithm        | Time Small Dataset | Time Large Dataset |
| ---------------- | ------------------ | ------------------ |
| Insertion Sort   | 0.10045            | 20.41727           |
| Merge Sort       | 0.01089            | 0.15047            |
| Timsort (sorted) | 0.00048            | 0.00848            |
| Timsort (.sort)  | 0.00007            | 0.00188            |

The extended test further validates the superior performance of Timsort for larger datasets. Timsort, both in its sorted() and .sort() implementations, significantly outperforms traditional sorting algorithms like Insertion Sort and Merge Sort, especially as the size of the dataset increases. The Insertion Sort, while simple, shows a marked increase in time consumption with the larger dataset, reflecting its O(n^2) complexity. Merge Sort maintains its O(n log n) performance but is still outpaced by the optimizations present in Timsort.

These findings underscore the importance of algorithm selection in handling large datasets. For smaller datasets, the choice of sorting algorithm may have a negligible impact on performance, but for larger datasets, an efficient algorithm like Timsort can offer substantial improvements in execution time.
