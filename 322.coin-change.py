#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (40.09%)
# Likes:    11974
# Dislikes: 274
# Total Accepted:    1M
# Total Submissions: 2.5M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
# Example 1:
#
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Example 3:
#
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#

# @lc code=start
from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ DP Solution
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
        """

        # BFS solution
        if not amount:
            return 0
        q = deque([(0, 0)])
        visit = [True] + [False] * amount
        while q:
            total, value = q.popleft()
            total += 1
            for coin in coins:
                newVal = value + coin
                if newVal == amount:
                    return total
                if newVal < amount:
                    if not visit[newVal]:
                        visit[newVal] = True
                        q.append((total, newVal))
        return -1
# @lc code=end
