from maximumSumSubarray import *

arr = [8, 1, 5, 1, 4, 2, 1, 4]
maxSum, startIdx, endIdx = maxSumSubarray(arr, 0, len(arr) - 1)
print(f"input array is : {arr} ")
print(f"maximum sum subarray is {arr[startIdx : endIdx + 1]}")
print(f"Maximum Subarray Sum: {maxSum} starting at '{startIdx}' and ending at '{endIdx}'")


arr = [-2, -1, -3, -4, -1, -2,  -5, -4]
maxSum, startIdx, endIdx = maxSumSubarray(arr, 0, len(arr) - 1)
print(f"input array is : {arr} ")
print(f"maximum sum subarray is {arr[startIdx : endIdx + 1]}")
print(f"Maximum Subarray Sum: {maxSum} starting at '{startIdx}' and ending at '{endIdx}'")

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSum, startIdx, endIdx = maxSumSubarray(arr, 0, len(arr) - 1)
print(f"input array is : {arr} ")
print(f"maximum sum subarray is {arr[startIdx : endIdx + 1]}")
print(f"Maximum Subarray Sum: {maxSum} starting at '{startIdx}' and ending at '{endIdx}'")

arr = [-2]
maxSum, startIdx, endIdx = maxSumSubarray(arr, 0, len(arr) - 1)
print(f"input array is : {arr} ")
print(f"maximum sum subarray is {arr[startIdx : endIdx + 1]}")
print(f"Maximum Subarray Sum: {maxSum} starting at '{startIdx}' and ending at '{endIdx}'")

arr = [-5]
maxSum, startIdx, endIdx = maxSumSubarray(arr, 0, len(arr) - 1)
print(arr)
print(f"Maximum Subarray Sum: {maxSum} starting at '{startIdx}' and ending at '{endIdx}'")