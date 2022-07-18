/*
 * @lc app=leetcode id=560 lang=cpp
 *
 * [560] Subarray Sum Equals K
 *
 * https://leetcode.com/problems/subarray-sum-equals-k/description/
 *
 * algorithms
 * Medium (44.24%)
 * Likes:    14146
 * Dislikes: 442
 * Total Accepted:    817.2K
 * Total Submissions: 1.8M
 * Testcase Example:  '[1,1,1]\n2'
 *
 * Given an array of integers nums and an integer k, return the total number of
 * subarrays whose sum equals to k.
 *
 * A subarray is a contiguous non-empty sequence of elements within an
 * array.
 *
 *
 * Example 1:
 * Input: nums = [1,1,1], k = 2
 * Output: 2
 * Example 2:
 * Input: nums = [1,2,3], k = 3
 * Output: 2
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 2 * 10^4
 * -1000 <= nums[i] <= 1000
 * -10^7 <= k <= 10^7
 *
 *
 */

// @lc code=start
class Solution {
   public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> d;
        int pref_sum = 0, res = 0;
        d[0] = 1;
        for (int num : nums) {
            pref_sum += num;
            int find_sum = pref_sum - k;
            if (d.find(find_sum) != d.end()) {
                res += d[find_sum];
            }
            d[pref_sum]++;
        }
        return res;
    }
};
// @lc code=end
