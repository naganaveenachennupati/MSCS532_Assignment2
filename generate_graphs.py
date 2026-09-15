"""
MSCS 532 - Assignment 2
Naga Naveena Chennupati

Creates performance graphs from the benchmark results.
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt


RESULTS_FILE = Path("results/performance_results.csv")
RESULTS_FOLDER = Path("results")


def load_results():
    """Read the benchmark results from the CSV file."""

    results = []

    with RESULTS_FILE.open("r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            results.append(
                {
                    "Algorithm": row["Algorithm"],
                    "Dataset Type": row["Dataset Type"],
                    "Input Size": int(row["Input Size"]),
                    "Average Time (ms)": float(row["Average Time (ms)"]),
                    "Peak Memory (KB)": float(row["Peak Memory (KB)"]),
                }
            )

    return results


def create_execution_time_graph(results):
    """Create a graph comparing execution times."""

    plt.figure(figsize=(10, 6))

    algorithms = ["Merge Sort", "Quick Sort"]
    dataset_types = ["Sorted", "Reverse Sorted", "Random"]

    for algorithm in algorithms:
        for dataset_type in dataset_types:
            selected = [
                row
                for row in results
                if row["Algorithm"] == algorithm
                and row["Dataset Type"] == dataset_type
            ]

            selected.sort(key=lambda row: row["Input Size"])

            sizes = [row["Input Size"] for row in selected]
            times = [row["Average Time (ms)"] for row in selected]

            plt.plot(
                sizes,
                times,
                marker="o",
                label=f"{algorithm} - {dataset_type}",
            )

    plt.title("Merge Sort and Quick Sort Execution Time")
    plt.xlabel("Input Size")
    plt.ylabel("Average Execution Time (ms)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_file = RESULTS_FOLDER / "execution_time.png"
    plt.savefig(output_file, dpi=300)
    plt.close()


def create_memory_graph(results):
    """Create a graph comparing measured peak memory usage."""

    plt.figure(figsize=(10, 6))

    algorithms = ["Merge Sort", "Quick Sort"]
    dataset_types = ["Sorted", "Reverse Sorted", "Random"]

    for algorithm in algorithms:
        for dataset_type in dataset_types:
            selected = [
                row
                for row in results
                if row["Algorithm"] == algorithm
                and row["Dataset Type"] == dataset_type
            ]

            selected.sort(key=lambda row: row["Input Size"])

            sizes = [row["Input Size"] for row in selected]
            memory = [row["Peak Memory (KB)"] for row in selected]

            plt.plot(
                sizes,
                memory,
                marker="o",
                label=f"{algorithm} - {dataset_type}",
            )

    plt.title("Merge Sort and Quick Sort Peak Memory Usage")
    plt.xlabel("Input Size")
    plt.ylabel("Peak Additional Memory (KB)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_file = RESULTS_FOLDER / "memory_usage.png"
    plt.savefig(output_file, dpi=300)
    plt.close()


def main():
    RESULTS_FOLDER.mkdir(exist_ok=True)

    results = load_results()

    create_execution_time_graph(results)
    create_memory_graph(results)

    print("Performance graphs created successfully.")
    print("Created: results/execution_time.png")
    print("Created: results/memory_usage.png")


if __name__ == "__main__":
    main()