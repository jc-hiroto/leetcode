#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        rs = []
        rt = []
        for i in range(len(s)):
            if s[i] != '#':
                rs.append(s[i])
            elif rs:
                rs.pop()
        
        for i in range(len(t)):
            if t[i] != '#':
                rt.append(t[i])
            elif rt:
                rt.pop()
        
        return rs == rt
            

            
# @lc code=end

