import random
import timeit
import matplotlib.pyplot as plt
from pathos.multiprocessing import ProcessPool
import os

def generate_random_array(n, m):
    return [random.randint(1, m) for _ in range(n)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def benchmark(args):
    n, m = args
    pid = os.getpid()
    print(f"[Process {pid}] Starting benchmark for n={n}, m={m}")

    total_time_bubble = 0
    total_time_insertion = 0
    
    for _ in range(1000):
        arr = generate_random_array(n, m)
        arr_copy_for_bubble = arr.copy()
        arr_copy_for_insertion = arr.copy()

        time_bubble = timeit.timeit(lambda: bubble_sort(arr_copy_for_bubble), number=1)
        total_time_bubble += time_bubble

        time_insertion = timeit.timeit(lambda: insertion_sort(arr_copy_for_insertion), number=1)
        total_time_insertion += time_insertion

    avg_time_bubble = (total_time_bubble / 1000) * 1000 # Convert to milliseconds
    avg_time_insertion = (total_time_insertion / 1000) * 1000 # Convert to milliseconds
    
    print(f"[Process {pid}] Completed benchmark for n={n}, m={m}.")
    return avg_time_bubble, avg_time_insertion


if __name__ == "__main__":
    n_values = [1000, 10000, 100000]
    m_values = [500, 5000, 50000]

    # If you have more than 2 cores, use all but two of them
    pool = ProcessPool(processes=max(1,os.cpu_count() - 2))
    print(f"Total CPU cores available: {os.cpu_count()} cores Using: {max(1,os.cpu_count() - 2)} cores")
    
    args_list = [(n, m) for n in n_values for m in m_values]
    results = pool.map(benchmark, args_list)

    print("Benchmarking completed!")

    bubble_sort_results = [res[0] for res in results]
    insertion_sort_results = [res[1] for res in results]

    plt.figure(figsize=(10, 6))

    x_ticks_labels = [f"{n}, {m}" for n in n_values for m in m_values]
    x_ticks_positions = range(len(x_ticks_labels))

    plt.plot(x_ticks_positions, bubble_sort_results, label='Bubble Sort', marker='o')
    plt.plot(x_ticks_positions, insertion_sort_results, label='Insertion Sort', marker='o')

    plt.xticks(ticks=x_ticks_positions, labels=x_ticks_labels, rotation=45)
    plt.xlabel('Array Size (n), Max Value (m)')
    plt.ylabel('Average Running Time (ms)')
    plt.legend()
    plt.title('Average Running Time of Bubble Sort and Insertion Sort')
    plt.tight_layout()
    plt.show()
