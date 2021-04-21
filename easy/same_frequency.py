"""
Given two positive integers, find out if the two numbers have the same frequency of digits.
"""
def sameFrequency(val1, val2):
    dict_1 = {}
    dict_2 = {}
    if len(str(val1)) != len(str(val2)):
        return False
    for v in list(str(val1)):
        if v in dict_1:
            dict_1[v] += 1
        else:
            dict_1[v] = 1
    for v_2 in list(str(val2)):
        if v_2 in dict_2:
            dict_2[v_2] += 1
        else:
            dict_2[v_2] = 1
    print(dict_1 == dict_2)