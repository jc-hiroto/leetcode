/*
 * @lc app=leetcode id=322 lang=cpp
 *
 * [322] Coin Change
 *
 * https://leetcode.com/problems/coin-change/description/
 *
 * algorithms
 * Medium (40.09%)
 * Likes:    11974
 * Dislikes: 274
 * Total Accepted:    1M
 * Total Submissions: 2.5M
 * Testcase Example:  '[1,2,5]\n11'
 *
 * You are given an integer array coins representing coins of different
 * denominations and an integer amount representing a total amount of money.
 *
 * Return the fewest number of coins that you need to make up that amount. If
 * that amount of money cannot be made up by any combination of the coins,
 * return -1.
 *
 * You may assume that you have an infinite number of each kind of coin.
 *
 *
 * Example 1:
 *
 *
 * Input: coins = [1,2,5], amount = 11
 * Output: 3
 * Explanation: 11 = 5 + 5 + 1
 *
 *
 * Example 2:
 *
 *
 * Input: coins = [2], amount = 3
 * Output: -1
 *
 *
 * Example 3:
 *
 *
 * Input: coins = [1], amount = 0
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= coins.length <= 12
 * 1 <= coins[i] <= 2^31 - 1
 * 0 <= amount <= 10^4
 *
 *
 */

// @lc code=start
class Solution {
   public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0) return 0;
        queue<pair<int, int>> q;
        vector<bool> visited(amount + 1, false);
        visited[0] = true;
        q.push({0, 0});
        while (!q.empty()) {
            auto cur = q.front();
            q.pop();
            int cur_count = cur.first + 1;
            int cur_amount = cur.second;
            for (int coin : coins) {
                int new_amount = cur_amount + coin;
                if (new_amount == amount) return cur_count;
                if (new_amount < amount && !visited[new_amount]) {
                    visited[new_amount] = true;
                    q.push({cur_count, new_amount});
                }
            }
        }
        return -1;
    }
};
// @lc code=end
