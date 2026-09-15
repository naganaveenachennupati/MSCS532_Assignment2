# MSCS 532 - Assignment 2

## Analyzing and Implementing Divide-and-Conquer Algorithms

**Student:** Naga Naveena Chennupati  
**Course:** MSCS 532 - Algorithms and Data Structures  
**Assignment:** Assignment 2

## Overview

This project analyzes and implements two divide-and-conquer sorting algorithms: Merge Sort and Quick Sort. The purpose of the assignment is to compare their theoretical efficiency with their practical performance on different types of input data.

Both algorithms were implemented in Python and tested using sorted, reverse-sorted, and random datasets. Performance was measured using execution time and peak additional Python memory allocation.

## Algorithms

### Merge Sort

Merge Sort divides the input into two halves, recursively sorts each half, and then merges the sorted halves.

Its recurrence relation is:

`T(n) = 2T(n/2) + Θ(n)`

Its running time is `Θ(n log n)` for best, average, and worst cases.

The implementation creates temporary lists during the divide and merge operations, so its auxiliary space requirement is `O(n)`.

### Quick Sort

Quick Sort selects a pivot, partitions the data around the pivot, and recursively sorts the resulting partitions.

This implementation uses a median-of-three pivot selection strategy based on the first, middle, and last elements.

For reasonably balanced partitions, the recurrence is:

`T(n) = 2T(n/2) + Θ(n)`

which gives `Θ(n log n)` performance.

In the worst case, the recurrence becomes:

`T(n) = T(n-1) + Θ(n)`

which gives `Θ(n²)` performance.

Because the implementation rearranges values within the existing list, it requires less additional memory than the Merge Sort implementation.

## Project Files

- `merge_sort.py` - Merge Sort implementation
- `quick_sort.py` - Quick Sort implementation
- `test_algorithms.py` - Correctness tests for both algorithms
- `benchmark.py` - Performance testing for execution time and memory usage
- `generate_graphs.py` - Generates performance graphs from benchmark results
- `requirements.txt` - Python package requirements
- `results/performance_results.csv` - Recorded benchmark results
- `results/execution_time.png` - Execution-time comparison graph
- `results/memory_usage.png` - Memory-usage comparison graph

## Testing

Both algorithms were tested using several input conditions, including:

- empty lists
- single-element lists
- sorted data
- reverse-sorted data
- duplicate values
- negative and positive values
- general unsorted data

Run the correctness tests with:

```bash
python test_algorithms.py