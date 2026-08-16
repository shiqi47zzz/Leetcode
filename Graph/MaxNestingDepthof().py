'''
1614. Maximum Nesting Depth of the Parentheses

Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
'''

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0

        for i in range(len(s)):
            if s[i] is "(":
                depth += 1
                max_depth = max(depth, max_depth)
            elif s[i] is ")":
                depth -= 1
        return max_depth