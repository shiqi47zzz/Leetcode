'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        result = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            result = max(result, right - left + 1)
        return result
