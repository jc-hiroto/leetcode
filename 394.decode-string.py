#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (56.30%)
# Likes:    8359
# Dislikes: 362
# Total Accepted:    505.5K
# Total Submissions: 893.9K
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; there are no extra
# white spaces, square brackets are well-formed, etc. Furthermore, you may
# assume that the original data does not contain any digits and that digits are
# only for those repeat numbers, k. For example, there will not be input like
# 3a or 2[4].
# 
# The test cases are generated so that the length of the output will never
# exceed 10^5.
# 
# 
# Example 1:
# 
# 
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# 
# 
# Example 2:
# 
# 
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# 
# 
# Example 3:
# 
# 
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets
# '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
# 
# 
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = ""
        for c in s:
            if c == "[":
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ""
                cur_num = 0
            elif c == "]":
                times = stack.pop()
                cur_str = stack.pop() + cur_str * times
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_str += c
        return cur_str

        
# @lc code=end

