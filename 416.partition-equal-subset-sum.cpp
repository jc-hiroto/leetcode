/*
 * @lc app=leetcode id=416 lang=cpp
 *
 * [416] Partition Equal Subset Sum
 *
 * https://leetcode.com/problems/partition-equal-subset-sum/description/
 *
 * algorithms
 * Medium (46.39%)
 * Likes:    8115
 * Dislikes: 128
 * Total Accepted:    481K
 * Total Submissions: 1M
 * Testcase Example:  '[1,5,11,5]'
 *
 * Given a non-empty array nums containing only positive integers, find if the
 * array can be partitioned into two subsets such that the sum of elements in
 * both subsets is equal.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,5,11,5]
 * Output: true
 * Explanation: The array can be partitioned as [1, 5, 5] and [11].
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,2,3,5]
 * Output: false
 * Explanation: The array cannot be partitioned into equal sum subsets.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 200
 * 1 <= nums[i] <= 100
 *
 *
 */

// @lc code=start
class Solution {
   public:
    int memo[201][10001] = {[0 ... 200] = {[0 ... 10000] = -1}};
    bool canPartition(vector<int>& nums) {
        int total = accumulate(nums.begin(), nums.end(), 0);
        if (total % 2 != 0) {
            return false;
        }
        return dp(nums, total / 2, 0);
    }
    bool dp(vector<int>& nums, int sum, int i) {
        if (sum == 0) return true;
        if (i >= nums.size() || sum < 0) return false;
        if (memo[i][sum] != -1) return memo[i][sum];
        return memo[i][sum] =
                   dp(nums, sum - nums[i], i + 1) || dp(nums, sum, i + 1);
    }
};
// @lc code=end
