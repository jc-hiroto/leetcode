#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (53.57%)
# Likes:    10549
# Dislikes: 689
# Total Accepted:    1.2M
# Total Submissions: 2.2M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# Example 2:
# 
# 
# Input: digits = ""
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: digits = "2"
# Output: ["a","b","c"]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# 
# 
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if not digits:
            return []
        res = []
        self.dfs(digits, digit_map, 0, "", res)
        return res

    def dfs(self, digits, digit_map, index, path, res):
        if index == len(digits):
            res.append(path)
            return
        for c in digit_map[digits[index]]:
            self.dfs(digits, digit_map, index + 1, path + c, res)

        
# @lc code=end

