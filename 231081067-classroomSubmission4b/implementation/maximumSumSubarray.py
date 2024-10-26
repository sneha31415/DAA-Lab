def maxCrossingSum(arr, left, mid, right):
    left_sum = float('-inf')
    sum_left = 0
    start_left = mid

    for i in range(mid, left - 1, -1):
        sum_left += arr[i]
        if sum_left > left_sum:
            left_sum = sum_left
        # Update the starting index of the left subarray
            start_left = i

    right_sum = float('-inf')
    sum_right = 0
    start_right = mid + 1

    for i in range(mid + 1, right + 1): 
        sum_right += arr[i]
        if sum_right > right_sum:
            right_sum = sum_right
        # Update the starting index of the right subarray
            start_right = i

    return left_sum + right_sum, start_left, start_right


def maxSumSubarray(arr, left, right):
    # base case
    if left == right:
        return arr[left], left, left

    mid = (left + right) // 2

    # Find maximum subarray sum in left half, right half, and crossing
    leftSubarraySum, leftStart, leftStart = maxSumSubarray(arr, left, mid)
    rightSubarraySum, rightStart, rightEnd = maxSumSubarray(arr, mid + 1, right)
    crossSubarraySum, crossStart, crossEnd = maxCrossingSum(arr, left, mid, right)

    # Determine the maximum of the three possibilities
    if leftSubarraySum >= rightSubarraySum and leftSubarraySum >= crossSubarraySum:
        return leftSubarraySum, leftStart, leftStart
    elif rightSubarraySum >= leftSubarraySum and rightSubarraySum >= crossSubarraySum:
        return rightSubarraySum, rightStart, rightEnd
    else:
        return crossSubarraySum, crossStart, crossEnd


