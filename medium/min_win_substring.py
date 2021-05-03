
class Solution(object):
    def minWindow(self, search_string, target):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_letter_counts = {}
        for c in target:
            if c in target_letter_counts:
                target_letter_counts[c] +=1
            else:
                target_letter_counts[c] = 1 
        start = 0
        end = 0
        min_window = ""
        target_len = len(target)        
        
        for end in range(len(search_string)):
			# If we see a target letter, decrease the total target letter count
            if search_string[end] in target_letter_counts :
                if target_letter_counts[search_string[end]] > 0:
                    target_len -= 1

                # Decrease the letter count for the current letter
			    # If the letter is not a target letter, the count just becomes -ve
                target_letter_counts[search_string[end]] -= 1
            
			# If all letters in the target are found:
            while target_len == 0:
                end_SSSS = search_string[end]
                start_ssss = search_string[start]
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
					# Note the new minimum window
                    min_window = search_string[start : end + 1]
                    
				# Increase the letter count of the current letter
                if search_string[start] in target_letter_counts:
                    target_letter_counts[search_string[start]] += 1
                    
				    # If all target letters have been seen and now, a target letter is seen with count > 0
				    # Increase the target length to be found. This will break out of the loop
                    if target_letter_counts[search_string[start]] > 0:
                        target_len += 1
                    
                start+=1
                
        return min_window

    def min_window_2(self, s,t):
        win = {}
        for c in t:
            if c not in win:
                win[c] = 1
            else: win[c] += 1
        target_len = len(t)
        start,min_window = 0,0
        result = ""
        for end in range(len(s)):
            if s[end] in win:
                if win[s[end]] > 0:
                    target_len -= 1
                win[s[end]] -= 1
            while target_len == 0:
                min_window = end - start + 1
                if not result or len(result) > min_window:
                    result = s[start:end+1]
                if s[start] in win:
                    win[s[start]] += 1
                    if win[s[start]] > 0:
                        target_len += 1
                start += 1
        return result



if __name__ == '__main__':
    cl = Solution()
    print(cl.min_window_2("LADOBECABEBANC", "ABC"))


