import random

#problem 1: RandomArray(size)

def RandomArray(size):
    Array = [random.randint(1, 50000) for _ in range(size)]  #Implemented random function to populate array
    return Array

#problem 2: InsertionSort

def InsertionSort(array,start,end):
    for i in range(start + 1, end + 1): #starts with the 
        key = array[i]
        j = i - 1
        while j >= start and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        
def SaveData(array,fileName):          # function to store data in file
    file=open(file=fileName,mode='w')  # opens the file in write mode
    for a in array:                    # iterated till last element
        file.write(str(a)+'\n')        # writes element to new row
    file.close()                       # closes the file

# Problem 3 MergeSort

def Merge(array, p, q, r):
    L = array[p:q + 1]
    R = array[q + 1:r + 1]
    i = j = 0
    for k in range(p, r + 1):
        if i < len(L) and (j >= len(R) or L[i] <= R[j]):
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1

def MergeSort(array, start, end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)
        
        
 # Problem 4 HybridMergeSort
       
def HybridMergeSort(array, start, end):      #Hybrid sorting algorithm that uses InsertionSort for subarrays of size ≤ n, and MergeSort otherwise.

    if (end - start + 1) <= 100:  # If subarray size is less than or equal to n
        InsertionSort(array, start, end)  # Use InsertionSort
    else:
        mid = (start + end) // 2  # Otherwise, use MergeSort
        HybridMergeSort(array, start, mid )  # Sort the left half
        HybridMergeSort(array, mid + 1, end)  # Sort the right half
        Merge(array, start, mid, end)  # Merge the two sorted halves

# Problem 5  Bubble Sort
def BubbleSort(array, start, end):
    for i in range(start, end):
        for j in range(start, end - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

        
# Problem 6 Selection Sort     
        
def SelectionSort(array, start, end):
    for i in range(start, end + 1):
        min_index = i
        for j in range(i + 1, end + 1):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]          # Swap the found minimum element with the first element

