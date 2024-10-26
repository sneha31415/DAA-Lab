import time, random
from maximumSumSubarray import *

def kadane (nums):
    runningSum = 0
    maxSum = float('-inf')
    for num in nums:
        runningSum += num
        maxSum = max(maxSum, runningSum)
        # if the running sum gets negative, its of no use to add it further
        if runningSum < 0:
            runningSum = 0
    return maxSum
    

def compare_algorithms(arr):
    # Timing Kadane's Algorithm
    startTime = time.time()
    kadaneResult = kadane(arr)
    kadane_time = time.time() - startTime
    
    # Timing Divide-and-Conquer Approach
    startTime = time.time()
    divideConquerResult = maxSumSubarray(arr, 0, len(arr) - 1)
    divideConquerTime = time.time() - startTime
    
    return (kadane_time, kadaneResult), (divideConquerTime, divideConquerResult)

# Generate a large random array of integers
n = 100000  
random_array = [random.randint(-1000, 1000) for _ in range(n)]


# Compare performance
kadanePerformance, divideConquerPerformance = compare_algorithms(random_array)

print(f"Kadane's Algorithm: Time = {kadanePerformance[0]:.6f}s, Max Subarray Sum = {kadanePerformance[1]}")
print(f"Divide-and-Conquer Algorithm: Time = {divideConquerPerformance[0]:.6f}s, Max Subarray Sum = {divideConquerPerformance[1][0]}")