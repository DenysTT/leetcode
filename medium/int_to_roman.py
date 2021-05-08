"""
Overview
In a lot of countries, Roman Numerals are taught in elementary school-level math. This has made them a somewhat popular "easy" interview question. Unfortunately though, this ignores the fact that not everybody learned them in school, and therefore a big advantage has been given to those who did. I suspect it's also difficult for a lot of us who have learned them previously to fully appreciate how much easier prior experience makes this question. While this is very unfair, and possibly very frustrating, keep in mind that the best thing you can do is work through this question and the related question Roman to Integer so that you don't get caught out by it in a real interview. In short, if you're here reading this, you've saved yourself from getting caught out by it! Thankfully, questions that rely on this kind of prior knowledge are few and far between.

Have a go at Roman to Integer first

The problem of converting a Roman Numeral to an Integer is simpler. Therefore, we suggest that you have a go at it first if you're finding this question difficult. This will allow you to become more familiar with the concept of Roman Numerals without the "ambiguity" issue that comes up in converting an integer to a Roman Numeral. When converting a Roman Numeral to an integer, there's only one sensible conversion.

Roman Numeral Symbols

Roman Numerals are made with 7 single-letter symbols, each with its own value. Additionally, the subtractive rules (as explained in the problem description) give an additional 6 symbols. This gives us a total of 13 unique symbols (each symbol is made of either 1 letter or 2).
"""
class Solution:
    def intToRoman(self, num):
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
        
        res = ""
        
        for i in d:
            res += (num//i) * d[i]
            num %= i
        
        return res


if __name__ == "__main__":
    sl = Solution()
    sl.intToRoman(100)
