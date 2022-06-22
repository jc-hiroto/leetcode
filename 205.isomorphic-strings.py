#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (42.08%)
# Likes:    3764
# Dislikes: 681
# Total Accepted:    515.4K
# Total Submissions: 1.2M
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.
# 
# 
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.
# 
# 
#

# @lc code=start
class Solution:
    def isIsomorphic(self, S: str, T: str) -> bool:
        smap = {}
        tmap = {}
        for s, t in zip(S, T):
            if s in smap and t != smap[s]:
                return False
            elif t in tmap and s != tmap[t]:
                return False
            elif s not in smap:
                smap[s] = t
                tmap[t] = s
        return True
# @lc code=end

