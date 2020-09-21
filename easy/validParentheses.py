"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


def isValidParentheses(str):
    stack = []
    brackets = {"}": "{", ")": "(", "]": "["}
    for char in str:
        if char in brackets:
            prev = stack.pop() if stack else '#'
            if prev != brackets[char]:
                return False
        else:
            stack.append(char)
