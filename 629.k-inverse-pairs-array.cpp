/*
 * @lc app=leetcode id=629 lang=cpp
 *
 * [629] K Inverse Pairs Array
 *
 * https://leetcode.com/problems/k-inverse-pairs-array/description/
 *
 * algorithms
 * Hard (37.29%)
 * Likes:    1424
 * Dislikes: 161
 * Total Accepted:    40.8K
 * Total Submissions: 99.3K
 * Testcase Example:  '3\n0'
 *
 * For an integer array nums, an inverse pair is a pair of integers [i, j]
 * where 0 <= i < j < nums.length and nums[i] > nums[j].
 *
 * Given two integers n and k, return the number of different arrays consist of
 * numbers from 1 to n such that there are exactly k inverse pairs. Since the
 * answer can be huge, return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 3, k = 0
 * Output: 1
 * Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3
 * has exactly 0 inverse pairs.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 3, k = 1
 * Output: 2
 * Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 1000
 * 0 <= k <= 1000
 *
 *
 */

// @lc code=start
class Solution {
   public:
    int kInversePairs(int n, int k) {
        int MOD = 1e9 + 7;
        int dp[2][1001] = {1};
        for (int N = 1; N <= n; N++) {
            for (int K = 0; K <= k; K++) {
                dp[N % 2][K] =
                    (dp[(N - 1) % 2][K] + (K > 0 ? dp[N % 2][K - 1] : 0)) % MOD;
                if (K >= N) {
                    dp[N % 2][K] =
                        (MOD + dp[N % 2][K] - dp[(N - 1) % 2][K - N]) % MOD;
                }
            }
        }
        return dp[n % 2][k];
    }
};
// @lc code=end
