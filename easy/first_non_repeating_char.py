"""
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

"""

def get_first_uniq_char(s):
    freq_d = {}
    for i in s:
        if i not in freq_d:
            freq_d[i] = 1
        else:
            freq_d[i] += 1
    for i in s:
        if freq_d[i] == 1:
            print(i)
    print('no')