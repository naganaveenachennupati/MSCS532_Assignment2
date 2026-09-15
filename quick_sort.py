"""
MSCS 532 - Assignment 2
Naga Naveena Chennupati

Quick Sort implementation using the divide-and-conquer approach.
"""


def quick_sort(values, low=0, high=None):
    """Sort the list in ascending order using Quick Sort."""

    if high is None:
        high = len(values) - 1

    if low < high:
        pivot_index = partition(values, low, high)

        # Sort the values on each side of the pivot.
        quick_sort(values, low, pivot_index - 1)
        quick_sort(values, pivot_index + 1, high)

    return values


def partition(values, low, high):
    """Partition the list around a selected pivot."""

    pivot = median_of_three(values, low, high)
    i = low - 1

    for j in range(low, high):
        if values[j] <= pivot:
            i += 1
            values[i], values[j] = values[j], values[i]

    # Put the pivot in its correct position.
    values[i + 1], values[high] = values[high], values[i + 1]

    return i + 1


def median_of_three(values, low, high):
    """Select a pivot using the median of the first, middle, and last values."""

    middle = (low + high) // 2

    if values[low] > values[middle]:
        values[low], values[middle] = values[middle], values[low]

    if values[low] > values[high]:
        values[low], values[high] = values[high], values[low]

    if values[middle] > values[high]:
        values[middle], values[high] = values[high], values[middle]

    # Move the selected pivot to the end for partitioning.
    values[middle], values[high] = values[high], values[middle]

    return values[high]


def main():
    sample_values = [38, 27, 43, 3, 9, 82, 10]

    print("Original values:")
    print(sample_values)

    quick_sort(sample_values)

    print("\nValues after Quick Sort:")
    print(sample_values)


if __name__ == "__main__":
    main()