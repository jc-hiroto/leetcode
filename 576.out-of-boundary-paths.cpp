/*
 * @lc app=leetcode id=576 lang=cpp
 *
 * [576] Out of Boundary Paths
 *
 * https://leetcode.com/problems/out-of-boundary-paths/description/
 *
 * algorithms
 * Medium (40.12%)
 * Likes:    2092
 * Dislikes: 204
 * Total Accepted:    81K
 * Total Submissions: 192.7K
 * Testcase Example:  '2\n2\n2\n0\n0'
 *
 * There is an m x n grid with a ball. The ball is initially at the position
 * [startRow, startColumn]. You are allowed to move the ball to one of the four
 * adjacent cells in the grid (possibly out of the grid crossing the grid
 * boundary). You can apply at most maxMove moves to the ball.
 *
 * Given the five integers m, n, maxMove, startRow, startColumn, return the
 * number of paths to move the ball out of the grid boundary. Since the answer
 * can be very large, return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
 * Output: 6
 *
 *
 * Example 2:
 *
 *
 * Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
 * Output: 12
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= m, n <= 50
 * 0 <= maxMove <= 50
 * 0 <= startRow < m
 * 0 <= startColumn < n
 *
 *
 */

// @lc code=start
class Solution {
   public:
    int m, n;
    int memo[51][51][51];
    vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        this->m = m;
        this->n = n;
        memset(memo, -1, sizeof(memo));
        return dfs(startRow, startColumn, maxMove);
    }
    int dfs(int row, int col, int max_move) {
        if (row < 0 || row >= m || col < 0 || col >= n) return 1;
        if (max_move == 0) return 0;
        if (memo[row][col][max_move] != -1) return memo[row][col][max_move];
        int res = 0;
        for (auto& dir : dirs) {
            res += dfs(row + dir.first, col + dir.second, max_move - 1);
            res %= 1000000007;
        }
        memo[row][col][max_move] = res;
        return res;
    }
};
// @lc code=end
