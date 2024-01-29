import timeit as t
import random as rnd
import matplotlib.pyplot as plt

# Insertion Sort
def insertion_sort(array):
    for ind in range(1, len(array)):
        ele = array[ind]
        index = ind - 1
        while index >= 0:
            if array[index] > ele:
                array[index + 1] = array[index]
                index -= 1
            else:
                break
        array[index + 1] = ele

# Bubble Sort
def bubble_sort(array):
     for a in range(len(array)):
        for b in range(len(array) - (a + 1)):
            if array[b] > array[b + 1]:
                array[b], array[b + 1] = array[b + 1], array[b]

# Selection Sort
def selection_sort(array):
     for start_ind in range(len(array)):
        smallest_element=array[start_ind]
        ele_ind=start_ind
        for i in range(start_ind+1,len(array)):
            if(array[i]<smallest_element):
                smallest_element=array[i]
                ele_ind=i
     
        array[start_ind],array[ele_ind]=array[ele_ind],array[start_ind]
# Function to generate a random array of a given size
def create_random_array(size):
    return [rnd.randint(1, 1000) for _ in range(size)]

# Function to benchmark sorting algorithms
def benchmark_sorting(sort_function, array):
    # Set up the code for benchmarking
    setup_code = f"from __main__ import {sort_function}, create_random_array; arr = create_random_array({len(array)})"
    stmt = f"{sort_function}(arr)"

    # Measure the execution time
    execution_time = t.timeit(stmt, setup=setup_code, number=10)

    return execution_time

# Benchmark parameters
array_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 4000, 6000]  # Adjust as needed

# Results dictionary to store benchmark results
sorting_results = {'Insertion Sort': [], 'Selection Sort': [], 'Bubble Sort': []}

# Run benchmarks for each sorting algorithm and array size
for size in array_sizes:
    array = create_random_array(size)

    # Benchmark each sorting algorithm
    insertion_time = benchmark_sorting('insertion_sort', array)
    sorting_results['Insertion Sort'].append(insertion_time)
    
    bubble_time = benchmark_sorting('bubble_sort', array)
    sorting_results['Bubble Sort'].append(bubble_time)
    
    selection_time = benchmark_sorting('selection_sort', array)
    sorting_results['Selection Sort'].append(selection_time)
   
# Plot the results
plt.plot(array_sizes, sorting_results['Insertion Sort'], label='Insertion Sort', color='purple')
plt.plot(array_sizes, sorting_results['Bubble Sort'], label='Bubble Sort', color='red')
plt.plot(array_sizes, sorting_results['Selection Sort'], label='Selection Sort', color='blue')

plt.xlabel('Array Size')
plt.ylabel('Executed time (sec)')
plt.title('Sorting Algorithms')
plt.legend()
plt.show()