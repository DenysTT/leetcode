"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

def square_sorted_arr(s):
        if not nums:
            return []
        result = [i**2 for i in nums]
        result.sort()
        return result

if __name__ == "__main__":
    square_sorted_arr([-4,-1,0,3,10])