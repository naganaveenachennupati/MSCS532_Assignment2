"""
MSCS 532 - Assignment 2
Naga Naveena Chennupati

Merge Sort implementation using the divide-and-conquer approach.
"""


def merge_sort(values):
    """Sort and return the values in ascending order using Merge Sort."""

    # A list with 0 or 1 element is already sorted.
    if len(values) <= 1:
        return values.copy()

    # Divide the list into two halves.
    midpoint = len(values) // 2
    left_half = values[:midpoint]
    right_half = values[midpoint:]

    # Recursively sort both halves.
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the two sorted halves.
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """Merge two sorted lists into one sorted list."""

    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any values that are left over.
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def main():
    sample_values = [38, 27, 43, 3, 9, 82, 10]

    print("Original values:")
    print(sample_values)

    sorted_values = merge_sort(sample_values)

    print("\nValues after Merge Sort:")
    print(sorted_values)


if __name__ == "__main__":
    main()