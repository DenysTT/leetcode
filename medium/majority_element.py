def majority_element(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    length = len(freq)-1 if len(nums) == 2 else len(freq)
    print([k for k,v in freq.items() if v > length/3])
    print()


if __name__ == '__main__':
    majority_element([3,2,3])
    majority_element([1,2])