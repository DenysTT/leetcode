"""Called a function called same, which accepts two arrays. The function should return true if every value in 
the array has corresponding value squared in the second array. The frequency of values must be the same"""
def is_doubled(arr_1, arr_2):
    freq_1 = {}
    freq_2 = {}
    if len(arr_1) != len(arr_2):
        return False
    for n in arr_1:
        if n not in freq_1:
            freq_1[n] = 1 
        else:
            freq_1[n] = freq_1[n] + 1
    for n in arr_2:
        if n not in freq_2:
            freq_2[n] = 1 
        else:
            freq_2[n] = freq_2[n] + 1
    for k,v in freq_1.items():
        if k*2 not in freq_2:
            return False
        if freq_2[k*2] != freq_1[k]:
            return False
    return True