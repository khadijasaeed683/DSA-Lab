import csv
import funcs
import time

# Function to compare different sorting algorithms
def compare_sorting_algorithms(n_values):
    # List to store results of sorting times
    results = []

    # Iterate over each value of n
    for n in n_values:
        # Generate a random array of size n
        array = funcs.RandomArray(n)

        # Measure time for InsertionSort
        array_copy = array[:]  # Make a copy of the array
        start_time = time.time()  # Start timing
        funcs.InsertionSort(array_copy, 0, len(array_copy) - 1)  # Sort the array
        insertion_time = time.time() - start_time  # Calculate elapsed time

        # Measure time for MergeSort
        array_copy = array[:]
        start_time = time.time()
        funcs.MergeSort(array_copy, 0, len(array_copy) - 1)
        merge_time = time.time() - start_time

        # Measure time for HybridMergeSort
        array_copy = array[:]
        start_time = time.time()
        funcs.HybridMergeSort(array_copy, 0, len(array_copy) - 1)
        hybrid_time = time.time() - start_time

        # Measure time for BubbleSort
        array_copy = array[:]
        start_time = time.time()
        funcs.BubbleSort(array_copy, 0, len(array_copy) - 1)
        bubble_time = time.time() - start_time

        # Measure time for SelectionSort
        array_copy = array[:]
        start_time = time.time()
        funcs.SelectionSort(array_copy, 0, len(array_copy) - 1)
        selection_time = time.time() - start_time

        # Store the results for this value of n
        results.append([n, insertion_time, merge_time, hybrid_time, bubble_time, selection_time])

    return results

# Function to read n values from a file
def read_n_values(filename):
    n_values = []
    with open(filename, "r") as file:
        for line in file:
            n_values.append(int(line.strip()))  # Convert each line to an integer and add to list
    return n_values

# Function to save results to a CSV file
def save_results_to_csv(results, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["n", "InsertionSort", "MergeSort", "HybridMergeSort", "BubbleSort", "SelectionSort"])  # Write header
        writer.writerows(results)  # Write the data rows

# Read n values from a file named "Nvalues.txt"
n_values = read_n_values("Nvalues.txt")

# Compare sorting algorithms for the given n values
results = compare_sorting_algorithms(n_values)

# Save the results to a file named "RunTime.csv"
save_results_to_csv(results, "RunTime.csv")

# Print the results for verification
for result in results:
    print(f"n={result[0]}, InsertionSort: {result[1]:.6f}s, MergeSort: {result[2]:.6f}s, HybridMergeSort: {result[3]:.6f}s, BubbleSort: {result[4]:.6f}s, SelectionSort: {result[5]:.6f}s")
