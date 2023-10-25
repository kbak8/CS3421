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
    n, m, f, num_runs = args
    pid = os.getpid()
    print(f"[Process {pid}] Starting {f.__name__} benchmark for n={n}, m={m}, runs={num_runs}")

    total_time = 0
    for _ in range(num_runs):
        arr = generate_random_array(n, m)
        time_bubble = timeit.timeit(lambda: f(arr), number=1)
        total_time += time_bubble

    avg_time = (total_time / num_runs) * 1000  # Convert to milliseconds
    
    print(f"[Process {pid}] Completed {f.__name__} benchmark for n={n}, m={m}. Average time: {avg_time:.2f} ms")
    return n, m, f.__name__, avg_time 


if __name__ == "__main__":
    n_values = [1000, 10000, 100000]
    m_values = [500, 5000, 50000]
    functions = [bubble_sort, insertion_sort]
    num_runs_dict = {n_values[0]: 1000, n_values[1]: 1000, n_values[2]: 10}  # Number of runs for each n value

    # If you have more than 2 cores, use all but two of them
    pool = ProcessPool(processes=max(1, os.cpu_count() - 2))
    print(f"Total CPU cores available: {os.cpu_count()} cores Using: {max(1, os.cpu_count() - 2)} cores")
    
    args_list = [(n, m, f, num_runs_dict[n], ) for n in n_values for m in m_values for f in functions] 
    results = pool.map(benchmark, args_list)

    print("Benchmarking completed!")

    bubble_sort_results = [res[3] for res in results if res[2] == "bubble_sort"]
    insertion_sort_results = [res[3] for res in results if res[2] == "insertion_sort"]

    plt.figure(figsize=(10, 6))

    x_ticks_labels = [f"{n}, {m}, runs:{num_runs_dict[n]}" for n in n_values for m in m_values]
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
