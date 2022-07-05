#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (54.35%)
# Likes:    4683
# Dislikes: 254
# Total Accepted:    394.5K
# Total Submissions: 722.6K
# Testcase Example:  '["i","love","leetcode","i","love","coding"]\n2'
#
# Given an array of strings words and an integer k, return the k most frequent
# strings.
#
# Return the answer sorted by the frequency from highest to lowest. Sort the
# words with the same frequency by their lexicographical order.
#
#
# Example 1:
#
#
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
#
#
# Example 2:
#
#
# Input: words =
# ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# with the number of occurrence being 4, 3, 2 and 1 respectively.
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 500
# 1 <= words[i] <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]
#
#
#
# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
#
#

# @lc code=start
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wd_cnt = defaultdict(int)
        max_heap = []
        res = []
        for word in words:
            wd_cnt[word] += 1
        for word in wd_cnt:
            heappush(max_heap, (-wd_cnt[word], word))
        for _ in range(k):
            cnt, word = heappop(max_heap)
            res.append(word)
        return res

# @lc code=end
