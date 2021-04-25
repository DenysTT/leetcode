"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

def groupAnagrams(strs):
    sort_dict = {}
    for s in strs:
        sorted_v = tuple(sorted(s))
        if sorted_v in sort_dict:
            sort_dict[sorted_v].append(s)
        else:
            sort_dict[sorted_v] = [s]
    return [arr for arr in sort_dict.values()]

if __name == '__main__':
    groupAnagrams(["eat","tea","tan","ate","nat","bat"])