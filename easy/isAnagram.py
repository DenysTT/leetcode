"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""
s = 'anagram'
t = 'ganaram'
dict_1, dict_2 = {}, {}
for c in list(s):
    if c in dict_1:
        dict_1[c] += 1
    else:
        dict_1[c] = 1
for c in list(t):
     if c in dict_2:
         dict_2[c] += 1
     else:
         dict_2[c] = 1
if dict_1 == dict_2:
    print(1)