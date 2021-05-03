"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
"""

def my_atoi(s):
    if not s:
        return False
    s = s.strip()
    max = 91283472332
    min = -91283472332
    if s[0].isalpha():
        return 0
    count = 0
    for c in range(1,len(s)):
        if not s[c].isdigit():
            break
        count += 1
    number = s[:count+1]
    res = int(number)
    if res > max:
        return max
    elif res < min:
        return min
    else:
        return res




if __name__ == "__main__":
    print(my_atoi("-42 words"))