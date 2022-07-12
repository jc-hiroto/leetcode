/*
 * @lc app=leetcode id=473 lang=cpp
 *
 * [473] Matchsticks to Square
 *
 * https://leetcode.com/problems/matchsticks-to-square/description/
 *
 * algorithms
 * Medium (40.32%)
 * Likes:    2205
 * Dislikes: 164
 * Total Accepted:    92.6K
 * Total Submissions: 231.5K
 * Testcase Example:  '[1,1,2,2,2]'
 *
 * You are given an integer array matchsticks where matchsticks[i] is the
 * length of the i^th matchstick. You want to use all the matchsticks to make
 * one square. You should not break any stick, but you can link them up, and
 * each matchstick must be used exactly one time.
 *
 * Return true if you can make this square and false otherwise.
 *
 *
 * Example 1:
 *
 *
 * Input: matchsticks = [1,1,2,2,2]
 * Output: true
 * Explanation: You can form a square with length 2, one side of the square
 * came two sticks with length 1.
 *
 *
 * Example 2:
 *
 *
 * Input: matchsticks = [3,3,3,3,4]
 * Output: false
 * Explanation: You cannot find a way to form a square with all the
 * matchsticks.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= matchsticks.length <= 15
 * 1 <= matchsticks[i] <= 10^8
 *
 *
 */

// @lc code=start
class Solution {
   public:
    bool dfs(vector<int>& edges, const vector<int>& matches, int index,
             int target) {
        if (index == matches.size()) {
            return edges[0] == edges[1] && edges[1] == edges[2] &&
                   edges[2] == edges[3];
        }
        for (int i = 0; i < 4; i++) {
            if (edges[i] + matches[index] > target) continue;
            int j = i;
            while (--j >= 0) {
                if (edges[i] == edges[j]) break;
            }
            if (j != -1) continue;
            edges[i] += matches[index];
            if (dfs(edges, matches, index + 1, target)) {
                return true;
            }
            edges[i] -= matches[index];
        }
        return false;
    }
    bool makesquare(vector<int>& matchsticks) {
        if (matchsticks.size() < 4) return false;
        int total = 0;
        for (auto& i : matchsticks) {
            total += i;
        }
        if (total % 4 != 0) return false;
        sort(matchsticks.begin(), matchsticks.end(),
             [](int a, int b) { return a > b; });
        vector<int> edges = {0, 0, 0, 0};
        return dfs(edges, matchsticks, 0, total / 4);
    }
};
// @lc code=end
