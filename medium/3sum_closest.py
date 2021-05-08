def threeSumClosest(nums, target):
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l,r = i + 1,len(nums)-1 
        while l < r:
            sum = nums[i] + nums[l] + nums[r] #1  sum = -4 
            if sum == target:
                return sum
            if abs(sum - target) < abs(result - target):
                result = sum
            if sum < target:
                l += 1
            else:
                r -= 1
    return result            
 
    



if __name__ == "__main__":
    print(threeSumClosest([1,2,4,8,16,32,64,128], 82 )
            