import random
import matplotlib.pyplot as plt


def generate_random_array(n, m):
    return [random.randint(1, m) for _ in range(n)]


def is_unique(arr):
    comparisons = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[i] == arr[j]:
                return False, comparisons
    return True, comparisons


m_values = [1000, 10000] # Maximum m-values for each array are 1000 and 10000. (Group 10 -> (100*10, 1000*10))
n_factors = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] # Determine length of array. (n_factors[i] * m = length)

print("Average comparisons after 1000 runs:")

for m in m_values:
    index = 0
    average_comparisons = []
    for n_factor in n_factors:
        n = int(n_factor * m)
        total_comparisons = 0
        for _ in range(1000):
            arr = generate_random_array(n, m)
            is_unique_result, comparisons = is_unique(arr)
            total_comparisons += comparisons
        average_comparisons.append(total_comparisons / 1000)
        print("Maximum m-value: " + str(m) + ", Length: " + str(n) + ", Average comparisons: " + str(average_comparisons[index]))
        index += 1

    plt.plot([n_factor * m for n_factor in n_factors], average_comparisons, label=f'm={m}')

plt.xlabel('n')
plt.ylabel('Average Comparisons')
plt.legend()
plt.title('Average Comparisons vs. n for Different m Values')
plt.show()
