def intersect(nums1, nums2):
    dict_1 = {}
    dict_2 = {}
    result = []
    for c1 in nums1:
        if c1 not in dict_1:
            dict_1[c1] = 1
        else:
            dict_1[c1] += 1
    for c2 in nums2:
        if c2 not in dict_2:
            dict_2[c2] = 1
        else:
            dict_2[c2] += 1
    if len(dict_1) > len(dict_2):
       for k in dict_2.keys():
            if k in dict_1:
                count = dict_2[k] if dict_2[k] < dict_1[k] else dict_1[k]
                for i in range(count):
                    result.append(k)
    else:
        for k in dict_1.keys():
            if k in dict_2:
                count = dict_2[k] if dict_2[k] < dict_1[k] else dict_1[k]
                for i in range(count):
                    result.append(k)
    return result

if __name__ == "__main__":
    intersect([1,2,2,1], [2,2])
        
        
