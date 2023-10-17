import random
import timeit
import matplotlib.pyplot as plt

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

# ...
n_values = [1000, 10000, 100000]
m_values = [500, 5000, 50000]

results = {'Bubble Sort': [], 'Insertion Sort': []}

for n in n_values:
    for m in m_values:
        total_time_bubble = 0
        total_time_insertion = 0
        for _ in range(1000):
            arr = generate_random_array(n, m)

            # Measure Bubble Sort time
            time_bubble = timeit.timeit(lambda: bubble_sort(arr.copy()), number=1)
            total_time_bubble += time_bubble

            # Measure Insertion Sort time
            time_insertion = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
            total_time_insertion += time_insertion

        avg_time_bubble = total_time_bubble / 1000
        avg_time_insertion = total_time_insertion / 1000
        results['Bubble Sort'].append(avg_time_bubble)
        results['Insertion Sort'].append(avg_time_insertion)

# Separate the results for each algorithm
bubble_sort_results = results['Bubble Sort'][:len(n_values)]
insertion_sort_results = results['Insertion Sort'][:len(n_values)]

plt.figure(figsize=(10, 6))

plt.plot(n_values, bubble_sort_results, label='Bubble Sort')
plt.plot(n_values, insertion_sort_results, label='Insertion Sort')

plt.xlabel('Array Size (n)')
plt.ylabel('Average Running Time (seconds)')
plt.legend()
plt.title('Average Running Time of Bubble Sort and Insertion Sort')
plt.show()
