class Solution {
    public int xorAfterQueries(int[] nums, int[][] queries) {
        int MOD = 1_000_000_007;

        for (int[] q : queries) {
            int l = q[0];
            int r = q[1];
            int k = q[2];
            int v = q[3];

            if (k == 0) {
                if (l >= 0 && l < nums.length) {
                    nums[l] = (int)((1L * nums[l] * v % MOD + MOD) % MOD);
                }
                continue;
            }

            int idx = l;
            while (idx <= r && idx < nums.length) {
                if (idx >= 0) {
                    nums[idx] = (int)((1L * nums[idx] * v % MOD + MOD) % MOD);
                }
                idx += k;
            }
        }

        int res = 0;
        for (int x : nums) {
            res ^= x;
        }

        return res;
    }
}