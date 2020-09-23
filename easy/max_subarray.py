"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""
def maxsubarray(nums):
    for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
    print(max(nums))


if __name__ == '__main__':
    maxsubarray([-2,1,-3,4,-1,2,1,-5,4])