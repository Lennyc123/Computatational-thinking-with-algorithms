# Importation of required modules in order for the application to function appropiately

# Usage of Pythons time module for the benchmarking process https://docs.python.org/3/library/time.html
import time
# Usage of Pythons random module for the generation of arrays containing random numbers https://docs.python.org/3/library/random.html
from random import randint
# Usage of Pandas to format the output of the benchmarking process within a pandas DataFrame https://pandas.pydata.org/docs/user_guide/10min.html
import pandas as pd
from pandas.core.frame import DataFrame

# Format the average running time of the algorithms to 3 decimal places
pd.set_option('precision', 3)

# A function that creates a series of random numbers within an array as specified by the input size of n
# n is passed as an argument within the function

def random_array(n):
    array1 = []
    for i in range(0, n, 1):
        array1.append(randint(0, 100))
    return array1

# A function that implements the sorting algorithm of Bubble Sort
# Code referenced from the following link: https://www.geeksforgeeks.org/bubble-sort/

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break
# End of Bubble Sort algorithm

# A function that implements the sorting algorithm of Merge Sort
# Code referenced from the following link: https://www.geeksforgeeks.org/merge-sort/

def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
# End of Merge Sort algorithm


# A function that implements the sorting algorithm of Counting Sort
# Code referenced from the following link: https://www.geeksforgeeks.org/counting-sort/

def countSort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1

    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

    return arr
# End of Counting Sort algorithm

# A function that implements the sorting algorithm of Selection Sort
# Code referenced from the following link: https://www.geeksforgeeks.org/selection-sort/

def selectionSort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
# End of Selection Sort algorithm

# A function that implements the sorting algorithm of Heap Sort
# Code referenced from the following link: https: // www.geeksforgeeks.org/heap-sort/

# To heapify subtree rooted at index i.
# n is size of heap

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1	 # left = 2*i + 1
    r = 2 * i + 2	 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size

def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
# End of Heap Sort algorithm


# Variable that is used for assinging the size of the random arrays i.e., how many elements are within the array
input_size = 100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000
# 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000

def main():
    # A function that benchmarks the average time of a particular sorting algorithm in milliseconds
    # The selected algorithm and input size are passed as arguments within the function
    def sortAvgTime(sortFunction, size):
        # the running time of a selected algorithm is added to an array i.e., benchmarks
        benchmarks = []
        # the running time is measured 10 times
        for i in range(10):
            # variable assigned to how many elements within an array should be randomly generated
            arr = random_array(size)
            # start the timer
            start_time = time.time() * 1000
            # call on the function i.e., specific sorting algorithm
            sortFunction(arr)
            # end the timer
            end_time = time.time() * 1000
            # calculate the running time of the algorithm
            time_elapsed = end_time - start_time
            # add the running time to the benchmarks list
            benchmarks.append(time_elapsed)
        # return the average of the benchmarks i.e., add up all the values and divide by the number of values, the for loop specifies how many values there will be.
        return sum(benchmarks)/10

    # A function that outputs benchmark values for the various sorting algorithms
    def benchmarkOutput():
        # The running time of each algorithm is stored within its relevant array
        bubbleBenchmarks = []
        mergeBenchmarks = []
        countBenchmarks = []
        selectionBenchmarks = []
        heapBenchmarks = []

        # Add the average running time of the algorithm to the arrays above
        # call on the sortAvgTime function and pass in the required arguments 
        for i in input_size:
            bubbleBenchmarks.append(sortAvgTime(bubbleSort, i))
            mergeBenchmarks.append(sortAvgTime(mergeSort, i))
            countBenchmarks.append(sortAvgTime(countSort, i))
            selectionBenchmarks.append(sortAvgTime(selectionSort, i))
            heapBenchmarks.append(sortAvgTime(heapSort, i))

        # Parameters for the pandas DataFrame i.e., formatting the output of the benchmark results
        # Labels for rows and columns of the DataFrame
        rows = "Bubble Sort", "Merge Sort", "Counting Sort", "Selection Sort", "Heap Sort"
        cols = 100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000
        # Data to place within the DataFrame
        output = bubbleBenchmarks, mergeBenchmarks, countBenchmarks, selectionBenchmarks, heapBenchmarks
        # Creation of the DataFrame using the parameters listed above 
        df = pd.DataFrame(output, index=list(rows), columns=list(cols))
        df.columns.name = 'Size'
        #Print the DataFrame
        print(df)

    # Call the function benchmarkOutput()
    benchmarkOutput()

if __name__ == "__main__":
    main()
