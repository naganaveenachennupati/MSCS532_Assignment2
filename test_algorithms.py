"""
MSCS 532 - Assignment 2
Naga Naveena Chennupati

Tests for the Merge Sort and Quick Sort implementations.
"""

from merge_sort import merge_sort
from quick_sort import quick_sort


def test_merge_sort():
    test_cases = [
        [],
        [10],
        [5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 2, 4, 1, 2],
        [-3, 7, 0, -1, 5],
        [38, 27, 43, 3, 9, 82, 10],
    ]

    for values in test_cases:
        expected = sorted(values)
        result = merge_sort(values)
        assert result == expected, f"Merge Sort failed for {values}"

    print("All Merge Sort tests passed successfully.")


def test_quick_sort():
    test_cases = [
        [],
        [10],
        [5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 2, 4, 1, 2],
        [-3, 7, 0, -1, 5],
        [38, 27, 43, 3, 9, 82, 10],
    ]

    for values in test_cases:
        expected = sorted(values)

        # Quick Sort changes the list directly, so use a copy.
        result = values.copy()
        quick_sort(result)

        assert result == expected, f"Quick Sort failed for {values}"

    print("All Quick Sort tests passed successfully.")


def main():
    test_merge_sort()
    test_quick_sort()
    print("All algorithm tests completed successfully.")


if __name__ == "__main__":
    main()