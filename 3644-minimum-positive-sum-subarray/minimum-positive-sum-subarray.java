class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int n = nums.size();
        int res = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            int curr = 0;

            for (int j = i; j < n; j++) {
                curr += nums.get(j);

                int length = j - i + 1;

                if (length > r) {
                    break;
                }

                if (length >= l && curr > 0) {
                    res = Math.min(res, curr);
                }
            }
        }

        return res == Integer.MAX_VALUE ? -1 : res;
    }
}