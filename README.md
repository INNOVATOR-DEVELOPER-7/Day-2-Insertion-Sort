# Day-2-Insertion-Sort
Here Python Program for Insertion Sort. Day 2 of Day 365.
- Concept: Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort or mergesort.

- Steps:
    1. Start with the first element: Consider the first element of the list as sorted.
    2. Pick the next element: Move to the next element and insert it into the sorted part of the list.
    3. Compare with sorted elements:
        - Compare the picked element with each element in the sorted part of the list (from right to left).
        - If the picked element is smaller, shift the sorted elements to the right.
    4. Insert the element: Place the picked element at the correct position.
    5. Repeat: Repeat steps 2-4 until all elements are sorted.

- Characteristics:
    - Simple and easy to understand.
    - Efficient for small data sets or nearly sorted data.
    - Has a time complexity of O(n^2) in the worst case and O(n) in the best case.
    - It is stable, meaning that it does not change the relative order of elements with equal keys.


```
List: [5, 3, 8, 4, 2]

Pass 1:
[5, 3, 8, 4, 2] -> (5) is already sorted

Pass 2:
[3, 5, 8, 4, 2] -> (3) is inserted before (5)

Pass 3:
[3, 5, 8, 4, 2] -> (8) is already in its correct position

Pass 4:
[3, 4, 5, 8, 2] -> (4) is inserted between (3) and (5)

Pass 5:
[2, 3, 4, 5, 8] -> (2) is inserted at the beginning
```
