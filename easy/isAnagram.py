"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""


def isAnagram(str1, str2):
    dict_1, dict_2 = {}, {}

    for c in str1:
        if c in dict_1:
            dict_1[c] += 1
        else:
            dict_1[c] = 1
    for c in str2:
        if c in dict_2:
            dict_2[c] += 1
        else:
            dict_2[c] = 1
    return dict_1 == dict_2