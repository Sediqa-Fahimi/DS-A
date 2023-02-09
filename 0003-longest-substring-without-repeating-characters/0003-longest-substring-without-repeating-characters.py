class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: # O(N) time | O(N) space
        max_length = 0
        curr_length = 0
        subString_set = set()
        start = 0
        end = 0
        while end < len(s):
            if(s[end] not in subString_set):
                subString_set.add(s[end])
                curr_length += 1
                end += 1
            else:
                max_length = max(max_length, curr_length)
                subString_set.remove(s[start])
                curr_length -= 1
                start += 1
        
        
        return max(max_length, curr_length)