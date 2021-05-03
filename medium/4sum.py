"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
def four_sum(nums, v):
    nums.sort()
    res = []
    if not nums or len(nums) == 1 and nums[0] == v:
        return []
    for j in range(len(nums)-3):
        if j > 0 and nums[j] == nums[j-1]:
            continue
        for i in range(j+1,len(nums)-2):
            if i > j + 1 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) -1
            while l < r:
                sum = nums[j] + nums[i] + nums[l] + nums[r]
                if sum > v:
                    r -= 1
                elif sum < v:
                    l += 1
                else:
                    res.append([nums[j], nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                            l += 1
                    while l < r and nums[r] == nums[r-1]:
                            r -= 1
                    l += 1
                    r -= 1
    return res



if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    four_sum([1,-2,-5,-4,-3,3,3,5], -11)
            