"""
Write a function called minSubArrayLen which accepts two parameters - an a
positive integers and a positive integer.
This function should return the minimal length of a contiguous subarray of wh
greater than or equal to the integer passed to the function. If there isn't one, re
instead.
1 minSubArrayLen([2,3,1,2,4,3], 7) // 2 -> because [4,3] is the
2 minSubArrayLen([2,1,6,5,4], 9) // 2 -> because [5,4] is the sm
3 minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52) // 1 -> becau
4 minSubArrayLen([1,4,16,22,5,7,8,9,10],39) // 3
5 minSubArrayLen([1,4,16,22,5,7,8,9,10],55) // 5
6 minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11) // 2
7 minSubArrayLen([1,4,16,22,5,7,8,9,10],95) // 0
"""
def min_subarray_len(arr, v):
    start = 0
    end = 0
    sum = 0
    min_len = 100
    while start < len(arr) - 1:
        if sum < v and end < len(arr) - 1:
            end += 1
            sum += arr[end]
        elif sum >= v:
            min_len = min(min_len,end - start)
            sum -= arr[start]
            start += 1
        else:
            break
    return min_len