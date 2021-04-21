"""
Given an array of integers and a number, write a function called
maxSubarraySum, which finds the maximum sum of a subarray with
the length of the number passed to the function.
Note that a subarray must consist of consecutive elements from the
original array. In the first example below, [100, 200, 300] is a subarray
of the original array but [100 300] is not
Examples:
1 maxSubarraySum([100,200,300,400], 2) // 700
2 maxSubarraySum([1,4,2,10,23,3,1,0,20], 4) // 39
3 maxSubarraySum([-3,4,0,-2,6,-1], 2) // 5
4 maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2) // 5
5 maxSubarraySum([2,3], 3) // null
"""

def max_subarray_sum(arr, n):
    maxsum = tempsum = sum(arr[0:n])
    for i in range(len(arr)):
        if n + i >= len(arr):
            return maxsum
        tempsum = tempsum - arr[i] + arr[n + i]
        maxsum = max(maxsum,tempsum)
