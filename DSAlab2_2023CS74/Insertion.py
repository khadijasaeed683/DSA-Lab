import funcs
import time


size=60000

# Problem 1 Driver Code (RandomArray(size))
random_array = funcs.RandomArray(size)
print("Random array values:", random_array)

# Problem 2 InsertionSort
array = funcs.RandomArray(size)
start_time = time.time()
funcs.InsertionSort(array, 0, len(array)-1)
end_time = time.time()
print("InsertionSort Time:", end_time - start_time)
with open("SortedInsertionSort.csv", "w") as file:
    for num in array:
        file.write(f"{num}\n")
        
# Problem 3 MergeSort
array = funcs.RandomArray(size)
start_time = time.time() #Record the start time
funcs.MergeSort(array, 0, len(array) - 1)     #Perform MergeSort
end_time = time.time()      #Record the end time
runtime = end_time - start_time    #Calculate and print the time taken
print(f"MergeSort Time for sorting an array of {size} elements: {runtime} seconds")

# Problem 4
n = 20  # Threshold for switching to InsertionSort
array = funcs.RandomArray(size) # Generate a random array
start_time = time.time()    # Measure the start time
funcs.HybridMergeSort(array, 0, len(array) - 1)     # Sort the array using HybridMergeSort
end_time = time.time()    # Measure the end time
runtime = end_time - start_time    # Calculate and print the time taken
print(f"HybridMergeSort Time for sorting an array of {size} elements: {runtime:.5f} seconds")

# Problem 5: Bubble sort
array=funcs.RandomArray(size)
start_time=time.time()
funcs.BubbleSort(array, 0, len(array) - 1)
end_time=time.time()
runtime = end_time - start_time    # Calculate and print the time taken
print(f"BubbleSort Time for sorting an array of {size} elements: {runtime:.5f} seconds")


# Problem 6 Selection sort
array = funcs.RandomArray(size)  # Generate random array 
start_time = time.time()    #measure starting time for selection sort
funcs.SelectionSort(array, 0, len(array) - 1) #implement function for selection sort
end_time = time.time()
print("SelectionSort Time:", end_time - start_time) #print selection sort

