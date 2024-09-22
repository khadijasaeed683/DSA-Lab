import funcs  #import all neccessary files
import random
import time

def ShuffleArray(array, start, end):  #function to shuffle the array
    for i in range(start, end + 1):
        rand_index = random.randint(start, end)  
        array[i], array[rand_index] = array[rand_index], array[i]

def read_words(filename):   # Read words from words.txt
    with open(filename, "r") as file:
        return [line.strip() for line in file]

# Task: Sort the words using InsertionSort and MergeSort
words = read_words("words.txt")

# Time Calculation for InsertionSort on words before shuffling
start_time = time.time()
funcs.InsertionSort(words, 0, len(words) - 1)
insertion_time = time.time() - start_time
print(f"InsertionSort Time (before shuffle): {insertion_time}")

# Time Calculation MergeSort on words before shuffling
words = read_words("words.txt")
start_time = time.time()
funcs.MergeSort(words, 0, len(words) - 1)
merge_time = time.time() - start_time
print(f"MergeSort Time (before shuffle): {merge_time}")

# Shuffle the words using function defined above
ShuffleArray(words, 0, len(words) - 1)

# Time InsertionSort after shuffling
start_time = time.time()
funcs.InsertionSort(words, 0, len(words) - 1)
insertion_time_shuffled = time.time() - start_time
print(f"InsertionSort Time (after shuffle): {insertion_time_shuffled}")

# Time MergeSort after shuffling
words = read_words("words.txt")
ShuffleArray(words, 0, len(words) - 1)
start_time = time.time()
funcs.MergeSort(words, 0, len(words) - 1)
merge_time_shuffled = time.time() - start_time
print(f"MergeSort Time (after shuffle): {merge_time_shuffled}")
