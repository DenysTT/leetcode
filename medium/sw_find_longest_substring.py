"""
Write a function which accepts a string and and returns the length of the longest substring with all distinct
characters.
1 findLongestSubstring('') // 0
2 findLongestSubstring('rithmschool') // 7
3 findLongestSubstring('thisisawesome') // 6
4 findLongestSubstring('thecatinthehat') // 7
5 findLongestSubstring('bbbbbb') // 1
6 findLongestSubstring('longestsubstring') // 8
7 findLongestSubstring('thisishowwedoit') // 6
"""

def find_longest_substring(str):
    s = list(str)
    max_lenght = start = 0
    used_char = {} 
    for i, v in enumerate(s):
        if v in used_char:
            start = max(start, used_char[v])
        max_lenght = max(max_lenght, i - start + 1)
        used_char[v] = i + 1 
    return max_lenght

if __name__ == "__main__":
    find_longest_substring("tmmzuxt")