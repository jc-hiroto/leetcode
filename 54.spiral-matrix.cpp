/*
 * @lc app=leetcode id=54 lang=cpp
 *
 * [54] Spiral Matrix
 *
 * https://leetcode.com/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (41.38%)
 * Likes:    7763
 * Dislikes: 860
 * Total Accepted:    775.8K
 * Total Submissions: 1.8M
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * Given an m x n matrix, return all elements of the matrix in spiral order.
 *
 *
 * Example 1:
 *
 *
 * Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * Output: [1,2,3,6,9,8,7,4,5]
 *
 *
 * Example 2:
 *
 *
 * Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 *
 *
 *
 * Constraints:
 *
 *
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 10
 * -100 <= matrix[i][j] <= 100
 *
 *
 */

// @lc code=start
class Solution {
   public:
    vector<int> spiralOrder(vector<vector<int>>& mat) {
        vector<int> res;
        int r1 = 0, r2 = mat.size() - 1;
        int c1 = 0, c2 = mat[0].size() - 1;
        while (r1 <= r2 && c1 <= c2) {
            for (int i = c1; i <= c2; i++) res.push_back(mat[r1][i]);
            for (int i = r1 + 1; i <= r2; i++) res.push_back(mat[i][c2]);
            if (r1 < r2 && c1 < c2) {
                for (int i = c2 - 1; i > c1; i--) res.push_back(mat[r2][i]);
                for (int i = r2; i > r1; i--) res.push_back(mat[i][c1]);
            }
            r1++;
            c1++;
            r2--;
            c2--;
        }
        return res;
    }
};
// @lc code=end
