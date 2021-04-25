"""
169
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
"""
def majorityElement(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
        
def majorityElement_sort(nums):
    nums.sort()
    return nums[len(nums)//2]

if __name__ == "__main__":
    majorityElement_sort([3,2,3])
