"""
MSCS 532 - Assignment 2
Naga Naveena Chennupati

Performance comparison of Merge Sort and Quick Sort using
sorted, reverse-sorted, and random datasets.
"""

import csv
import random
import time
import tracemalloc
from pathlib import Path

from merge_sort import merge_sort
from quick_sort import quick_sort


# Dataset sizes used in the experiment.
DATASET_SIZES = [100, 1000, 5000, 10000, 20000]

# Run each timing test several times and report the average.
TIMING_TRIALS = 5

# Fixed seed makes the random datasets reproducible.
RANDOM_SEED = 532


def create_datasets(size):
    """Create sorted, reverse-sorted, and random datasets."""

    sorted_data = list(range(size))
    reverse_sorted_data = list(range(size, 0, -1))

    # Use unique random values to keep the comparison consistent.
    random_data = random.sample(range(size * 10), size)

    return {
        "Sorted": sorted_data,
        "Reverse Sorted": reverse_sorted_data,
        "Random": random_data,
    }


def run_algorithm(algorithm_name, data):
    """Run the selected sorting algorithm on the prepared dataset."""

    if algorithm_name == "Merge Sort":
        return merge_sort(data)

    quick_sort(data)
    return data


def measure_execution_time(algorithm_name, original_data):
    """Measure average execution time across multiple trials."""

    times = []

    for _ in range(TIMING_TRIALS):
        data = original_data.copy()

        start_time = time.perf_counter()

        result = run_algorithm(algorithm_name, data)

        end_time = time.perf_counter()

        assert result == sorted(original_data)

        times.append(end_time - start_time)

    average_seconds = sum(times) / len(times)

    return average_seconds * 1000


def measure_peak_memory(algorithm_name, original_data):
    """Measure peak Python memory used during the sorting operation."""

    data = original_data.copy()

    tracemalloc.start()

    result = run_algorithm(algorithm_name, data)

    _, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    assert result == sorted(original_data)

    return peak_memory / 1024

def run_benchmarks():
    """Run all performance tests and save the results to a CSV file."""

    random.seed(RANDOM_SEED)

    algorithms = ["Merge Sort", "Quick Sort"]
    results = []

    print("Starting performance tests...\n")

    for size in DATASET_SIZES:
        datasets = create_datasets(size)

        for dataset_type, dataset in datasets.items():
            for algorithm in algorithms:
                average_time = measure_execution_time(
                    algorithm,
                    dataset
                )

                peak_memory = measure_peak_memory(
                    algorithm,
                    dataset
                )

                results.append({
                    "Algorithm": algorithm,
                    "Dataset Type": dataset_type,
                    "Input Size": size,
                    "Average Time (ms)": round(average_time, 4),
                    "Peak Memory (KB)": round(peak_memory, 2),
                })

                print(
                    f"{algorithm:10} | "
                    f"{dataset_type:14} | "
                    f"n={size:<6} | "
                    f"Time={average_time:9.4f} ms | "
                    f"Memory={peak_memory:9.2f} KB"
                )

    save_results(results)

    print("\nPerformance testing completed successfully.")
    print("Results saved to results/performance_results.csv")


def save_results(results):
    """Save benchmark results to a CSV file."""

    results_folder = Path("results")
    results_folder.mkdir(exist_ok=True)

    output_file = results_folder / "performance_results.csv"

    fieldnames = [
        "Algorithm",
        "Dataset Type",
        "Input Size",
        "Average Time (ms)",
        "Peak Memory (KB)",
    ]

    with output_file.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    run_benchmarks()