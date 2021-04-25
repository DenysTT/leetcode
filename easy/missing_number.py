"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

def miss_number(nums):
    for i,v in enumerate(sorted(nums)):
        if i == len(nums) - 1 and v != len(nums):
            return i + 1
        elif i != v or i == len(nums) - 1 and v != len(nums):
            return i
        
if __name__ == '__main__':
    miss_number([0,1])