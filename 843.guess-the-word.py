#
# @lc app=leetcode id=843 lang=python3
#
# [843] Guess the Word
#
# https://leetcode.com/problems/guess-the-word/description/
#
# algorithms
# Hard (42.99%)
# Likes:    1235
# Dislikes: 1420
# Total Accepted:    118.5K
# Total Submissions: 276.9K
# Testcase Example:  '"acckzz"\n["acckzz","ccbazz","eiowzz","abcczz"]\n10'
#
# This is an interactive problem.
# 
# You are given an array of unique strings wordlist where wordlist[i] is 6
# letters long, and one word in this list is chosen as secret.
# 
# You may call Master.guess(word) to guess a word. The guessed word should have
# type string and must be from the original list with 6 lowercase letters.
# 
# This function returns an integer type, representing the number of exact
# matches (value and position) of your guess to the secret word. Also, if your
# guess is not in the given wordlist, it will return -1 instead.
# 
# For each test case, you have exactly 10 guesses to guess the word. At the end
# of any number of calls, if you have made 10 or fewer calls to Master.guess
# and at least one of these guesses was secret, then you pass the test case.
# 
# 
# Example 1:
# 
# 
# Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"],
# numguesses = 10
# Output: You guessed the secret word correctly.
# Explanation:
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6
# matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
# We made 5 calls to master.guess and one of them was the secret, so we pass
# the test case.
# 
# 
# Example 2:
# 
# 
# Input: secret = "hamada", wordlist = ["hamada","khaled"], numguesses = 10
# Output: You guessed the secret word correctly.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= wordlist.length <= 100
# wordlist[i].length == 6
# wordlist[i] consist of lowercase English letters.
# All the strings of wordlist are unique.
# secret exists in wordlist.
# numguesses == 10
# 
# 
#

# @lc code=start
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        def pair_match(a, b):
            return sum(c1 == c2 for c1, c2 in zip(a, b))
        
        def most_overlap():
            cnt = [[0] * 26 for _ in range(6)]
            for word in candidate:
                for i, c in enumerate(word):
                    cnt[i][ord(c) - ord("a")] += 1
            best = 0
            for word in candidate:
                score = 0
                for i, c in enumerate(word):
                    score += cnt[i][ord(c) - ord("a")]
                if score > best:
                    best = score
                    best_word = word
            return best_word

        candidate = wordlist[:]
        while candidate:
            s = most_overlap()
            match = master.guess(s)

            if match == 6:
                return

            candidate = [w for w in candidate if pair_match(s, w) == match]
# @lc code=end

