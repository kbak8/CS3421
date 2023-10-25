# CS4321 Project 1
# Kevin Bak, Patrick Janssen, Brennan Domerese, Ethan Jones
# 10/24/2023
#
# How to run:
# Ensure python is installed
# Run commands in elevated cmd prompt to install necessary library:
# python -m pip install -U pip
# python -m pip install -U matplotlib
#
# Navigate to directory containing bruteForce.py in cmd prompt
# python bruteForce.py

import random
import matplotlib.pyplot as plt

# Function: generate_random_array
# Author: group
# Takes a length (n) and maximum element value (m) as inputs.
# Returns an array of length n containing random numbers in the range [1..m]
# Cost:
#   Time complexity: O(n) (basic operation of generating random number n times)
#   Space compleity: O(n) (size of array directly proportional to space taken by program)
def generate_random_array(n, m):
    return [random.randint(1, m) for _ in range(n)]

# Function: is_unique
# Author: group
# Takes an array and performs a brute force comparison of all of its elements to determine if all elements are unique
# Returns true or false with the number of comparisons needed
# Cost:
#   Time complexity: O(n^2) (nested loops results in complexity of (n^2 - n)/2 = O(n^2))
#   Space compleity: O(n) (same array that was generated before, still takes O(n) space)
def is_unique(arr):
    comparisons = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[i] == arr[j]:
                return False, comparisons
    return True, comparisons

# Set up input variables (m = 1000, 10000)
m_values = [1000, 10000] # Maximum m-values for each array are 1000 and 10000. (Group 10 -> (100*10, 1000*10))
n_factors = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] # Determine length of array. (n_factors[i] * m = length)

# Main function
# Author: group
# This method takes the m-values and generates ten arrays with the lengths determined by the n_factors array.
# It fills these arrays with random numbers in the range [1..m], performs the brute force algorithm to check
# if the array is unique. It does this 1000 times for each value of m, calculates the average number of comparisons
# for each pair of (m, n) and finally generates a plot of the data.
# Cost:
#   Time complexity: O(n^2) (the call to is_unique is O(n^2) and it happens a constant number of times, which still reduces to O(n^2))
#   Space complexity: O(n) (the size of the array that gets generated here depends on n)
print("Average comparisons after 1000 runs:")
for m in m_values: # m-values is always a constant size
    index = 0
    average_comparisons = []
    for n_factor in n_factors: # n-factors is always a constant size
        n = int(n_factor * m)
        total_comparisons = 0
        for _ in range(1000): # generate 1000 random arrays for each (m, n) pair and calculate avg number of comparisons
            arr = generate_random_array(n, m)
            is_unique_result, comparisons = is_unique(arr)
            total_comparisons += comparisons
        average_comparisons.append(total_comparisons / 1000)
        print("Maximum m-value: " + str(m) + ", Length: " + str(n) + ", Average comparisons: " + str(average_comparisons[index]))
        index += 1
    plt.plot([n_factor * m for n_factor in n_factors], average_comparisons, label=f'm={m}')

# Generate plot of results
plt.xlabel('n')
plt.ylabel('Average Comparisons')
plt.legend()
plt.title('Average Comparisons vs. n for Different m Values')
plt.show()

