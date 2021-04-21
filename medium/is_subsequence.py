"""
which takes in two strings and checks whether the characters in the first string form a subsequence of the characters in the second string. In other words, the function should check whether the characters in the first string appear somewhere in the second string,
isSubsequence('hello', 'hello world'); // true
isSubsequence('sing', 'sting'); // true
isSubsequence('abc', 'abracadabra'); // true
isSubsequence('abc', 'acb'); // false (order matters) 
"""

def is_subsequence(arr1, arr2):
    p1 = 0
    c_list1 = list(arr1)
    c_list2 = list(arr2)
    if len(c_list1) == 0 or len(c_list2) == 0 or len(c_list1) > len(c_list2):
        return False
    for n in range(len(c_list2)):
        if c_list1[p1] == c_list2[n]:
            p1 += 1
        if p1 > len(c_list1) - 1:
            return True
    return False